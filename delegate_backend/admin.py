from django.contrib import admin

from.models import Item, User, Group, Event, List
# Register your models here.
admin.site.register(Item)
admin.site.register(User)
admin.site.register(Group)
admin.site.register(Event)
admin.site.register(List)