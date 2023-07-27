from django.contrib import admin
from django.urls import include, path, re_path
from chat import consumers
from chat.consumer.drawboard_consumer import DrawboardConsumer
"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', include('chat.urls')),  # chat 앱의 URLconf를 포함
    path('accounts/', include('allauth.urls')),
    path('drawboard/',include('chat.urls')),
    path('ws/chat/<str:room_name>/', consumers.ChatConsumer.as_asgi()),
    path('ws/drawboard/<str:drawboard_id>/', DrawboardConsumer.as_asgi()),
]
