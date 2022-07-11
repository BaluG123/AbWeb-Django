from django.contrib import admin
from . models import Sports,Entertainment,Technology,EditorChoice

# Register your models here.
class SportsAdmin(admin.ModelAdmin):
    list_display=['id','title','image','body']
    list_filter=['title']
    search_fields=['title','body']

class EntertainmentAdmin(admin.ModelAdmin):
    list_display=['id','title','image','body']
    list_filter=['title']
    search_fields=['title','body']

class TechnologyAdmin(admin.ModelAdmin):
    list_display=['id','title','image','body']
    list_filter=['title']
    search_fields=['title','body']   

class EditorChoiceAdmin(admin.ModelAdmin):
    list_display=['id','title','image','body']
    list_filter=['title']
    search_fields=['title','body']  

admin.site.register(Sports,SportsAdmin)
admin.site.register(Entertainment,EntertainmentAdmin) 
admin.site.register(Technology,TechnologyAdmin)
admin.site.register(EditorChoice,EditorChoiceAdmin)          

