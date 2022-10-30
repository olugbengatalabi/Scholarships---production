from django.contrib import admin
from .models import *


class ApplicationAdmin(admin.ModelAdmin):
  list_display = ["date_submitted","user", "niche", "wallet_address", "application_text", "link1", "link2", "image", "suggestions", "status", "has_been_reviewed"]
  list_display_links = ["user"]
  list_editable = ["status"]
  list_filter = ["date_submitted", "niche", "status", 'has_been_reviewed']
# Register your models here.


admin.site.register(Application, ApplicationAdmin)
