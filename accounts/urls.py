from django.urls import path

from accounts.views import AdminSignUpView,StudentSignUpView,TrainerSignUpView

urlpatterns = [
    path("admin-register/",AdminSignUpView.as_view()),
    path("student-register/",StudentSignUpView.as_view()),
    path("trainer-register/",TrainerSignUpView.as_view()),
]