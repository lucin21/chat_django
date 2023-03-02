from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('admin/', admin.site.urls),

    path('', include('core.urls')),
    path('', include('users.urls')),
    path('', include('comunity.urls')),
    path('', include('posts.urls')),
    path('', include('comments.urls')),

    path('login/', auth_views.LoginView.as_view(), name='login'),
     
    path('logout/', auth_views.LogoutView.as_view(), {'next_page': '/'},
         name='logout')


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
