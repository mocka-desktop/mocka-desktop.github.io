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

Pushing to `main` triggers `.github/workflows/pages.yml`, which calls
Pelican's reusable `github_pages.yml` workflow to build with
`publishconf.py` and deploy. The Pages source must be set to GitHub Actions
in the repository settings.

Three details are easy to trip over:

- The reusable workflow builds with `--extra-settings SITEURL=...`, which
  overrides whatever `publishconf.py` sets. The canonical domain is
  therefore passed as the `siteurl` and `feed_domain` inputs in
  `pages.yml`. Changing the domain means changing it there too.
- Only `output/` is published, so the `CNAME` in the repository root never
  reaches the deployed site. `content/extra/CNAME` is the copy that does,
  mapped to the root by `EXTRA_PATH_METADATA`. Keep the two in step.
- The workflow tag is pinned to the Pelican release in `requirements.txt`,
  and `python` is pinned to the version local builds are verified against.
  Move them together.

To reproduce a deployment build locally, exactly as CI runs it:

```sh
.venv/bin/pelican --settings publishconf.py \
  --extra-settings SITEURL='"https://mocka-desktop.org"' \
                   FEED_DOMAIN='"https://mocka-desktop.org"' \
  --output output
```

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

An article can carry an optional cover image, shown on the article page and
in the news listing. It needs all three fields, because the dimensions
reserve the image's space before it loads:

```
Cover: images/news/example.webp
Cover_width: 1200
Cover_height: 630
Cover_alt: What the image shows
```

Put the file in `content/images/news/`, in WebP with a PNG of the same name
beside it, the way screenshots are handled.

## Conventions

- No JavaScript. The site works fully with JS disabled.
- No third-party requests. Fonts, images, CSS and scripts all come from
  this repository.
- No em dashes in content, templates or config strings. Use commas, colons,
  periods or parentheses.
- Every image needs alt text, plus explicit width and height.

## Placeholder images

One generated stand-in is still in place. Replace it at the same path and
pixel size and no template change is needed.

| File | Size | Used in | State |
|------|------|---------|-------|
| `content/images/screenshots/hero-desktop.{webp,jpg}` | 1600x900 | Hero, in the laptop frame | Real |
| `content/images/screenshots/dock-overview.{webp,png}` | 1200x400 | Mocka Dock feature story, in the window frame | Placeholder |

Still to come, listed in `PLAN.md` phase 7: `dock-app-menu` (optional
second feature story) and `social-card` (1200x630, for the Open Graph and
Twitter tags added in phase 8).

Every screenshot ships as WebP with one fallback beside it. Choose the
fallback by content, not by habit:

- **Photographic** (a desktop with a wallpaper): JPEG. The hero as a PNG is
  1327 KB against 121 KB as a JPEG, with no visible difference.
- **Flat interface** (a dock, a menu, a dialog): PNG, which stays sharp on
  hard edges and compresses such images well.

The macro assumes a PNG of the same name. For a JPEG, give the path
explicitly with a `fallback` key next to `image` in `HERO` or the
`FEATURES` entry.

Templates size images from the `width` and `height` in `pelicanconf.py`,
so update those if a replacement has different dimensions. Keeping the
aspect ratio avoids layout shift.

To regenerate the hero from a fresh 16:9 desktop capture:

```sh
magick shot.png -resize 1600x900 -strip -quality 82 \
  content/images/screenshots/hero-desktop.webp
magick shot.png -resize 1600x900 -strip -quality 82 \
  -sampling-factor 4:2:0 -interlace Plane \
  content/images/screenshots/hero-desktop.jpg
```

## License

Site content and code are released under the BSD-3-Clause license. See
`LICENSE`.