from django.urls import path
from . import views


urlpatterns = [
    path('all/',views.get_all_locations_list),
    path('', views.user_create_location),
    path('allcomments/',views.get_all_comments_list),
    path('comment/', views.user_comment_detail),
    path('commentbylocation/<int:location>/', views.comment_by_location_id),
    path('replies/', views.user_replies_detail),
    path('replies/<int:comment_id>/', views.replies_by_comment_id),
    # path('like-comment/<int:pk>/', views.user_likes_location),
    # path('dislike-comment/<int:pk>/', views.user_dislikes_location),

]