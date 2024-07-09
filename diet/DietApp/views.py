from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import login, logout, authenticate
from .models import AthleteData, MealData
from .forms import AthleteForm, UserCreationForm
import fontawesome as fa

# other imports
import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from django_daraja.mpesa.core import MpesaClient
# Create your views here.


@login_required(login_url='DietApp:login')
def main(request):
    template = loader.get_template("DietApp/main.html")
    return HttpResponse(template.render())



@login_required(login_url='DietApp:login')
def predict(request):
    if request.method == 'POST':
        form = AthleteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('DietApp:recommended_meal')
    else:
        form = AthleteForm()
    template = loader.get_template("DietApp/index.html")
    context = { 
        'form': form,
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url='DietApp:login')
def viewpredictions(request):
    all_predictions = AthleteData.objects.order_by('-date')
    template =  loader.get_template("DietApp/predictions.html")
    context = {
        "all_predictions": all_predictions
    }
    
    return HttpResponse(template.render(context, request))



@login_required(login_url='DietApp:login')
def view_meals(request):
    all_meals = MealData.objects.all()
    template = loader.get_template("DietApp/meals.html")
    context = {
        'all_meals': all_meals
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url='DietApp:login')
def recommended_meal(request):
    # Retrieve the latest predicted calories
    latest_calories = AthleteData.objects.order_by('-date').first()
    
    if latest_calories:
        predicted_calories = latest_calories.prediction
        meal_list = MealData.objects.all()

        # Initialize variables to keep track of the closest meal and the minimum difference
        closest_meal = None
        min_difference = float('inf')  # Initialize to positive infinity

        # Iterate through each meal in the list
        for meal in meal_list:
            # Extract meal details
            meal_name = meal.meal_name
            meal_calories = meal.Calories

            # Calculate the absolute difference between recommended and actual calories
            difference = abs(predicted_calories - meal_calories)

            # Check if the current meal has a smaller difference
            if difference < min_difference:
                min_difference = difference
                closest_meal = meal

        context = {
            'closest_meal': closest_meal,
            'predicted_calories': predicted_calories
        }
        template = loader.get_template("DietApp/meal.html")

        return HttpResponse(template.render(context, request))
    else:
        # Handle the case where there are no predicted calories
        return HttpResponse("No predicted calories available.")
    

def logoutUser(request):
    logout(request)
    return redirect("DietApp:main")

@login_required(login_url='DietApp:login')
def about(request):
    template = loader.get_template("DietApp/about.html")
    return HttpResponse(template.render())


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST['next'])
            return redirect('DietApp:main')
        else:
            context = {
                'errors': "User does not exist",
            }
            return render(request, 'DietApp/login.html', context)
    return render(request, 'DietApp/login.html')


def register(request):
    form = UserCreationForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = form.save(commit=False)
            if user is not None:
                User.objects.create_user(username=username, email=email, password=password)
                user = authenticate(username=username, password=password)
                login(request, user)
                return redirect('DietApp:main')
    return render(request, 'DietApp/register.html', {'form': form})

def getUser(request):
    user = User.objects.all()
    context = {
        'user': user,
    }
    return render(request, 'DietApp/partials/nav.html', context)
    

