from django.urls import path
from rest_framework.routers import DefaultRouter

from core import views

router = DefaultRouter()
router.register("posts", views.PostViewSet, basename="posts")
router.register("comments", views.CommentViewSet, basename="comments")

urlpatterns = [path("upvote_post/<int:pk>/", views.UpvotePostView.as_view())]

urlpatterns += router.urls
