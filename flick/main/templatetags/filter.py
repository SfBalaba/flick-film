def lookup(value, arg):
    return value[arg]

def get_prop(value, prop):
    return list(map(lambda x: x[prop], value))

def profession(value, arg):
    return list(filter(lambda x: x['profession'] == arg and 
                       (x['name'] is not None or x['enName'] is not None), value))

from django.template import Library

register = Library()
register.filter(name='lookup', filter_func=lookup)

register.filter(name='profession', filter_func=profession)
register.filter(name='get_prop', filter_func=get_prop)