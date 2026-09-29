AUTHOR = "Mocka Desktop"
SITENAME = "Mocka"
SITESUBTITLE = "A desktop built from scratch for GhostBSD"
SITEURL = ""
TIMEZONE = "America/Moncton"
DEFAULT_LANG = "en"

PATH = "content"
THEME = "themes/mocka"
STATIC_PATHS = ["images", "extra/favicon.ico", "extra/CNAME"]
ARTICLE_PATHS = ["news"]
PAGE_PATHS = ["pages"]

# Files that belong at the site root rather than under a directory.
# favicon.ico because browsers request it there whatever the <link> tags
# say, and CNAME because the workflow publishes output/ and the copy in
# the repository root never reaches it.
EXTRA_PATH_METADATA = {
    "extra/favicon.ico": {"path": "favicon.ico"},
    "extra/CNAME": {"path": "CNAME"},
}

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

# Pelican's default, plus .gitkeep. Those only exist so git tracks the
# empty directories of the scaffold, and they should not reach output/.
IGNORE_FILES = ["**/.*", ".gitkeep"]

# Site data. Templates render these, so nothing below is hardcoded in HTML.

GITHUB_ORG_URL = "https://github.com/mocka-desktop"
DISCUSSIONS_URL = "https://github.com/orgs/mocka-desktop/discussions"
WIKI_URL = "https://github.com/mocka-desktop/mocka-dock/wiki"
GHOSTBSD_URL = "https://www.ghostbsd.org"
GHOSTBSD_DOWNLOAD_URL = "https://www.ghostbsd.org/download"

# (label, url, is_external)
NAV_LINKS = [
    ("Components", "components/", False),
    ("News", "news/", False),
    ("Docs", WIKI_URL, True),
    ("Community", DISCUSSIONS_URL, True),
    ("GitHub", GITHUB_ORG_URL, True),
]

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
        "repo": "https://github.com/mocka-desktop/mocka-menu",
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

HERO = {
    "headline": "A desktop built from scratch for GhostBSD.",
    "subline": (
        "Mocka replaces MATE one component at a time, written from scratch "
        "and compatible with MATE along the way."
    ),
    "image": "images/screenshots/hero-desktop.webp",
    "alt": "A GhostBSD desktop with Mocka Dock on the panel",
    "width": 1600,
    "height": 900,
}

# Images are given as the WebP path. Templates serve that through a
# <picture> and fall back to the PNG of the same name.
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
        "width": 1200,
        "height": 400,
    },
]

# (title, text, anchor). The anchors match the sections of get-involved.md.
GET_INVOLVED = [
    ("Code",
     "Every component is a repository in the GitHub org. Open a pull "
     "request, or raise larger changes in Discussions first.",
     "code"),
    ("Testing",
     "Run the alpha on GhostBSD and report what breaks, with the steps "
     "that led there.",
     "testing"),
    ("Design",
     "Share mockups, icons and interface ideas in Discussions.",
     "design"),
    ("Translation",
     "Not set up yet. Watch Discussions for the announcement.",
     "translation"),
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