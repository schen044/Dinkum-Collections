from django.contrib import admin
# import your models here
from .models import Fish, Museum

# Register your models here
admin.site.register(Fish)
admin.site.register(Museum)