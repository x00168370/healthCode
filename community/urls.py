
from django.contrib import admin
from django.urls import path
from .views import *



app_name = "community"
 
urlpatterns = [

    path('admin/', admin.site.urls),

    path('new/', CommunityCreateView.as_view(),name="community"),
    path('community_list', CommunityListView.as_view(), name="community_list"),


    path("<int:pk>/", CommunityDetailView.as_view(),name="community_detail"),
    path("<int:pk>/edit/", CommunityUpdateView.as_view(), name="community_edit"),
    path("<int:pk>/delete/", CommunityDeleteView.as_view(), name="community_delete"),
    

    path('like/<int:pk>', CommunityLike, name="community_like"),

]

