from django.contrib import admin

# Register your models here.

from .models import World, Category, CategoryRooms, Topic, TopicRooms, RoomsProjects, TopicImage

admin.site.register(World)
admin.site.register(Category)
admin.site.register(CategoryRooms)
admin.site.register(Topic)
admin.site.register(TopicRooms)
admin.site.register(RoomsProjects)
admin.site.register(TopicImage)
