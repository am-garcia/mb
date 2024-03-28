from django.urls import path
from posts import views

urlpatterns = [
    # path("", views.PostHomeView.as_view(), name="home"),
    # path("post/", views.PostAboutView.as_view(), name="about"),
    path("", views.PostListView.as_view(), name="list"),
    path("<int:pk>/", views.PostDetailView.as_view(), name="detail"),
    path("new/", views.PostCreateView.as_view(), name="new"),
] 