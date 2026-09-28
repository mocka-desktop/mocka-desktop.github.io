# Mocka Website v1: Implementation Plan

This plan builds the first version of the Mocka website described in
`SPEC.md`. It is written for Claude Code. Work through the phases in order,
commit at the end of each phase, and stop for review where a phase says so.

Repository: `mocka-desktop/mocka-desktop.github.io`
Generator: Pelican (Markdown, Jinja2)
Hosting: GitHub Pages via GitHub Actions

## Decisions for v1

These defaults apply unless the maintainer says otherwise:

- English only. Do not add i18n plugins, but keep all user-facing strings in
  templates or `pelicanconf.py` (not scattered in CSS) so translation can be
  added later.
- No Patreon or donation links anywhere in v1.
- No JavaScript. The site must work fully with JS disabled.
- No third-party requests: no web fonts from CDNs, no analytics, no external
  images. Everything is served from the repository.
- Logo: a text wordmark ("Mocka") styled in CSS until a real logo exists.
- Screenshots: the maintainer provides them in
  `content/images/screenshots/`. Until then, use clearly marked placeholder
  images (see Phase 7).
- Writing style for all site copy: no em dashes. Use commas, colons,
  periods or parentheses instead.

## Phase 0: Prerequisites (maintainer, not Claude Code)

- [x] Create the `mocka-desktop.github.io` repository in the org.
- [x] Settings > Pages > Source: GitHub Actions.
- [x] Add `SPEC.md` and this `PLAN.md` to the repository root.
- [x] Custom domain `mocka-desktop.org` configured and HTTPS enforced.
- [ ] Provide screenshots when available (list in Phase 7).

## Phase 1: Project scaffold

Create:

```
.
├── .github/workflows/pages.yml
├── .gitignore
├── PLAN.md
├── README.md
├── SPEC.md
├── content/
│   ├── images/
│   │   ├── news/
│   │   └── screenshots/
│   ├── news/
│   └── pages/
├── pelicanconf.py
├── publishconf.py
├── requirements.txt
└── themes/mocka/
    ├── static/
    │   ├── css/
    │   └── img/
    └── templates/
        └── partials/
```

`requirements.txt`: Pelican with Markdown support, pinned to the current
stable release (check PyPI for the version, do not guess):

```
pelican[markdown]==<current stable>
```

`.gitignore`: `output/`, `__pycache__/`, `*.pyc`, `.venv/`, `cache/`.

`pelicanconf.py` (development settings):

```python
AUTHOR = "Mocka Desktop"
SITENAME = "Mocka"
SITESUBTITLE = "A desktop built from scratch for GhostBSD"
SITEURL = ""
TIMEZONE = "America/Moncton"
DEFAULT_LANG = "en"

PATH = "content"
THEME = "themes/mocka"
STATIC_PATHS = ["images"]
ARTICLE_PATHS = ["news"]
PAGE_PATHS = ["pages"]

# URLs
ARTICLE_URL = "news/{slug}/"
ARTICLE_SAVE_AS = "news/{slug}/index.html"
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"

# The home page is a page (content/pages/home.md) saved as index.html,
# so the article listing moves to /news/.
INDEX_SAVE_AS = "news/index.html"
DIRECT_TEMPLATES = ["index"]
DEFAULT_PAGINATION = 10
PAGINATION_PATTERNS = (
    (1, "{url}", "{save_as}"),
    (2, "{base_name}/page/{number}/", "{base_name}/page/{number}/index.html"),
)

# Disable pages the site does not use
AUTHOR_SAVE_AS = ""
AUTHORS_SAVE_AS = ""
CATEGORY_SAVE_AS = ""
CATEGORIES_SAVE_AS = ""
TAG_SAVE_AS = ""
TAGS_SAVE_AS = ""
ARCHIVES_SAVE_AS = ""

# Feeds are generated only in publishconf.py
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_DATE_FORMAT = "%B %-d, %Y"
RELATIVE_URLS = True
```

Structured data, also in `pelicanconf.py`:

