from .common import  *




DEBUG = True

SECRET_KEY = 'django-insecure-^wua5vaqu9+$lwual#_!cqlx75qc1vaibq(153fx@1u0f8hgd6'



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'track_activities',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'macquena'

    }
}
