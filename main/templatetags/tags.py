from django import template

from main.models import Category, Movie

register = template.Library()

@register.simple_tag()
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('main/tags/last_movies.html')
def get_last_movie(count = 5):
    movies = Movie.objects.order_by("id")[:count]
    return {"last_movies": movies}