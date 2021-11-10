from django.contrib import admin
from .models import newProduct, user, usercontact
# Register your models here.


class useredit(admin.ModelAdmin):
    list_display = ["name", "username", "email", "password"]
    list_editable = ["username"]
    search_fields = ["name"]

class userscontact(admin.ModelAdmin):
    list_display = ["name", "email", "msn"]
    search_fields = ["nom"]

class adminproducts(admin.ModelAdmin):
    list_display = ["name", "type", "gender", "size", "brand", "price", "img"]
    search_fields = ["brand"]


admin.site.register(user, useredit)
admin.site.register(usercontact, userscontact)
admin.site.register(newProduct, adminproducts)