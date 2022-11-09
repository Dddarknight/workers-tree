import os
from pathlib import Path
from dotenv import load_dotenv


load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "bootstrap4",
    'django_seed',
    'django_tables2',
    'django_filters',
    'crispy_forms',
    'crispy_bootstrap5',
    'django_htmx',
    'debug_toolbar',
    'workers_tree',
    'workers_tree.users',
    'workers_tree.employees',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'workers_tree.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
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

WSGI_APPLICATION = 'workers_tree.wsgi.application'

DATABASE_URL = 'postgresql://<postgresql>'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB', 'postgres'),
        'USER': os.getenv('POSTGRES_USER', 'postgres'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', 'password'),
        'HOST': os.getenv('POSTGRES_HOST', 'localhost'),
        'PORT': os.getenv('POSTGRES_PORT', '5432'),
    },
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

BOOTSTRAP4 = {
    "css_url": {
        "href": "https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/"
                "dist/css/bootstrap.min.css",
        "integrity": "sha384-zCbKRCUGaJDkqS1kPbPd7TveP5iyJE0Ej"
                     "AuZQTgFLD2ylzuqKfdKlfG/eSrtxUkn",
        "crossorigin": "anonymous",
    },

    "javascript_url": {
        "url": "https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/"
               "dist/js/bootstrap.bundle.min.js",
        "integrity": "sha384-fQybjgWLrvvRgtW6bFlB7jaZrFsaBXjs"
                     "OMm/tB9LTS58ONXgqbR9W8oWht/amnpF",
        "crossorigin": "anonymous",
    },

    "jquery_url": {
        "url": "https://code.jquery.com/jquery-3.5.1.min.js",
        "integrity": "sha384-ZvpUoO/+PpLXR1lu4jmpXWu80pZlYUAfxl5NsBMWOEPSjUn/"
                     "6Z/hRTt8+pR6L4N2",
        "crossorigin": "anonymous",
    },

    "jquery_slim_url": {
        "url": "https://code.jquery.com/jquery-3.5.1.slim.min.js",
        "integrity": "sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+Ibb"
                     "VYUew+OrCXaRkfj",
        "crossorigin": "anonymous",
    },

    'javascript_in_head': False,

    'include_jquery': False,

    'horizontal_label_class': 'col-md-3',

    'horizontal_field_class': 'col-md-9',

    'set_placeholder': True,

    'required_css_class': '',

    'error_css_class': 'is-invalid',

    'success_css_class': 'is-valid',

    'formset_renderers': {
        'default': 'bootstrap4.renderers.FormsetRenderer',
    },
    'form_renderers': {
        'default': 'bootstrap4.renderers.FormRenderer',
    },
    'field_renderers': {
        'default': 'bootstrap4.renderers.FieldRenderer',
        'inline': 'bootstrap4.renderers.InlineFieldRenderer',
    },
}

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"
CRISPY_TEMPLATE_PACK = "bootstrap4"

# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATIC_URL = '/static/'

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

AUTH_USER_MODEL = 'users.EmployeeUser'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

LOGIN_REDIRECT_URL = '/'
LOGIN_URL = 'users/login'
LOGOUT_REDIRECT_URL = '/'
