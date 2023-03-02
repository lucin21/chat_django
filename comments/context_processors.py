from .models import Comment
from users.models import User


def comment_links(request):
    if str(request.user) != "AnonymousUser":
        content = Comment.objects.filter(user=request.user).values_list("content")[0]
        content = str(content)
        content = content[2:-3]
        created_at = Comment.objects.filter(user=request.user).values_list("created_at")[0]
        # created_at = str(created_at)
        # created_at = created_at[2:-3]
        user = Comment.objects.filter(user=request.user).values_list("user")[0][0]
        user = User.objects.get(id=user)
        user = str(user)
        # user = user[2:-3]

        return {"content_comment": content, "created_at_comment":created_at, "user_comment":user}
    return {}