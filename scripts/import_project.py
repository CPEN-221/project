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

PUBLICATION_REPLACEMENTS = {
    "Students should define a project and work on it over ~7 weeks (Oct 20 - December 5).":
        "Project work begins in Week 2, on September 16, and continues through December 9.",
    "The scope of the project should reflect group size and be equivalent of 1 credit of work. In other words, each student should expect to spend ~3 hours a week on the project. This would be ~15 person hours of work each week and ~105 person hours of work over the entire term.":
        "The scope of the project should reflect the group size and require approximately 105 person-hours for a five-person team. Starting in Week 2 gives teams more time for design and iteration; it is not intended to increase the project scope.",
    "**Your design should be something your team can implement in *4 weeks* of part-time effort**":
        "**Your design should be something your team can implement in *5 weeks* of part-time effort**",
    "In about four weeks, you're going to launch your 1.0 product.":
        "In about five weeks, you're going to launch your 1.0 product.",
    "How will you use your time over the next four weeks?":
        "How will you use your time over the next five weeks?",
    "    - **Demos will be on December 4, during the regular lecture time in Kaiser 2020/2030**\n    - Video submission only needed if live demo cannot be done for any purpose. ":
        "    - **Live-demo details will be announced separately.**\n    - Submit a video only if a live demo cannot be completed.",
}

MILESTONE_SECTION = """# Milestones

<figure class="project-figure project-figure--wide">
  <img src="{{ '/assets/images/milestone-trail-marker.jpeg' | relative_url }}" alt="A yellow trail marker painted on a rock beside a mountain path, indicating an elevation of 2,000 metres.">
  <figcaption>The milestone schedule divides the project into staged submissions.</figcaption>
</figure>

The project launches on **Wednesday, September 16**. Each deliverable has its own milestone so that teams receive feedback before moving to the next stage.

The project has a weight of 25, divided across the phases of project work. We will assign a letter grade or score between 0 and 10 for each submission. Every deadline below is **11:59 p.m. Pacific Time** on the date shown.

| Milestone | Deliverable | Due | Points |
|---|---|---:|---:|
| 1 | [Design your Team](#design-your-team) | Friday, September 25 | 3 |
| 2 | [Design Your Solution](#design-your-solution) | Friday, October 2 | 2 |
| 3 | [Requirements](#requirements) | Friday, October 9 | 2 |
| 4 | [Architecture](#architecture) | Friday, October 16 | 2 |
| 5 | [Plan](#plan) | Friday, October 23 | 6 |
| 6 | [Release](#release) | Friday, November 27 | 5 |
| 7 | [Evaluate](#evaluate-and-triage) | Wednesday, December 2 | 2 |
| 8 | [Triage](#evaluate-and-triage) | Friday, December 4 | 1 |
| 9 | [Reflect](#reflect) *(individual)* | Wednesday, December 9 | 2 |
"""

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

    for old, new in PUBLICATION_REPLACEMENTS.items():
        if old not in body:
            raise ValueError(f"Expected source text was not found: {old}")
        body = body.replace(old, new)

    body, milestone_count = re.subn(
        r"# Milestones\n.*?\n---\n\n# Notes",
        MILESTONE_SECTION.rstrip() + "\n\n---\n\n# Notes",
        body,
        count=1,
        flags=re.DOTALL,
    )
    if milestone_count != 1:
        raise ValueError("Could not replace the archived milestone schedule")

    # Remove a lone punctuation line left by the image export.
    body = re.sub(r"\n:\n", "\n", body)
    body = re.sub(r"\n{4,}", "\n\n\n", body)

    return FRONT_MATTER + body + "\n"


def main() -> None:
    OUTPUT.write_text(render(SOURCE.read_text(encoding="utf-8")), encoding="utf-8")
    print(f"Generated {OUTPUT.relative_to(ROOT)} from {SOURCE.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
