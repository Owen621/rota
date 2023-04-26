from django import template
register = template.Library()

@register.simple_tag
def tagsave(x, days):
    x.SaveShifts(days)
    return ""
