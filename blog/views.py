from django.utils import timezone
from .models import Post
from django.views import generic


class Index(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'lista'

    def get_queryset(self):
        return Post.objects.filter(
            published_date__lte=timezone.now()
        ).order_by('-created_date')[:5]


class Detalhes(generic.DetailView):
    model = Post
    template_name = 'blog/detalhes.html'
