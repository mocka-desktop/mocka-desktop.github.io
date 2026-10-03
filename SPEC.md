# Mocka Website Specification

Status: Draft
Repository: `mocka-desktop/mocka-desktop.github.io`

## 1. Purpose

The Mocka website is the public home of the Mocka desktop project. It explains
what Mocka is, shows the components that exist today, announces releases, and
points visitors to GhostBSD, GitHub, the wiki and Discussions.

The first version targets a small project with one shipping component
(Mocka Dock). The design must be able to grow toward a larger community site
(KDE style) without a redesign.

## 2. Scope

In scope:

- Landing page
- Components page
- News (release announcements and project updates)
- Static pages (About, Get Involved)

Out of scope (handled elsewhere):

- Documentation: GitHub wiki
- Community forum: GitHub Discussions
- Bug tracking: GitHub issues per component repository
- Downloads: GhostBSD packages and ISO

## 3. Stack

| Item | Choice |
|------|--------|
| Generator | Pelican (Markdown content, Jinja2 templates) |
| Hosting | GitHub Pages, organization site |
| Build and deploy | GitHub Actions using Pelican's reusable `github_pages.yml` workflow, pinned to a release tag |
| Pages source | Settings > Pages > Source: GitHub Actions |
| URL | `https://mocka-desktop.org` (custom domain, verified at the org level, HTTPS enforced) |
| JavaScript | None required. Site must work fully without JS |

## 4. Site map

```
/                       Landing page (custom home template)
/components/            Components overview
/news/                  News listing, newest first
/news/<slug>/           Article
/get-involved/          How to contribute
/about/                 About the project and its relation to GhostBSD
/feeds/                 Atom feed for news
```

External links in navigation: Docs (GitHub wiki), Community (GitHub
Discussions), GitHub (org page).

## 5. Landing page

Design reference: gnome.org for structure and tone (product storytelling,
short navigation, visual sections). kde.org as the long-term reference for a
larger site.

Sections, in order:

1. **Header**
   Logo and "Mocka" on the left. Navigation: Components, News, Docs,
   Community, GitHub. No Support button in the first version.

2. **Hero**
   Headline: "A desktop built from scratch for GhostBSD."
   Subline: "Mocka replaces MATE one component at a time, written from scratch
   and compatible with MATE along the way."
   Buttons: "Try Mocka Dock" (current release) and "Follow development"
   (GitHub org).
   Visual: laptop device frame containing a GhostBSD desktop screenshot with
   Mocka Dock on the panel.

3. **Highlight card**
   One card below the hero, pattern borrowed from gnome.org. Used for the
   current release while the project is young, for example:
   "Mocka Dock 0.0.1 alpha is out. Available in the next GhostBSD package
   update." Links to the news article. Later it can carry other campaigns
   (donations, events). Content comes from config, not the template.

4. **Feature stories**
   One section per shipping component, alternating image left and right.
   First version: Mocka Dock only (pinning, app menu with recent files and
   desktop actions, window list). Menu and settings sections are added when
   those components ship.

5. **Why Mocka**
   Three blocks:
   - Written from scratch: every component is new code, written from its
     own specification and sharing no code with MATE.
   - BSD first: built for FreeBSD and GhostBSD, no Linux-specific assumptions.
   - Compatible with MATE: mix Mocka and MATE components during the
     transition.

6. **Get involved**
   Links by team: Code, Testing, Design, Translation. Targets: GitHub,
   Discussions, wiki.

7. **Get Mocka**
   "Included in GhostBSD" with a link to the GhostBSD download page and a link
   to the latest release notes.

8. **Announcements**
   The three most recent news articles with date and summary, plus a link to
   `/news/`.

9. **Footer**
   Grouped links: Project (Components, News, About), Community (Discussions,
   Get Involved, GitHub), Resources (Docs, GhostBSD).
   Line: "Mocka is developed as part of GhostBSD." License: BSD-3-Clause.

## 6. Other pages

**Components** (`/components/`)
One card per component: name, one-line description, status badge (Alpha,
Beta, Stable, Planned), links to repository and latest release.
Initial entries:

| Component | Description | Status |
|-----------|-------------|--------|
| Mocka Dock | Taskbar-style dock applet for the MATE panel | Alpha |
| Mocka Menu | Application menu with Classic and full-screen Launcher layouts | Planned |
| Settings tool | Appearance and UI settings, replacing mate-control-center | Planned (name not final) |

**News** (`/news/`)
Paginated list of articles: title, date, summary, optional cover image.

**Article** (`/news/<slug>/`)
Title, date, author, body, optional cover image, link back to news.

**Get Involved** and **About**
Standard content pages.

## 7. Content model

```
content/
  pages/
    home.md            (save_as: index.html, template: home)
    components.md      (template: components)
    get-involved.md
    about.md
  news/
    2026-09-26-mocka-dock-0.0.1.md
  images/
    screenshots/
    news/
```

Structured data lives in `pelicanconf.py` so templates render it without
editing HTML:

- `HIGHLIGHT`: title, text, link, optional label
- `COMPONENTS`: list of name, slug, description, status, repo URL, release URL
- `FEATURES`: list of feature story blocks (title, text, image, alt text)
- `NAV_LINKS` and `FOOTER_LINKS`

Pelican settings of note:

- `INDEX_SAVE_AS = 'news/index.html'` so the blog index does not take `/`
- `ARTICLE_URL = 'news/{slug}/'`, `ARTICLE_SAVE_AS = 'news/{slug}/index.html'`
- `PAGE_URL = '{slug}/'`, `PAGE_SAVE_AS = '{slug}/index.html'`
- Atom feed for news only; category, tag and author pages disabled

## 8. Theme

```
themes/mocka/
  templates/
    base.html
    home.html
    components.html
    page.html
    article.html
    index.html          (news listing)
    partials/
      header.html
      footer.html
      hero.html
      highlight.html
      feature.html
      component_card.html
      news_list.html
  static/
    css/main.css
    img/
```

Requirements:

- Sections are reusable Jinja2 partials so new pages can be assembled from
  existing blocks.
- Light and dark mode through `prefers-color-scheme`, colors defined as CSS
  custom properties.
- Responsive from 360 px wide phones to wide desktops.
- System font stack or one self-hosted font; no third-party font or asset
  requests.
- Screenshots shown in device frames (laptop for full desktop, window frame
  for component close-ups).

## 9. Quality requirements

- Accessibility: semantic HTML, alt text on every image, visible focus
  styles, WCAG AA contrast in both color schemes.
- Performance: no JavaScript by default, images in WebP with PNG fallback,
  explicit width and height on images.
- SEO and sharing: title and description per page, Open Graph and Twitter
  card tags with a default social image.
- No analytics or tracking in the first version.

## 10. Deployment

- Push to `main` triggers the workflow, which builds with `publishconf.py`
  and deploys to Pages.
- `requirements.txt` pins Pelican and its plugins.
- Local preview with `pelican --listen --autoreload`.

## 11. Future additions

- Donate / Support button in the header and a Support section (Patreon)
- French translation (i18n_subsites plugin)
- Feature stories for Mocka Menu and the settings tool
- Screenshots gallery
- Events or "Mocka for you" style audience pages as the project grows

## 12. Open questions

- Should Patreon appear as text links in Get Involved and the footer before
  the Support button is added?
- English only at launch, or English and French from the start? Deciding
  early avoids retrofitting URLs and templates.
- Logo, color palette and typography for Mocka.
- Illustrations, or screenshots only?
- Final name of the settings tool.
