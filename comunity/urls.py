from django.urls import path
from comunity.views import CommunityList, CommunityDetail, CommunityCreateView

app_name = "community"

urlpatterns = [
    path('home/', CommunityList.as_view(), name='index'),
    path('comunidad/detail/<str:slug>', CommunityDetail.as_view(), name='comunidad_detail'),
    path('comunidad/crear', CommunityCreateView.as_view(), name='comunidad_crear'),
]
