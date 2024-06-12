from django.contrib import admin
from recommender.models import Food
from recommender.models import UserList
# from recommender.models import User
# Register your models here.
admin.site.register(Food)
admin.site.register(UserList)
# admin.site.register(User)