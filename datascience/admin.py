from django.contrib import admin
from .models import Registration, UserData, DiabeteDataModel, Messages
# Register your models here.
admin.site.register(Registration)
admin.site.register(UserData)
admin.site.register(DiabeteDataModel)
admin.site.register(Messages)