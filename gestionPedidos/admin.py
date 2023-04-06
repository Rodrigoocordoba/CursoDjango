from django.contrib import admin

from gestionPedidos.models import Clientes, Articulos, Pedidos #Importo clientes desde el models de gestionpedidos

# Register your models here.

class ClientesAdmin(admin.ModelAdmin): #en esta clase indicamos que campos pueden ver en el panel de administracion de la clase de clientes
    list_display=("nombre", "direccion", "tfno")
    search_fields=("nombre","direccion", "tfno")  #con esto podemos realizar busquedas por nombre y direccion


class ArticulosAdmin(admin.ModelAdmin):
    list_filter=("seccion",)

class PedidosAdmin(admin.ModelAdmin):
    list_display=("numero","fecha")  #con list display lo que hacemos es darle formato a como queremos ver las tablas en el admin
    list_filter=("fecha",) #se agrega la coma final porque es una tupla
    date_hierarchy="fecha"  #es un filtro que va arriba de la tabla por fechas puntuales



admin.site.register(Clientes, ClientesAdmin) #Con esto vamos a tener disponible la tabla de clientes desde el panel de administracion

admin.site.register(Articulos,ArticulosAdmin)

admin.site.register(Pedidos,PedidosAdmin)
