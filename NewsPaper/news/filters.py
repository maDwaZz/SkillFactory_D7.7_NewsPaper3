from django_filters import FilterSet, CharFilter, ModelChoiceFilter
from django.contrib.auth.models import User
from .models import Post


class PostFilter(FilterSet):
    author = ModelChoiceFilter(
        field_name='author__user__username',
        queryset=User.objects.all(),
    )

    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
            'creation_time': ['gt']
        }
