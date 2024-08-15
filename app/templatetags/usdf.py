from django import template

register=template.Library()

@register.filter()
def swapping(value):
    return value.swapcase()

def count(value,sch):
    return value.lower().count(sch.lower())

def upper(value):
    return value.upper()




register.filter('count',count)
register.filter('upper',upper)

@register.filter()
def replace(value,rech):
    return value.replace(rech,' ')