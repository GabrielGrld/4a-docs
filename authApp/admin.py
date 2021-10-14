from django.contrib import admin
from .models.factura import Factura
from .models.pqr import Pqr
from .models.usuario import User
from .models.producto import Producto

admin.site.register (Factura)
admin.site.register (Pqr)
admin.site.register (Producto)
admin.site.register (User)


# Register your models here.
