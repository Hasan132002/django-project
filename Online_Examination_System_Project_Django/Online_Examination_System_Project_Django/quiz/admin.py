from django.contrib import admin

from .models import Result
from .models import Set


class SetModelAdmin(admin.ModelAdmin):
    list_display = ['set_no', 'exam_name']


admin.site.register(Set, SetModelAdmin)
admin.site.register(Result)
