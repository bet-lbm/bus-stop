from django.contrib import admin
from .models import Bus
from .models import Stop
from .models import Route

# Register your models here.

admin.site.register(Bus)
admin.site.register(Stop)
admin.site.register(Route)