import random
import string

from django.utils.text import slugify


def random_string_generator(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_payment_id_generator(instance):

    payment_new_id = random_string_generator()

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(payment_id=payment_new_id).exists()
    if qs_exists:
        return unique_slug_generator(instance)
    return payment_new_id


def unique_slug_generator(instance, new_slug=None):

    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
            slug=slug,
            randstr= random_string_generator(size=4)
        )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug

