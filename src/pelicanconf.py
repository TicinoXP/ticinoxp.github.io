#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'TicinoXP'
SITENAME = u'TicinoXP'
SITEURL = ''



PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'it'
THEME = "themes/pelican-bootstrap3"
SITELOGO = "images/ticinoxp-75.png"
HIDE_SITENAME = True
SITELOGO_SIZE="75px"
STATIC_PATHS = ["images"]

GOOGLE_ANALYTICS = 'UA-44802996-3'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
SHOW_ARTICLE_CATEGORY = True
DISPLAY_ARTICLE_INFO_ON_INDEX = True
DISPLAY_PAGES_ON_MENU = True



PAGE_URL = "{slug}"
PAGE_SAVE_AS = "{slug}.html"
CATEGORY_URL = "{slug}"
CATEGORY_SAVE_AS = "{slug}.html"
ARTICLE_URL = "{slug}"
ARTICLE_SAVE_AS = "{slug}.html"
TAG_URL = "tag/{slug}"
TAG_SAVE_AS = "tag/{name}.html"
AUTHORS_SAVE_AS = "authors"
AUTHOR_SAVE_AS = "author/{slug}.html"
AUTHOR_URL = "author/{slug}"
ARCHIVES_SAVE_AS = "archives.html"

# Blogroll
LINKS = (('Code Games Repo', 'http://github.com/ticinoxp/code-games'),

         ('MilanoJS', 'http://milanojs.com/'),
         ('Varese XPug', 'https://groups.google.com/forum/#!forum/varese-xpug'),
        )

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/ticinoxp'),
          ('github', 'http://github.com/ticinoxp'),
          ('reddit', 'http://reddit.com/r/TicinoXP'),
          ('google groups' , 'https://groups.google.com/g/ticinoxp'))

DEFAULT_PAGINATION = False

DISPLAY_TAGS_ON_SIDEBAR = False
DISPLAY_BREADCRUMBS = True

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
BOOTSTRAP_THEME = "arialdo"
NEWEST_FIRST_ARCHIVES = True

OUTPUT_PATH = '../'
