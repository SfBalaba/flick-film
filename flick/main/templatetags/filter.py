def lookup(value, arg):
    return value[arg]

from django.template import Library

register = Library()
register.filter(name='lookup', filter_func=lookup)