from django.urls import path
from . import views

urlpatterns = [
    path("<int:quiz_id>/", views.Quiz.as_view(), name="quiz"),
    path("add_question/", views.AddQuestion.as_view(), name="add_question"),
    path("result/", views.Result.as_view(), name="result"),
    path("leaderboard/<int:quiz_id>/", views.Leaderboard.as_view(), name="leaderboard"),
    path("leaderboards/", views.Leaderboards.as_view(), name="leaderboards"),
    path("", views.Quiz_module.as_view(), name="module")

]
