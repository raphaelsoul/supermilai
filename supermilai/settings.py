"""
Django settings for supermilai project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
#from sae.const import MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASS, MYSQL_DB

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'k5s_4fd4&cdp#s9u54=uso!f73sc&*#=i6+i-!!z5$b^t6e*om'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    #'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'account',
    'autotemplate',
    'logistik',
    'listcheck',
    'workflow',
)


TEMPLATE_CONTEXT_PROCESSORS=(
    'django.core.context_processors.request',
    #'django.core.context_processors.auth', #for version before django1.4
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
)


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'supermilai.urls'

WSGI_APPLICATION = 'supermilai.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

if 'SERVER_SOFTWARE' in os.environ:
    from sae.const import MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASS, MYSQL_DB
else:
    MYSQL_HOST = 'localhost'
    MYSQL_PORT = '3306'
    MYSQL_USER = 'root'
    MYSQL_PASS = '123456'
    MYSQL_DB   = 'app_supermilai'

DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),

        #'ENGINE': 'django.db.backends.mysql',
        #'NAME': 'supermilai',
        #'USER': 'root',
        #'PASSWORD': '123456',
        #'POST': '',
        #'PORT': '',

        'ENGINE': 'django.db.backends.mysql',
        'NAME': MYSQL_DB,
        'USER': MYSQL_USER,
        'PASSWORD': MYSQL_PASS,
        'HOST': MYSQL_HOST,
        'PORT': MYSQL_PORT,

    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'zh-cn'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

#ASSETS

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(os.path.dirname(__file__), 'static')

STATICFILES_DIRS = ('static',)

#MEDIA

MEDIA_URL  = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, "media")

MEDIA_DIRS = ('media',)

#TEMPLATES

#TEMPLATE_DIRS = (os.path.join(BASE_DIR, "templates"),)

TEMPLATE_DIRS = [os.path.join(BASE_DIR, "templates")]

LOGIN_URL = '/account/login.html'

SESSION_COOKIE_AGE = 60*60*4

AUTH_USER_MODEL = 'account.UserProfile'