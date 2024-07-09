from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from sklearn.tree import DecisionTreeClassifier
import joblib
import pickle


# Create your models here.

GENDER = (
    (0, 'Female'),
    (1, 'Male'),
)


class AthleteData(models.Model):
    name = models.CharField(max_length=255)
    gender = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)], choices=GENDER, default=1)
    age = models.PositiveIntegerField(validators=[MinValueValidator(18), MaxValueValidator(40)],null=True, default=1)
    height = models.FloatField(null=True)
    weight = models.FloatField(null=True)
    duration = models.FloatField(null=True)
    heart_rate = models.FloatField(null=True)
    body_temp = models.FloatField(null=True)
    prediction = models.FloatField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
    
    
    def save(self, *args, **kwargs):
        with open('ml_model/LinearRegression_model.pkl', 'rb') as file:
            model = pickle.load(file)
            predict_calories = model.predict(
            [[self.gender, self.age, self.height, self.weight, self.duration,
              self.heart_rate, self.body_temp]])
            self.prediction = abs(round(predict_calories[0]))
        return super().save(*args, **kwargs)
    class Meta:
        ordering = ['-date']
    def __str__(self):
        return self.name
    
    
    
    
class MealData(models.Model):
    meal_name = models.CharField(max_length=255)
    img_url = models.CharField(max_length=255)
    carbohydrates = models.PositiveIntegerField()
    fat = models.PositiveIntegerField()
    protein = models.PositiveIntegerField()
    Calories = models.FloatField()
    
    def __str__(self):
        return self.meal_name
    
