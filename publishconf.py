import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *  # noqa: F401,F403

SITEURL = "https://mocka-desktop.org"
RELATIVE_URLS = False
FEED_ALL_ATOM = "feeds/news.atom.xml"
DELETE_OUTPUT_DIRECTORY = True