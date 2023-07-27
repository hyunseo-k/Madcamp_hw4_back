from django.urls import path, re_path
from . import views
from .consumer.drawboard_consumer import DrawboardConsumer


urlpatterns = [
    path('test/', views.test, name='test'),
    path('register/', views.register_view, name='register_view'),
    path('user/idcheck/', views.user_idcheck, name='user_idcheck'),
    path('user/', views.login_view, name='login_view'),
    path('profile/', views.profile, name='profile'),
    path('api/user-profile/', views.UserProfileAPIView.as_view(), name='user-profile-api'),
    path('friend-list/', views.FriendListAPIView.as_view(), name='friend-list'),
    path("", views.index, name="index"),
    path("draw/<str:drawboard_id>/", views.drawboard, name="drawboard"),
    path("<str:room_name>/", views.room, name="room"),
]
