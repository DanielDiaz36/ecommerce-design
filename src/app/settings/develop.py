import os


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'x&e=@be22im-$)*zrh)$n#=2y+ph+(f20+9x6evt^+xu-6@5*8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: update this when you have the production host
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'testingmylandingpage_ecommerce',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}