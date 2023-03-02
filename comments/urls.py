from django.urls import path
from comments.views import CommentsByPost, CommentCreateView
app_name ="comment"

urlpatterns = [
    path('comments/<shorname>/', CommentsByPost.as_view(), name='comentarios'),
    path('comment/crear/', CommentCreateView.as_view(), name='crear_comentario'),

]