```python
GITHUB_ORG_URL = "https://github.com/mocka-desktop"
DISCUSSIONS_URL = "https://github.com/orgs/mocka-desktop/discussions"
WIKI_URL = "<to be provided by maintainer>"
GHOSTBSD_URL = "https://www.ghostbsd.org"
GHOSTBSD_DOWNLOAD_URL = "https://www.ghostbsd.org/download"

NAV_LINKS = [
    ("Components", "components/", False),
    ("News", "news/", False),
    ("Docs", WIKI_URL, True),
    ("Community", DISCUSSIONS_URL, True),
    ("GitHub", GITHUB_ORG_URL, True),
]
# (label, url, is_external)

HIGHLIGHT = {
    "label": "New",
    "title": "Mocka Dock 0.0.1 alpha is out",
    "text": "Available in the next GhostBSD package update.",
    "url": "news/mocka-dock-0-0-1/",
}

COMPONENTS = [
    {
        "name": "Mocka Dock",
        "slug": "mocka-dock",
        "description": "Taskbar-style dock applet for the MATE panel.",
        "status": "Alpha",
        "repo": "https://github.com/mocka-desktop/mocka-dock",
        "release": "https://github.com/mocka-desktop/mocka-dock/releases/tag/0.0.1",
    },
    {
        "name": "Mocka Menu",
        "slug": "mocka-menu",
        "description": "Application menu with Classic and full-screen Launcher layouts.",
        "status": "Planned",
        "repo": None,
        "release": None,
    },
    {
        "name": "Settings tool",
        "slug": "settings",
        "description": "Appearance and UI settings, replacing mate-control-center.",
        "status": "Planned",
        "repo": None,
        "release": None,
    },
]

FEATURES = [
    {
        "component": "Mocka Dock",
        "title": "Your apps, one click away",
        "text": (
            "Pinned and running apps share one row of buttons. Pin by "
            "dragging from the menu, the desktop or the file manager, and "
            "right click any app for its actions, recent files and windows."
        ),
        "image": "images/screenshots/dock-overview.webp",
        "alt": "Mocka Dock on a GhostBSD panel with pinned and running apps",
    },
]

WHY_MOCKA = [
    ("Written from scratch",
     "Every component is new code, reverse engineered from how the MATE tools behave."),
    ("BSD first",
     "Built for FreeBSD and GhostBSD, with no Linux-specific assumptions."),
    ("Compatible with MATE",
     "Mix Mocka and MATE components while the transition happens."),
]

FOOTER_LINKS = {
    "Project": [("Components", "components/"), ("News", "news/"), ("About", "about/")],
    "Community": [("Discussions", DISCUSSIONS_URL), ("Get Involved", "get-involved/"),
                  ("GitHub", GITHUB_ORG_URL)],
    "Resources": [("Docs", WIKI_URL), ("GhostBSD", GHOSTBSD_URL)],
}
```

`publishconf.py`:

```python
import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *  # noqa

SITEURL = "https://mocka-desktop.org"
RELATIVE_URLS = False
FEED_ALL_ATOM = "feeds/news.atom.xml"
DELETE_OUTPUT_DIRECTORY = True
```

`README.md`: how to build locally (`pip install -r requirements.txt`,
`pelican --listen --autoreload`), how deployment works, where to edit the
highlight card and component list.

Acceptance: `pelican content` runs without errors or warnings on an empty
theme skeleton.

## Phase 2: Theme foundation

Files: `templates/base.html`, `partials/header.html`,
`partials/footer.html`, `static/css/main.css`.

`base.html`:

- `<!doctype html>`, `lang="en"`, viewport meta, charset.
- Blocks: `title`, `description`, `og` (Open Graph and Twitter card tags),
  `content`.
- Skip link to `#main`.
- Link to the Atom feed when `FEED_ALL_ATOM` is set.
- Favicon placeholder.

`main.css`:

- Design tokens as CSS custom properties on `:root`: colors, spacing scale,
  radii, font sizes, max content width.
- Palette direction: warm coffee tones as accents (espresso brown, caramel,
  cream) on neutral backgrounds. Keep it restrained, GNOME style: mostly
  white or near-black backgrounds, large type, generous spacing.
- Dark mode through `@media (prefers-color-scheme: dark)` overriding the
  same tokens.
- System font stack for body text and headings.
- Layout with CSS grid and flexbox, mobile first, breakpoints at roughly
  640 px and 1024 px.
- Visible focus styles on all interactive elements.
- Status badge styles: Alpha, Beta, Stable, Planned.
- Button styles: primary and secondary.

Header: wordmark on the left, navigation from `NAV_LINKS`. External links get
`rel="noopener"`. On narrow screens, navigation wraps or collapses using a
CSS-only pattern (`<details>` element), no JS.

