#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from collections import Counter
from datetime import datetime
from pathlib import Path
import re

AUTHOR = 'Sarath Dontireddy'
SITENAME = 'silverdreamracer.me'
SITETITLE = 'Sarath Dontireddy'
SITEURL = 'https://www.silverdreamracer.me'
SITEDESCRIPTION = 'Practical notes on integration architecture, AS/RS automation, cloud, and AI — by Sarath Dontireddy, Solution Architect.'
SITESUBTITLE = 'Solution Architect — Integration, AS/RS, Cloud, AI'
PYGMENTS_STYLE = "monokai"
THEME = 'Flex'

STATIC_PATHS = ["images", "extra/ads.txt", "extra/custom.css"]
CUSTOM_CSS = "custom.css"

DATE_FORMATS = {
    "en": "%B %d, %Y",
}
FAVICON = '/images/favicon.ico'

PATH = 'content'
CONTENT_ROOT = Path(__file__).parent / PATH
MENU_FOLDER_EXCLUDES = {"extra", "images", "pages"}
MENU_CATEGORY_EXCLUDES = {"misc", "WebSite", "website"}
ARTICLE_PATHS = [
    '.',
    'AI',
    'docker',
    'git',
    'supplychain',
]
PAGE_PATHS = ['pages']

TIMEZONE = "America/New_York"

DEFAULT_LANG = 'en'
USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
DISPLAY_PAGES_ON_MENU = False
HOME_HIDE_TAGS = False


def _menu_title(folder_name):
    overrides = {
        'AI': 'AI',
        'git': 'Git',
        'docker': 'Docker',
        'supplychain': 'Supply Chain',
    }
    return overrides.get(folder_name, folder_name.replace('-', ' ').replace('_', ' ').title())


def _menu_slug(folder_name):
    return re.sub(r'[^a-z0-9]+', '-', folder_name.lower()).strip('-')


def _folder_category(folder_name):
    category_values = []
    folder_path = CONTENT_ROOT / folder_name

    for article_path in sorted(folder_path.rglob('*.md')):
        with article_path.open(encoding='utf-8') as article_file:
            for _, line in zip(range(25), article_file):
                if line.lower().startswith('category:'):
                    category_values.append(line.split(':', 1)[1].strip())
                    break

    for category_name in category_values:
        if _menu_slug(category_name) == _menu_slug(folder_name):
            return category_name

    if category_values:
        return Counter(category_values).most_common(1)[0][0]

    return folder_name


CONTENT_MENU_FOLDERS = tuple(
    sorted(
        folder.name
        for folder in CONTENT_ROOT.iterdir()
        if folder.is_dir() and not folder.name.startswith('.') and folder.name not in MENU_FOLDER_EXCLUDES
    )
)

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

BROWSER_COLOR = "#333"
ROBOTS = "index, follow"

THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True

USE_LESS = True

COPYRIGHT_YEAR = "2026  silverdreamracer.me"


# Social widget
SOCIAL = (('twitter', 'https://twitter.com/sarathreddy'),
          ('linkedin', 'https://www.linkedin.com/in/sarath-dontireddy/'),
          ('wordpress', 'https://spaceageracer.wordpress.com/'),
          ('github', 'https://github.com/sdontireddy'))

LINKS_IN_NEW_TAB = "external"
LINKS = (
    ('📡 Supply Chain Tech Signals', 'https://supplychaintechsignals.com/'),
    ('🧠 Decision Intelligence', 'https://www.silverdreamracer.me/transaction-processing-to-decision-intelligence.html#transaction-processing-to-decision-intelligence'),
    ('🏭 Edge Servers in WMS', 'https://www.silverdreamracer.me/why-edge-servers-are-important-in-modern-wms.html#why-edge-servers-are-important-in-modern-wms'),
    ('🤖 Automation and Tasks', 'https://www.silverdreamracer.me/my-take-on-the-mckinsey-report-automation-is-coming-for-tasks-not-entire-professions.html#my-take-on-the-mckinsey-report-automation-is-coming-for-tasks-not-entire-professions'),
    ('🗂️ Local RAG Knowledge Base', 'https://github.com/sdontireddy/rag-knowledge-base'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

CATEGORY_URL = 'category/{slug}'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'

TAG_SAVE_AS = 'tag/{slug}.html'
TAGS_SAVE_AS = 'tags.html'


AUTHORS_BIO = {
  "sdontireddy": {
    "name": "Sarath Dontireddy",
    "cover": "/images/favicon.ico",
    "image": "/theme/img/profile.png",
    "location": "Jacksonville, FL",
    "bio": "Solution Architect focused on integration, AS/RS automation, cloud, and AI. <p><img src=\'https://images.credly.com/size/680x680/images/2b31a8f4-92c4-468d-87eb-33115d97f6f5/AWS-DataAnalytics-Specialty-2020.png\' alt=\'Cert\'>AWS Certified Data Analytics — Specialty</p>",
    "linkedin": "sarath-dontireddy/",
    "github": "sdontireddy",
    "twitter": "sarathreddy",
  }
}


def slugify_name(name):
    return re.sub(r'[^a-z0-9]+', '-', name.lower()).strip('-')


# ---- Static menu order — explicit, intentional ----
MENUITEMS = (
    ('About Me', '/aboutme.html'),
    ('Supply Chain', '/category/scm'),
    ('AI', '/category/ai/'),
    ('Infra', '/infra.html'),
    ('Projects', '/projects.html'),
)

GOOGLE_ADSENSE = {
    "ca_id": "ca-pub-4811615297206908",
    "page_level_ads": True,
    'ads': {
        'aside': '1234561',          # Side bar banner (all pages)
        'main_menu': '1234562',      # Banner before main menu (all pages)
        'index_top': '1234563',      # Banner after main menu (index only)
        'index_bottom': '1234564',   # Banner before footer (index only)
        'article_top': '1234565',    # Banner after article title (article only)
        'article_bottom': '1234566', # Banner after article content (article only)
    }
}
ADD_THIS_ID = 'ra-63dbd4845c561c7d'

EXTRA_PATH_METADATA = {
    "extra/ads.txt": {"path": "ads.txt"},
    "extra/custom.css": {"path": "custom.css"},
}

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.6,
        'indexes': 0.6,
        'pages': 0.5,
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly',
    }
}
