# FitPath: Gym and Nutrition Assistant

## Overview

FitPath is a comprehensive web application developed using Django that helps users manage their fitness journey. It provides tools to calculate daily caloric needs (TDEE), analyze the nutritional value of meals, explore and search for exercises based on muscle groups, and build personalized workout plans. The application also includes user authentication to ensure a personalized and secure experience.

## Distinctiveness and Complexity

FitPath stands out from other course projects due to its integration of multiple complex features across domains such as health, nutrition, and exercise planning. Unlike simpler to-do lists or blog engines, this project involves:

* **TDEE (Total Daily Energy Expenditure) Calculation**: Users can input their physical information and activity level to calculate how many calories they should consume daily. This involves understanding and applying formulas from exercise science.

* **Nutritional Analysis**: The app connects to an external API to fetch nutritional data based on food input, then calculates values per given gram input. This involves handling asynchronous API calls, parsing JSON responses, and integrating with frontend JS validation.

* **Exercise Management**: Users can explore exercises by target muscle group, search by name, and archive exercises to a personalized workout plan. This adds data modeling complexity as well as interface considerations to keep the experience smooth.

* **Workout Planner**: The archiving and day assignment features allow users to assign exercises to specific days, view them later under "My Workout," and build structured fitness routines.

* **Authentication and Personalization**: Each user's inputs, plans, and history are securely managed, making this a personalized fitness companion.

Together, these features form a cohesive, full-stack application that provides a real-world utility with a complex and diverse codebase.

## File Descriptions

* **fitness/**: The main Django app directory, containing all backend logic:

  * `models.py`: Defines the data models for Users, Exercises, Meals, and Archived Workouts.
  * `views.py`: Handles view logic including TDEE calculation, food API integration, and workout planning.
  * `urls.py`: Maps routes to views.
  * `templates/fitness/`: Contains all HTML templates including the homepage, login/register, TDEE calculator, meal analyzer, and exercise planner.
  * `static/styles/`: Contains CSS files for styling.

* **project/**: The Django project settings and WSGI entry point.

  * `settings.py`, `urls.py`, `wsgi.py`: Standard Django configuration files.

* **db.sqlite3**: The SQLite database containing stored user data, workouts, and archived items.

* **README.md**: This documentation file.

## Running the Application

1. **Clone the Repository**

   ```bash
   git clone https://github.com/me50/theg0-0done.git
   cd project
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install Requirements**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations**

   ```bash
   python manage.py migrate
   ```

5. **Run the Server**

   ```bash
   python manage.py runserver
   ```

6. **Access the App**
   Navigate to `http://127.0.0.1:8000/` in your browser.

## Additional Information

* The app uses a food nutrition API (e.g., Calorieninjas or similar) to get real-time macro data.
* JavaScript is used extensively on the frontend to validate inputs and dynamically display results.
* Render.com is used for live deployment, requiring a `Procfile` and `requirements.txt`.
* Bootstrap and custom CSS provide a clean and responsive design.

The Fitenss app aims to help users plan their fitness journey effectively by combining scientific calculations with modern web technologies in a user-friendly interface.
