from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login', views.login_view, name="login"),
    path('register', views.register, name="register"),
    path('logout', views.logout_view, name="logout"),
    path('gym', views.gym, name="gym"),
    path('macros', views.macros, name="macros"),
    path('count_calories', views.counter, name="counter"),
    path('exercises/', views.exercises, name='exercises'),
    path('my-workout', views.my_workout, name="my_workout"),
    path('saved/', views.saved, name='saved'),
    path('api/toggle_save/', views.toggle_save_exercise, name='toggle_save_exercise'),
    path('saved-page/', views.saved_page_view, name='saved_page'),

]
