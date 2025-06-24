from django.urls import reverse
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import json
from django.views.decorators.csrf import csrf_exempt


from .models import *

# Create your views here.
def index(request):
    return render(request, "fitness/index.html")

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "fitness/login.html", {
                "error": "Invalid username and/or password."
            })
        
    return render(request, "fitness/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "fitness/register.html", {
                "error": "Passwords must match."
            })


        # Attempt to create new user
        try:
            user = User.objects.create_user(username=username, password=password)
        except IntegrityError:
            return render(request, "fitness/register.html", {
                "error": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "fitness/register.html")

@login_required
def gym(request):
    return render(request, "fitness/gym.html")

def macros(request):
    return render(request, "fitness/meal_macros.html")

def counter(request):
    if request.method == 'POST':
        # Get form inputs and handle missing data
        try:
            height    = float(request.POST.get('height', 0))
            weight    = float(request.POST.get('weight', 0))
            age       = float(request.POST.get('age', 0))
            gender    = request.POST.get('gender', 'male')
            intensity = request.POST.get('intensity', 'light')
            goal_choice = request.POST.get('goal', 'maintain')

            if height <= 0 or weight <= 0 or age <= 0:
                raise ValueError("Please enter valid positive values for height, weight, and age.")

            # Calculate BMR based on gender
            if gender == 'male':
                bmr = 10 * weight + 6.25 * height - 5 * age + 5
            else:
                bmr = 10 * weight + 6.25 * height - 5 * age - 161

            # Factor based on activity intensity
            factors = {
                'light':    1.375,
                'moderate': 1.55,
                'vigorous': 1.725
            }
            tdee = bmr * factors.get(intensity, 1.375)  # Default to 'light' if intensity is missing

            # Adjust TDEE based on the goal
            if goal_choice == 'lose':
                targeted_cals = tdee - 500
            elif goal_choice == 'gain':
                targeted_cals = tdee + 500

            # Macronutrient ratios based on the goal
            goals = {
                "maintain": {"p": 0.30, "c": 0.45, "f": 0.25},
                "lose":     {"p": 0.40, "c": 0.30, "f": 0.30},
                "gain":     {"p": 0.25, "c": 0.55, "f": 0.20},
            }

            # Default to "maintain" if the goal is not valid
            ratios = goals.get(goal_choice, goals["maintain"])

            # Calculate macros (protein, carbs, fat)
            protein = (targeted_cals * ratios['p']) / 4
            carbs   = (targeted_cals * ratios['c']) / 4
            fat     = (targeted_cals * ratios['f']) / 9

            return render(request, 'fitness/count_calories.html', {
                'calories': round(tdee, 0),
                'protein':  round(protein, 0),
                'carbs':    round(carbs, 0),
                'fat':      round(fat, 0),
                'goal':     goal_choice,
                'targeted_cals': round(targeted_cals)
            })

        except ValueError as e:
            return render(request, 'fitness/count_calories.html', {
                'error': str(e)
            })

    # If GET request, return empty form
    return render(request, 'fitness/count_calories.html')

def exercises(request):
    return render(request, 'fitness/exercises.html')

@login_required
def my_workout(request):
    return render(request, 'fitness/my_workout.html')

@login_required
def saved(request):
    if request.method == 'GET':
        user = request.user
        saved_exercises = SavedExercise.objects.filter(user=user).values_list('exercise_id', flat=True)
        return JsonResponse(list(saved_exercises), safe=False)
    
@login_required
def toggle_save_exercise(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user = request.user
        exercise_id = data['id']
        saved = data['saved']
        if saved:
            SavedExercise.objects.get_or_create(user=user, exercise_id=exercise_id)
        else:
            SavedExercise.objects.filter(user=user, exercise_id=exercise_id).delete()
        return JsonResponse({'status': 'success'})
    
@login_required
def saved_page_view(request):
    return render(request, 'fitness/saved.html')

