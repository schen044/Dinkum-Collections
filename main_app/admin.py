from django.contrib import admin
# import your models here
from .models import Fish, User, Licence

# Register your models here
admin.site.register(Fish)
admin.site.register(User)
admin.site.register(Licence)