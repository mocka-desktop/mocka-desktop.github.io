# mocka-desktop.github.io

Website for the Mocka desktop project, built with [Pelican](https://getpelican.com)
and published to GitHub Pages at [mocka-desktop.org](https://mocka-desktop.org).

See `SPEC.md` for what the site contains and `PLAN.md` for the phased build.

## Build locally

```sh
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
```

Preview at http://localhost:8000, rebuilding as files change:

```sh
.venv/bin/pelican --listen --autoreload
```

Build the way the deployment does, into `output/`:

```sh
.venv/bin/pelican content -s publishconf.py
```

`pelicanconf.py` holds the development settings and all the site data.
`publishconf.py` imports it and overrides the parts that differ in
production: the absolute `SITEURL`, absolute URLs, and the Atom feed.

The virtualenv is the source of truth for dependencies. On FreeBSD and
GhostBSD there is no prebuilt wheel for the `watchfiles` dependency, so
`pip` compiles it from source and Rust has to be available
(`pkg install rust`).

## Deployment

Pushing to `main` triggers `.github/workflows/pages.yml`, which builds with
`publishconf.py` and deploys to GitHub Pages. The Pages source is set to
GitHub Actions, and `CNAME` holds the custom domain.

The Pelican version is pinned in `requirements.txt`. When bumping it, move
the reusable workflow in `pages.yml` to the matching release tag.

## Editing the site

Most of the site is data rather than markup. Templates read it from
`pelicanconf.py`, so these do not need any HTML changes:

| What | Setting |
|------|---------|
| Header navigation | `NAV_LINKS` |
| Card below the hero | `HIGHLIGHT` (empty or removed hides the card) |
| Components page and cards | `COMPONENTS` |
| Home page feature stories | `FEATURES` |
| The three "Why Mocka" blocks | `WHY_MOCKA` |
| Footer link groups | `FOOTER_LINKS` |
| Shared external URLs | `GITHUB_ORG_URL`, `DISCUSSIONS_URL`, `WIKI_URL`, `GHOSTBSD_URL`, `GHOSTBSD_DOWNLOAD_URL` |

Prose lives in `content/`: pages in `content/pages/`, news articles in
`content/news/`, images in `content/images/`.

To publish a news article, add a Markdown file to `content/news/` with
`Title`, `Date`, `Slug` and `Summary` metadata. It appears on `/news/`, in
the Atom feed, and in the announcements section of the home page. Point
`HIGHLIGHT` at it to feature it below the hero.

## Conventions

- No JavaScript. The site works fully with JS disabled.
- No third-party requests. Fonts, images, CSS and scripts all come from
  this repository.
- No em dashes in content, templates or config strings. Use commas, colons,
  periods or parentheses.
- Every image needs alt text, plus explicit width and height.

## Placeholder images

None yet. The screenshots listed in `PLAN.md` phase 7 are still to come. Any
placeholder standing in for a real screenshot gets recorded here, so they
are easy to find and replace.

## License

Site content and code are released under the BSD-3-Clause license. See
`LICENSE`.