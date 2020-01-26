from .common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


#ローカルでの実行時
#① wsgi.py の whitenoise 関連のコードをコメントアウトする
#②　python manage.py runserver --settings vote_app.settings.dev　で実行する