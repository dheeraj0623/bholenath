from django import template
register=template.Library()

@register.filter(name='f8upper')

def first_eight_upper(value):
    '''This is my own filter'''
    result=value[:8].upper()
    return result

@register.filter(name='c_and_c')
def cut_and_concate(value,arg):
    result=value[:4]+str(arg)
    return result
