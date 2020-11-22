from django.contrib import admin

# Register your models here.
from tutorial.quickstart.models import Bond, Lei


class LeiAdmin(admin.ModelAdmin):
    list_display = ("lei", "legal_name",)
    
class BondAdmin(admin.ModelAdmin):
    list_display = ("user", "isin", "size", "currency", "maturity", 'lei')


admin.site.register(Bond, BondAdmin)
admin.site.register(Lei, LeiAdmin)
