from django.urls import path
from posts.views import PostByCommunity, PostCreateView
app_name ="post"

urlpatterns = [
    path('comunidades/<shorname>/', PostByCommunity.as_view(), name='post_comunidad'),
    path('post/crear/', PostCreateView.as_view(), name='crer_post'),

]
