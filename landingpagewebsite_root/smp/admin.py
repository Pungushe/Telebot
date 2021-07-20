from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import SmpSlider


class SmpAdmin(admin.ModelAdmin):
    list_display = ('smp_title', 'smp_text', 'smp_css', 'get_img')
    list_display_links = ('smp_title',)
    list_editable = ('smp_css',)
    fields = ('smp_title', 'smp_text', 'smp_css', 'smp_img', 'get_img')
    readonly_fields = ('get_img',)

    def get_img(self, obj):
        if obj.smp_img:
            return mark_safe(f'<img src="{obj.smp_img.url}" width="80px"')
        else:
            return 'Нет картинки'

    get_img.short_description = 'Миниатюра'


admin.site.register(SmpSlider, SmpAdmin)
