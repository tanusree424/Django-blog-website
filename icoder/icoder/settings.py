"""
Django settings for icoder project.

Generated by 'django-admin startproject' using Django 5.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os
from django.contrib.messages import constants as messages

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-kcy2k@u-!sq0dn-6*p)190ofx-4gs2=y=(awi-n%bxzscko4h&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    'home',
    'django.contrib.humanize',
    'tinymce',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'icoder.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join('templates')],
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

WSGI_APPLICATION = 'icoder.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_DIRS = [os.path.join(BASE_DIR /'static')]
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MESSAGE_TAGS = {
   messages.ERROR:"danger"

}
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field
TINYMCE_DEFAULT_CONFIG = {
    "height": 500,
    "width": 800,
    "menubar": "file edit view insert format tools table help",
    "plugins": (
        "advlist autolink lists link image charmap print preview anchor "
        "searchreplace visualblocks code fullscreen insertdatetime media table paste "
        "code help wordcount"
    ),
    "toolbar": (
        "undo redo | formatselect | bold italic underline strikethrough | "
        "forecolor backcolor | alignleft aligncenter alignright alignjustify | "
        "bullist numlist outdent indent | paragraph | link image media | "
        "code preview | fullscreen"
    ),
    "image_advtab": True,  # Enables the 'Advanced' tab for images
    "automatic_uploads": True,
    "file_picker_types": "image",
    "images_upload_url": "/upload/",  # URL for image upload endpoint
       "style_formats": [
        {"title": "Paragraph", "format": "p"},
        {"title": "Heading 1", "format": "h1"},
        {"title": "Heading 2", "format": "h2"},
        {"title": "Heading 3", "format": "h3"},
        {"title": "Heading 4", "format": "h4"},
        {"title": "Heading 5", "format": "h5"},
        {"title": "Heading 6", "format": "h6"},
    ],
    "font_formats": "Arial=arial,helvetica,sans-serif; Times New Roman=times new roman,times; Verdana=verdana,geneva; Courier New=courier new,courier",
    "fontsize_formats": "8pt 10pt 12pt 14pt 18pt 24pt 36pt",
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
