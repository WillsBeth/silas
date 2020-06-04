from django.contrib import admin

from . models import Agent
# Register your models here.


class agentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'hire_date')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 3


admin.site.register(Agent, agentAdmin)
