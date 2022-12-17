from django.contrib import admin

# Register your models here.
from file.models import File

# admin.site.register(Catalog)
admin.site.register(File)

admin.site.site_header = 'Administration'
admin.site.index_title = 'Panel'
admin.site.site_title = 'Files'
