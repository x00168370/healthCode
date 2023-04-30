from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from .models import *

# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'age','gender','height','goal_weight', 'current_weight', 'weight_goal']

class mealAdmin(admin.ModelAdmin):
    class Meta:
        model = Meal
        list_display = "__all__"
        list_filter = ['name']


admin.site.register(Exercise)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Meal, mealAdmin)



