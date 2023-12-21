from django.urls import path
from . import views
from . views import IndexView, AddView
app_name = "polls"

urlpatterns = [
    path("", IndexView, name="index"),
    path("add", AddView, name="add"),

    # path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    # path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    # path("<int:question_id>/vote/", views.vote, name="vote"),
]