Footer: link groups from `FOOTER_LINKS`, the line "Mocka is developed as part
of GhostBSD.", and "Released under the BSD-3-Clause license."

Acceptance: an empty page renders with header and footer in light and dark
mode, at 360 px and 1440 px widths.

**Stop for review** (maintainer checks the visual direction).

## Phase 3: Home page

Content file `content/pages/home.md`:

```
Title: Mocka
Slug: home
Save_as: index.html
URL:
Template: home
Status: hidden
```

`templates/home.html` assembles these partials in order:

1. `hero.html`: headline "A desktop built from scratch for GhostBSD.",
   subline "Mocka replaces MATE one component at a time, written from scratch
   and compatible with MATE along the way.", buttons "Try Mocka Dock" (to
   the Mocka Dock release URL) and "Follow development" (GitHub org). Visual:
   hero screenshot inside a CSS-drawn laptop frame (no frame image asset).
2. `highlight.html`: renders `HIGHLIGHT` as a card. Renders nothing if
   `HIGHLIGHT` is empty or missing.
3. `feature.html`: loops over `FEATURES`, alternating image left and right
   on wide screens, stacked on mobile. Screenshots in a CSS-drawn window
   frame.
4. Why Mocka: three blocks from `WHY_MOCKA`.
5. Get involved: four links (Code, Testing, Design, Translation), all
   pointing to `get-involved/` anchors.
6. Get Mocka: "Included in GhostBSD" with a button to
   `GHOSTBSD_DOWNLOAD_URL` and a link to the latest release notes.
7. `news_list.html`: the three most recent articles (title, date,
   summary) and a link to `/news/`.

Acceptance: every section renders from config data; removing an entry from
`FEATURES` or clearing `HIGHLIGHT` changes the page without template edits.

## Phase 4: Components page

`content/pages/components.md` with `Template: components`.

`templates/components.html`: intro paragraph, then a grid of
`component_card.html` from `COMPONENTS`: name, description, status badge,
"Source" and "Latest release" links (omitted when `None`).

Acceptance: three cards, Mocka Dock shows both links, planned components
show only the badge.

## Phase 5: News

`templates/index.html` (news listing): paginated list using
`news_list.html` in full mode (title, date, summary, optional cover image).

`templates/article.html`: title, date, body, optional cover image from a
`Cover:` metadata field, link back to `/news/`.

First article `content/news/2026-09-26-mocka-dock-0.0.1.md`:

```
Title: Mocka Dock 0.0.1 alpha
Date: 2026-09-26
Slug: mocka-dock-0-0-1
Summary: The first Mocka component is out for testing.
```

Body: write it from the release notes at
https://github.com/mocka-desktop/mocka-dock/releases/tag/0.0.1 (fetch them,
do not invent features). Cover: what Mocka is in two sentences, what works,
what is not in this release yet, that it will be available in the next
GhostBSD package update and preinstalled but not the default yet, how to add
it to the panel, and how to report bugs. Keep it under 500 words. Link to the
release notes for the full list and build instructions.

Acceptance: `/news/` lists the article, the article page renders, the home
page shows it in the announcements section, and the highlight card links to
it.

## Phase 6: Static pages

`templates/page.html`: title and body in a readable column.

`content/pages/about.md`, use this text verbatim:

```markdown
Title: About
Slug: about

## Why Mocka exists

Mocka is a GTK desktop built for FreeBSD and GhostBSD first.

Most desktop environments are designed on Linux and ported to the BSDs
afterward. They work, but they carry assumptions that don't belong on a BSD
system, and those assumptions show up as missing features, workarounds, and
patches that downstream projects have to maintain. Mocka starts from the
other side: FreeBSD and GhostBSD are the target platforms, not a port.

## Why reverse engineering instead of forking

The obvious path would have been to fork MATE and change it. We chose not to.

**A clean license.** Forked code keeps its original license. Writing every
component from scratch lets Mocka be released under the BSD-3-Clause
license, the same family of license as FreeBSD and GhostBSD themselves.

**No inherited assumptions.** A fork carries its history with it, including
the Linux-specific design decisions. New code can be designed around how
FreeBSD actually works from the first line.

**Compatibility without dependency.** Mocka components are reverse
engineered from how the MATE tools behave, not copied from their source.
That keeps Mocka compatible with MATE, so you can run Mocka and MATE
components side by side while the transition happens, and move over one
piece at a time.

## One component at a time

Mocka replaces MATE gradually until every part has been replaced. The first
component is Mocka Dock, a taskbar-style dock for the panel. The application
menu and a settings tool are next.

## The name

MATE is named after the South American drink, and one of its forks, Café,
kept the tradition going. Mocha is the project founder's favorite treat, so
it felt like the natural next cup. While researching whether any projects
were already called Mocha, he misspelled it with a "k" instead of an "h".
The typo stuck, and Mocha became Mocka.

## Part of GhostBSD

Mocka is developed as part of GhostBSD and ships with it. Development
happens in the open on GitHub, and everyone is welcome to test, report bugs,
and contribute.
```

