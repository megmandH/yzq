AUTHOR = 'Megmand'
SITENAME = 'Megmand'
SITEURL = ""

PATH = "content"

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'zh_CN'

OUTPUT_PATH = 'docs'

# THEME = 'simple'
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = False
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
DELETE_OUTPUT_DIRECTORY = True
# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

MENUITEMS = (
    ('首页','/homepage.html'),
    ('文档','/categories.html'),
    ('关于本站','pages/about-pages.html'),
)