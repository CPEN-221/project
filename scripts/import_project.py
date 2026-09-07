#!/usr/bin/env python3
"""Convert the archived project handout into the published Jekyll page.

The archived Markdown is kept unchanged in ``source/``.  This importer fixes
formatting introduced by the document export, rewrites internal links, and
adds accessible local figures.  Run it whenever the archived copy changes.
"""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source" / "project-description.md"
OUTPUT = ROOT / "index.md"

FRONT_MATTER = """---
layout: default
title: Team project
description: Project stages, submission milestones, and supporting design notes for CPEN 221A.
term: Fall 2026
permalink: /
---

"""

SECTION_ANCHORS = {
    "Design your Team": "design-your-team",
    "Design Your Solution": "design-your-solution",
    "Requirements": "requirements",
    "Architecture": "architecture",
    "Plan": "plan",
    "Release": "release",
    "Evaluate and Triage": "evaluate-and-triage",
    "Reflect": "reflect",
}

FIGURES = {
    "![Image.jpeg](CPEN%20221A%20-%20Team%20Project.assets/Image.jpeg)": """<figure class="project-figure project-figure--compact">
  <img src="{{ '/assets/images/arithmetic-question.jpeg' | relative_url }}" alt="A hand-drawn multiplication game screen showing seven times four above a numeric keypad.">
  <figcaption>The game's question screen accepts a numeric answer from an on-screen keypad.</figcaption>
</figure>""",
    "![Image.jpeg](CPEN%20221A%20-%20Team%20Project.assets/Image%20(2).jpeg)": """<figure class="project-figure project-figure--compact">
  <img src="{{ '/assets/images/arithmetic-feedback.jpeg' | relative_url }}" alt="Two hand-drawn multiplication game screens showing an incorrect answer with a red X and a correct answer with a green check mark.">
  <figcaption>The feedback screen shows the outcome for two seconds before presenting the next question.</figcaption>
</figure>""",
    "![Image.jpeg](CPEN%20221A%20-%20Team%20Project.assets/Image%20(3).jpeg)": """<figure class="project-figure project-figure--compact">
  <img src="{{ '/assets/images/arithmetic-game-over.jpeg' | relative_url }}" alt="A hand-drawn game completion screen that says You have mastered multiplication and includes a reset button.">
  <figcaption>The completion screen lets the player reset their play history.</figcaption>
</figure>""",
    "![](CPEN%20221A%20-%20Team%20Project.assets/5BD007F4-0F1E-4C41-BC68-64FF85862847_jpeg_preview.png)": """<figure class="project-figure project-figure--wide">
  <img src="{{ '/assets/images/milestone-trail-marker.jpeg' | relative_url }}" alt="A yellow trail marker painted on a rock beside a mountain path, indicating an elevation of 2,000 metres.">
  <figcaption>The milestone schedule divides the project into staged submissions.</figcaption>
</figure>""",
    "![](CPEN%20221A%20-%20Team%20Project.assets/654BF96F-FFB9-45D8-9C2C-43FD7FA6DC36_jpeg_preview.png)": """<figure class="project-figure project-figure--wide">
  <img src="{{ '/assets/images/project-notes.jpeg' | relative_url }}" alt="An open notebook with handwritten annotations and diagrams resting on a desk.">
  <figcaption>The supporting notes collect the design and requirements material used across the project.</figcaption>
</figure>""",
}


def _rewrite_craft_link(match: re.Match[str]) -> str:
    label = match.group(1)
    anchor = SECTION_ANCHORS.get(label)
    if not anchor:
        return match.group(0)
    return f"[{label}](#{anchor})"


def render(source: str) -> str:
    """Return publishable Markdown generated from the archived handout."""
    lines = source.splitlines()

    if lines and lines[0].strip() == "# CPEN 221A - Team Project":
        lines = lines[1:]

    in_notes = False
    normalized: list[str] = []
    for line in lines:
        # Craft exports some real headings as block quotes.
        line = re.sub(r"^>\s+(#{1,6}\s+)", r"\1", line)

        # Craft also prefixes many list items with a redundant quote marker.
        line = re.sub(r"^(\s*(?:[-+*]|\d+\.)\s+)>+\s?", r"\1", line)

        if line.strip() == "# Notes":
            in_notes = True

        # The notes section was exported almost entirely as nested quotes.
        # Restore ordinary headings, paragraphs, and lists for readability.
        if in_notes:
            line = re.sub(r"^(\s*)>+\s?", r"\1", line)

        normalized.append(line)

    body = "\n".join(normalized).strip()

    body = re.sub(
        r"\[([^\]]+)\]\(craftdocs://[^)]+\)",
        _rewrite_craft_link,
        body,
    )
    body = body.replace("[requirements](Requirements)", "[requirements](#requirements)")
    body = body.replace(
        "[how products such as Facebook started|https://en.wikipedia.org/wiki/History_of_Facebook]",
        "[how products such as Facebook started](https://en.wikipedia.org/wiki/History_of_Facebook)",
    )

    for old, new in FIGURES.items():
        body = body.replace(old, new)

    # Remove a lone punctuation line left by the image export.
    body = re.sub(r"\n:\n", "\n", body)
    body = re.sub(r"\n{4,}", "\n\n\n", body)

    return FRONT_MATTER + body + "\n"


def main() -> None:
    OUTPUT.write_text(render(SOURCE.read_text(encoding="utf-8")), encoding="utf-8")
    print(f"Generated {OUTPUT.relative_to(ROOT)} from {SOURCE.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
