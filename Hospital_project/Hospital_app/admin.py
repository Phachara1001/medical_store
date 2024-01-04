from django.contrib import admin
from .models import * #เอามาหมดทุก Class

# Register your models here.
admin.site.register(d_type)
admin.site.register(drug)
admin.site.register(userbuy)
admin.site.register(report_buy)
