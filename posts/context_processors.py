from .models import Post


def post_links(request):
    if str(request.user) != "AnonymousUser":
        try:
            slug = str(request)
            slug = slug[37:-2]
            print(slug)
            title = Post.objects.filter(community__slug=slug).values_list("title")
            list_title = []
            n =0
            for titulo in title:
                titulo = (titulo)
                titulo = title[n][0]
                list_title.append(titulo)
                n += 1
            print(list_title)
            content = Post.objects.filter(community__slug=slug).values_list("content")[0]
            content = str(content)
            content = content[2:-3]
            image = Post.objects.filter(community__slug=slug).values_list("miniature")[0]
            image = str(image)
            image = image[2:-3]

            return {"posts":{"title_post": list_title, "content_post": content, "image_post": image}}
        except:
            return {}
