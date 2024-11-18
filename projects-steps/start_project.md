
# TO START PROJECT 
> check the settings to select a DB sqlite

- try python manage.py (you might have the required file if you are a django dev before) or
- pip install -r requirements.txt


# Instructions

- in the settings.py file you want to make sure you have this settings

```python

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# for postgres offline
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'hotel_storage',
#         'USER': 'postgres',
#         'PASSWORD': os.environ.get('book hall postgres PASSWORD'),
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }


```

- To create migrations : ` python manage.py makemigration ` 

- To create database table after migrations : ` python manage.py migrate `

- To create superuser (a user that has all permission and can login to admin site) : ` python manage.py createsuper user `

- To see the table on the admin site go to:
` localhost/admin/ `

> Note check seed.sql before you run this command

- to populate db table room and categories run :  ` python manage.py populate_cat_room `

> Note check seed_reserve.sql before you run this command

- to populate db table booking and customer run : ` python manage.py populate_cust_booking `
