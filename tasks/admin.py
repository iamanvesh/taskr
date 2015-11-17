from django.contrib import admin

from .models import Entry, Keyword, Result


class EntryAdmin(admin.ModelAdmin):
    pass


class KeywordAdmin(admin.ModelAdmin):
    pass


class ResultAdmin(admin.ModelAdmin):
    pass


admin.site.register(Entry, EntryAdmin)
admin.site.register(Keyword, KeywordAdmin)
admin.site.register(Result, ResultAdmin)
