from django.contrib import admin
from django import forms

# Register your models here.
from .models import Vegetables, Tomato, Flowers, Perets, Baklajan, Kapusta, Svekla, Morkov, Redis, Cucumber,Comments

class Veg_typeInline(admin.StackedInline):
    model = Tomato
    raw_id_fields = ("t_id",)
class VegetablesAdmin(admin.ModelAdmin):
    search_fields = ['tomato__name']
class TomatoAdmin(admin.ModelAdmin):
    search_fields = ['name', 'tomato_color']
class PeretsAdmin(admin.ModelAdmin):
    pass
class BaklajanAdmin(admin.ModelAdmin):
    pass
class KapustaAdmin(admin.ModelAdmin):
    pass
class SveklaAdmin(admin.ModelAdmin):
    pass
class MorkovAdmin(admin.ModelAdmin):
    pass
class RedisAdmin(admin.ModelAdmin):
    pass
class CucumberAdmin(admin.ModelAdmin):
    pass
class CommentsAdmin(admin.ModelAdmin):
    list_filter = ['approved']

class FlowersAdmin(admin.ModelAdmin):
    exclude = ['class_image','veg_type','vid_image']
    list_filter = ['vids','lifetime']
    #pass

admin.site.register(Vegetables, VegetablesAdmin)
admin.site.register(Tomato, TomatoAdmin)
admin.site.register(Perets, PeretsAdmin)
admin.site.register(Baklajan, BaklajanAdmin)
admin.site.register(Kapusta, KapustaAdmin)
admin.site.register(Svekla, SveklaAdmin)
admin.site.register(Morkov, MorkovAdmin)
admin.site.register(Redis, RedisAdmin)
admin.site.register(Cucumber, CucumberAdmin)
admin.site.register(Comments, CommentsAdmin)

admin.site.register(Flowers, FlowersAdmin)

