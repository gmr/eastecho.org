"""
Django settings for eastecho project.

"""
import os
import pathlib

DEBUG = os.environ.get('DEV', 'TRUE') == 'TRUE'

BASE_DIR = pathlib.Path(__file__).parent if DEBUG else pathlib.Path(
    '/opt/eastecho')

SECRET_KEY = os.environ.get('SECRET_KEY', 'secret_key')

SITE_PASSWORD = 'patriot'

ALLOWED_HOSTS = [
    'eastecho.org', 'www.eastecho.org', 'localhost', '127.0.0.1', '[::1]'
]

INSTALLED_APPS = [
    'eastecho.site.apps.SiteConfig', 'django.contrib.admin',
    'django.contrib.auth', 'django.contrib.contenttypes',
    'django.contrib.sessions', 'django.contrib.messages',
    'django.contrib.staticfiles', 'ckeditor', 'sorl.thumbnail',
    'django_instagram'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'eastecho.site.middleware.AuthCookieMiddleware'
]

ROOT_URLCONF = 'eastecho.urls'

TEMPLATES = [
    {
        'BACKEND':
        'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            str(BASE_DIR / 'site/templates') if DEBUG else str(BASE_DIR /
                                                               'templates')
        ],
        'APP_DIRS':
        True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'eastecho.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': str(BASE_DIR.parent / 'db.sqlite3'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'postgres',
            'USER': 'postgres',
            'HOST': 'postgres',
            'PORT': 5432,
        }
    }

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':
        'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  # noqa: E501
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

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/New_York'
USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = BASE_DIR / 'site/media' if DEBUG else BASE_DIR / 'media'
MEDIA_URL = '/media/'

STATIC_ROOT = BASE_DIR / 'site/static' if DEBUG else BASE_DIR / 'static'
STATIC_URL = '/static/'

if DEBUG:
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
            'LOCATION': '/var/tmp/django_cache',
        }
    }
else:
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'LOCATION': 'memcached:11211',
        }
    }

CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar_CustomConfig': [{
            'name':
            'basicstyles',
            'items': [
                'Bold', 'Italic', 'Underline', 'Strike', 'Subscript',
                'Superscript', '-', 'RemoveFormat'
            ]
        }, {
            'name':
            'paragraph',
            'items': [
                'NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-',
                'Blockquote', '-', 'JustifyLeft', 'JustifyCenter',
                'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl'
            ]
        }, {
            'name': 'links',
            'items': ['Link', 'Unlink', 'Anchor']
        }, {
            'name':
            'insert',
            'items':
            ['Image', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar']
        }, {
            'name': 'colors',
            'items': [
                'TextColor',
            ]
        }],
        'toolbar':
        'CustomConfig'
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format':
            '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'filters': {},
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
        },
        'django.request': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        'eastecho': {
            'handlers': ['console'],
            'level': 'INFO'
        }
    }
}

if not DEBUG:
    USE_X_FORWARDED_HOST = True
    USE_X_FORWARDED_PORT = True