`content/pages/get-involved.md`: four sections with anchors matching the
home page links:

- `#code`: repositories live in the GitHub org; open a pull request, discuss
  larger changes in Discussions first.
- `#testing`: install the alpha on GhostBSD, report bugs as GitHub issues in
  the component's repository, include steps, expected and actual results.
- `#design`: share mockups and ideas in Discussions.
- `#translation`: translations are not set up yet; say so and invite people
  to watch Discussions for the announcement.

Draft this page for maintainer review; keep it short.

Acceptance: `/about/` and `/get-involved/` render; home page anchors land on
the right sections.

**Stop for review** (maintainer reads all copy).

## Phase 7: Images

Expected screenshots, WebP plus PNG fallback, in
`content/images/screenshots/`:

| File | Content | Used in |
|------|---------|---------|
| `hero-desktop` | Full GhostBSD desktop with Mocka Dock on the panel | Hero |
| `dock-overview` | Close-up of the dock with pinned and running apps | Feature story |
| `dock-app-menu` | Right-click app menu with recent files | Feature story (optional) |
| `social-card` | 1200x630 image for Open Graph and Twitter | Meta tags |

Until real screenshots exist, generate placeholders with the same file
names and dimensions, a neutral background and the text "Screenshot
placeholder". Record in `README.md` which images are placeholders.

Use `<picture>` with WebP source and PNG fallback. Every `<img>` has `alt`,
`width`, `height` and `loading="lazy"` (except the hero image).

## Phase 8: Metadata and feed

- Per-page `<title>` in the form "Page title | Mocka" (home: "Mocka, a
  desktop built from scratch for GhostBSD").
- `<meta name="description">` from page or article summary, falling back to
  `SITESUBTITLE`.
- Open Graph and Twitter card tags, image defaults to `social-card`.
- Canonical URL on every page in production builds.
- Atom feed at `/feeds/news.atom.xml`, linked from `<head>` and the news
  page.
- `404.html` page (GitHub Pages serves it automatically), with links back
  to home and news.

## Phase 9: Deployment

`.github/workflows/pages.yml`:

```yaml
name: Deploy to GitHub Pages
on:
  push:
    branches: ["main"]
  workflow_dispatch:
jobs:
  deploy:
    uses: "getpelican/pelican/.github/workflows/github_pages.yml@<tag>"
    permissions:
      contents: "read"
      pages: "write"
      id-token: "write"
    with:
      settings: "publishconf.py"
      requirements: "-r requirements.txt"
```

Replace `<tag>` with the Pelican release tag matching `requirements.txt`.
Verify that `.github/workflows/github_pages.yml` exists at that tag in the
Pelican repository and check its current inputs before using it.

Acceptance: a push to `main` builds and deploys, and the site loads at
`https://mocka-desktop.org` over HTTPS, and `www.mocka-desktop.org` and
`mocka-desktop.github.io` redirect to it.

## Phase 10: Quality checks

Run before calling v1 done:

- [ ] `pelican content -s publishconf.py` builds with no warnings.
- [ ] Every internal link resolves (use a link checker on `output/`).
- [ ] HTML validates (e.g. `html5validator` or the Nu validator).
- [ ] Contrast meets WCAG AA in light and dark mode.
- [ ] Keyboard navigation works on every page, focus is always visible.
- [ ] Page works with JavaScript disabled (there should be none).
- [ ] No requests to external hosts when loading any page.
- [ ] Layout checked at 360, 768, 1024 and 1440 px.
- [ ] No em dashes in content or templates: `grep -rn "—" content themes`
      returns nothing.
- [ ] Every image has alt text.

## Out of scope for v1

Support/Patreon button, French translation, screenshot
gallery, search, analytics. See `SPEC.md` section 11.
