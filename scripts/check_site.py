#!/usr/bin/env python3
"""Validate the project site source and, when present, its Jekyll build."""

from __future__ import annotations

import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

from import_project import SOURCE, render


ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.md"
BUILD = ROOT / "_site"
ORIGINAL = ROOT.parent / "CPEN 221A - Team Project" / "CPEN 221A - Team Project.md"

REQUIRED_FILES = (
    "_config.yml",
    "_layouts/default.html",
    "index.md",
    "404.html",
    "assets/css/main.scss",
    "assets/js/site.js",
    "assets/fonts/fonts.css",
    "assets/images/arithmetic-question.jpeg",
    "assets/images/arithmetic-feedback.jpeg",
    "assets/images/arithmetic-game-over.jpeg",
    "assets/images/milestone-trail-marker.jpeg",
    "assets/images/project-notes.jpeg",
)

REQUIRED_SECTIONS = (
    "overview",
    "design-your-team",
    "design-your-solution",
    "requirements",
    "architecture",
    "plan",
    "release",
    "evaluate-and-triage",
    "reflect",
    "milestones",
    "notes",
)

REQUIRED_IMAGES = (
    "arithmetic-question.jpeg",
    "arithmetic-feedback.jpeg",
    "arithmetic-game-over.jpeg",
    "milestone-trail-marker.jpeg",
    "project-notes.jpeg",
)


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.ids: set[str] = set()
        self.references: list[tuple[str, str]] = []
        self.landmarks: set[str] = set()
        self.images_without_alt: list[str] = []
        self.title_parts: list[str] = []
        self._in_title = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        identifier = values.get("id")
        if identifier:
            self.ids.add(identifier)
        if tag in {"header", "nav", "main", "footer"}:
            self.landmarks.add(tag)
        if tag == "a" and values.get("href"):
            self.references.append(("href", values["href"] or ""))
        if tag in {"img", "script"} and values.get("src"):
            self.references.append(("src", values["src"] or ""))
        if tag == "link" and values.get("href"):
            self.references.append(("href", values["href"] or ""))
        if tag == "img" and not (values.get("alt") or "").strip():
            self.images_without_alt.append(values.get("src") or "unknown image")
        if tag == "title":
            self._in_title = True

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self._in_title = False

    def handle_data(self, data: str) -> None:
        if self._in_title:
            self.title_parts.append(data)


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def local_target(current_page: Path, url: str) -> tuple[Path, str] | None:
    parsed = urlsplit(url)
    if parsed.scheme or parsed.netloc or url.startswith(("mailto:", "tel:")):
        return None

    path = unquote(parsed.path)
    if path.startswith("/project"):
        path = path[len("/project") :]

    if path.startswith("/"):
        target = BUILD / path.lstrip("/")
    elif path:
        target = current_page.parent / path
    else:
        target = current_page

    if path.endswith("/") or target.is_dir():
        target = target / "index.html"

    return target, parsed.fragment


def check_source(errors: list[str]) -> None:
    for relative in REQUIRED_FILES:
        if not (ROOT / relative).is_file():
            fail(errors, f"missing required file: {relative}")

    config = (ROOT / "_config.yml").read_text(encoding="utf-8")
    if 'url: "https://cpen-221.github.io"' not in config:
        fail(errors, "_config.yml must use https://cpen-221.github.io")
    if 'baseurl: "/project"' not in config:
        fail(errors, "_config.yml must use /project as its baseurl")
    if (ROOT / ".github" / "workflows").exists():
        fail(errors, "GitHub Actions workflows are not allowed for branch publishing")

    source_text = SOURCE.read_text(encoding="utf-8")
    index_text = INDEX.read_text(encoding="utf-8") if INDEX.exists() else ""
    if index_text != render(source_text):
        fail(errors, "index.md is stale; run python3 scripts/import_project.py")

    if ORIGINAL.exists() and SOURCE.read_bytes() != ORIGINAL.read_bytes():
        fail(errors, "source/project-description.md differs from the imported handout")

    for heading in (
        "# Overview",
        "# Design your Team",
        "# Design Your Solution",
        "# Requirements",
        "# Architecture",
        "# Plan",
        "# Release",
        "# Evaluate and Triage",
        "# Reflect",
        "# Milestones",
        "# Notes",
    ):
        if heading not in index_text:
            fail(errors, f"missing project section: {heading}")

    for stale in ("craftdocs://", "CPEN%20221A%20-%20Team%20Project.assets"):
        if stale in index_text:
            fail(errors, f"stale exported reference remains in index.md: {stale}")

    for image in REQUIRED_IMAGES:
        if index_text.count(image) != 1:
            fail(errors, f"expected one reference to {image} in index.md")

    image_tags = re.findall(r"<img\b[^>]*>", index_text)
    if len(image_tags) != len(REQUIRED_IMAGES):
        fail(errors, f"expected {len(REQUIRED_IMAGES)} image tags in index.md")
    for tag in image_tags:
        match = re.search(r'\balt="([^"]*)"', tag)
        if not match or not match.group(1).strip():
            fail(errors, f"image is missing alt text: {tag}")

    font_css = (ROOT / "assets" / "fonts" / "fonts.css").read_text(encoding="utf-8")
    if "IBM Plex Sans" not in font_css or "IBM Plex Mono" not in font_css:
        fail(errors, "local IBM Plex font declarations are incomplete")
    for value in re.findall(r"url\((?:['\"])?([^)'\"]+)", font_css):
        font = ROOT / "assets" / "fonts" / value
        if not font.is_file():
            fail(errors, f"missing font referenced by fonts.css: {value}")


def check_build(errors: list[str]) -> None:
    if not BUILD.exists():
        print("Build directory not present; skipped rendered-site checks.")
        return

    html_files = sorted(BUILD.rglob("*.html"))
    if not html_files:
        fail(errors, "_site contains no HTML files")
        return

    parsed_pages: dict[Path, PageParser] = {}
    for page in html_files:
        parser = PageParser()
        parser.feed(page.read_text(encoding="utf-8"))
        parsed_pages[page.resolve()] = parser

    home = (BUILD / "index.html").resolve()
    if home not in parsed_pages:
        fail(errors, "built home page is missing")
        return

    home_parser = parsed_pages[home]
    missing_landmarks = {"header", "nav", "main", "footer"} - home_parser.landmarks
    if missing_landmarks:
        fail(errors, f"home page is missing landmarks: {', '.join(sorted(missing_landmarks))}")
    missing_sections = set(REQUIRED_SECTIONS) - home_parser.ids
    if missing_sections:
        fail(errors, f"home page is missing section ids: {', '.join(sorted(missing_sections))}")
    if "Team project" not in "".join(home_parser.title_parts):
        fail(errors, "built home page title is incorrect")

    for page, parser in parsed_pages.items():
        for image in parser.images_without_alt:
            fail(errors, f"{page.relative_to(BUILD.resolve())}: image has empty alt text: {image}")

        for attribute, url in parser.references:
            local = local_target(page, url)
            if local is None:
                continue
            target, fragment = local
            target = target.resolve()
            if not target.exists():
                fail(
                    errors,
                    f"{page.relative_to(BUILD.resolve())}: broken local {attribute} {url}",
                )
                continue
            if fragment and target.suffix == ".html":
                target_parser = parsed_pages.get(target)
                if target_parser and fragment not in target_parser.ids:
                    fail(
                        errors,
                        f"{page.relative_to(BUILD.resolve())}: missing fragment #{fragment} in {url}",
                    )


def main() -> int:
    errors: list[str] = []
    check_source(errors)
    check_build(errors)

    if errors:
        print("Site checks failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Project site checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
