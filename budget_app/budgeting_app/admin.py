from django.contrib import admin
from . models import *
# Register your models here.

admin.site.register(Project)
admin.site.register(Budget)
admin.site.register(Category)
admin.site.register(Planned)
admin.site.register(Cashflow)