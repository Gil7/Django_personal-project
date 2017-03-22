import random
import string


def shortcode_generator(size=6,chars = string.ascii_lowercase + string.digits):
    return "".join(random.choice(chars) for _ in range(size))

def create_shortcode(instance,size=6):
    new_code = shortcode_generator(size=6)
    print(instance)
    print(instance.__class__)
    print(instance.__class__.__name__)
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(shortcode = new_code).exists()
    if qs_exists:
        return create_shortcode(instance,size=6)
    return new_code 
