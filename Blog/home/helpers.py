from django.utils.text import slugify
import string
import random


def generate_random_string(N):
    return ''.join(random.choices(string.ascii_uppercase+string.digits, k=N))


def generate_slug(text):
    from . models import BlogModel
    new_slug  = slugify(text)
    if BlogModel.objects.filter(slug = new_slug).exists():
        return generate_slug(text+"-"+generate_random_string(5))
    return new_slug
    