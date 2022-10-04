from django.contrib import admin

from .models import Maqola

class Maqola_Admin(admin.ModelAdmin):
    list_display = ['nomi','maqola_soni','sana']
    list_per_page = 10
    ordering = ('nomi','maqola_soni','sana')
    search_fields = ['nomi','maqola_soni','sana']
admin.site.register(Maqola, Maqola_Admin)