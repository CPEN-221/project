# CPEN 221 Fall 2026 team project

This directory is a self-contained Jekyll site for the CPEN 221A team project.
The published guide is in `index.md`; the imported description is retained in
`source/project-description.md`. Run `python3 scripts/import_project.py` after
updating the imported description.

The site shares the course syllabus's institutional visual system and self-hosted
IBM Plex Sans and IBM Plex Mono fonts.

## Preview locally

Use Ruby 3.3 and run:

```sh
bundle install
bundle exec jekyll serve --livereload
```

Run the validation checks after changing the content or layout:

```sh
python3 scripts/check_site.py
```

## Publish with GitHub Pages

This site is configured for `https://cpen-221.github.io/project/`. If the GitHub
repository uses a different name, update `baseurl` in `_config.yml` to match it.

In the repository settings, open **Pages** and choose **Deploy from a branch**.
Select the `main` branch and the `/(root)` folder. GitHub Pages will run Jekyll and
publish the site after each push. No GitHub Actions workflow is needed.
