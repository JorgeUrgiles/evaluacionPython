from django.contrib import admin
from .models import Social

# Register your models here. metodos de clase siemore con self
class SocialAdmin(admin.ModelAdmin):
   #readonly_fields=('created','updated')
    #configuracion para grupo de personas
    def get_readonly_fields(self,request,object=None):
        if request.user.groups.filter(name='Personal').exists():
            return ('created','updated','key','name')
        else:
            return ('created','updated')


admin.site.register(Social,SocialAdmin)