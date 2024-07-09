from django.contrib import admin
from .models import AthleteData, MealData

# Register your models here.

class AthleteDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'age', 'height', 'weight', 'duration','heart_rate', 'body_temp', 'prediction')
admin.site.register(AthleteData, AthleteDataAdmin)


class MealDataAdmin(admin.ModelAdmin):
    list_display = ('meal_name', 'img_url', 'carbohydrates', 'fat', 'protein', 'Calories')
admin.site.register(MealData, MealDataAdmin)