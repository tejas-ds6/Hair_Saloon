"""
Django settings for hair_saloon project.
"""

from pathlib import Path

# ============================================================
# BASE DIRECTORY
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent


# ============================================================
# SECURITY
# ============================================================

SECRET_KEY = 'django-insecure-sxl4zxfgzqzib+d+0fz&o#fu5xdnvey8w#ey*0*g4l3d95&_mv'

DEBUG = True

ALLOWED_HOSTS = []


# ============================================================
# APPLICATIONS
# ============================================================

INSTALLED_APPS = [

    # Jazzmin must be before django.contrib.admin
    'jazzmin',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'customers',
]


# ============================================================
# JAZZMIN SETTINGS
# ============================================================

JAZZMIN_SETTINGS = {

    "site_title": "Hair Salon Admin",

    "site_header": "Hair Salon",

    "site_brand": "Hair Salon",

    "welcome_sign": "Welcome to Hair Salon Administration",

    "copyright": "Hair Salon",

    "show_sidebar": True,

    "navigation_expanded": True,

    "topmenu_links": [
        {
            "name": "Dashboard",
            "url": "admin:index",
        },
    ],

    "usermenu_links": [
        {
            "name": "View Website",
            "url": "/",
            "new_window": True,
        },
    ],

    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
    },

    "default_icon_parents": "fas fa-folder",
    "default_icon_children": "fas fa-circle",

    "related_modal_active": True,

    "show_ui_builder": False,

    "changeform_format": "horizontal_tabs",
}


# ============================================================
# JAZZMIN UI TWEAKS
# ============================================================

JAZZMIN_UI_TWEAKS = {

    "navbar_small_text": False,

    "footer_small_text": False,

    "body_small_text": False,

    "brand_small_text": False,

    "brand_colour": "navbar-dark",

    "accent": "accent-info",

    "navbar": "navbar-dark",

    "no_navbar_border": False,

    "sidebar": "sidebar-dark-info",

    "sidebar_nav_small_text": False,

    "sidebar_disable_expand": False,

    "sidebar_nav_child_indent": True,

    "sidebar_nav_compact_style": False,

    "sidebar_nav_legacy_style": False,

    "sidebar_nav_flat_style": False,

    "theme": "default",

    "dark_mode_theme": "darkly",
}


# ============================================================
# MIDDLEWARE
# ============================================================

MIDDLEWARE = [

    'django.middleware.security.SecurityMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',

    'django.middleware.common.CommonMiddleware',

    'django.middleware.csrf.CsrfViewMiddleware',

    'django.contrib.auth.middleware.AuthenticationMiddleware',

    'django.contrib.messages.middleware.MessageMiddleware',

    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# ============================================================
# URL CONFIGURATION
# ============================================================

ROOT_URLCONF = 'hair_saloon.urls'


# ============================================================
# TEMPLATES
# ============================================================

TEMPLATES = [

    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        # IMPORTANT
        # Django will look for templates here
        'DIRS': [BASE_DIR / 'templates'],

        'APP_DIRS': True,

        'OPTIONS': {

            'context_processors': [

                'django.template.context_processors.request',

                'django.contrib.auth.context_processors.auth',

                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# ============================================================
# WSGI
# ============================================================

WSGI_APPLICATION = 'hair_saloon.wsgi.application'


# ============================================================
# DATABASE
# ============================================================

DATABASES = {

    'default': {

        'ENGINE': 'django.db.backends.sqlite3',

        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# ============================================================
# PASSWORD VALIDATION
# ============================================================

AUTH_PASSWORD_VALIDATORS = [

    {
        'NAME':
        'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },

    {
        'NAME':
        'django.contrib.auth.password_validation.MinimumLengthValidator',
    },

    {
        'NAME':
        'django.contrib.auth.password_validation.CommonPasswordValidator',
    },

    {
        'NAME':
        'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# ============================================================
# INTERNATIONALIZATION
# ============================================================

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True


# ============================================================
# STATIC FILES
# ============================================================

STATIC_URL = 'static/'


# ============================================================
# DEFAULT PRIMARY KEY
# ============================================================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# ============================================================
# EMAIL
# ============================================================

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'