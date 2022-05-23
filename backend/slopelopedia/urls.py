from django.urls import path
from . import views


urlpatterns = [
    path('all/',views.get_all_locations_list),
    path('', views.user_create_location),
    path('',views.get_all_comments_list),
    path('comment/', views.user_comment_detail),
    path('replies/', views.user_replies_detail),
    path('replies/<int:pk>/', views.replies_by_id)
    path('like-post'/<int:pk>)
]