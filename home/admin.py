from django.contrib import admin
from .models import Reservation,Person,RealEstate_Images,RealEstate ,NewRealEstate,Town,City,MyReservations,Favourits,Comment,Rating

admin.site.register(Person)
admin.site.register(RealEstate_Images)
admin.site.register(NewRealEstate)
admin.site.register(Town)
admin.site.register(City)
admin.site.register(MyReservations)
admin.site.register(Favourits)
admin.site.register(Comment)
admin.site.register(Rating)


class ReservationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'real_estate', 'start_date', 'end_date', 'status', 'total_price')
    list_filter = ('status', 'real_estate')
    search_fields = ('user__username', 'real_estate__person__name')
    actions = ['approve_reservations', 'reject_reservations']

    def approve_reservations(self, request, queryset):
        queryset.update(status='approved')
    approve_reservations.short_description = "Approve selected reservations"

    def reject_reservations(self, request, queryset):
        queryset.update(status='rejected')
    reject_reservations.short_description = "Reject selected reservations"

admin.site.register(Reservation, ReservationAdmin)

# Register your models here.
class RealEstate_admin(admin.ModelAdmin):
    list_display = ['person','address',  'price']
    # this will show the products as table
    # name     price      active
    # a         11         T
    # b         10         T
    #  if you turn it to  list_display =['name','active','price']
    # the order of the table will chang
    # name       active        price
    # a            T           10
    # b            T           11


  #   list_editable = ['address',  'price']
    # now you can edit the (active or not) of every product easier
    # you can put      list_editable = ['name','active',...]
    # but you can not put any thing you put in list_display_links
    # which means you can not put 'name' in list_editable , because you put it i in list_display_links
    search_fields = ['town__name']
    # will put box to search among the products based on name
    list_filter = [ 'address']
    # will create filters based on category and price
    #fields = ['name', 'price', 'category']
    # when you click on the name you will see all information for that products
    # but with this line now you will see just name , price and category


admin.site.register(RealEstate, RealEstate_admin)
# don't forget to do this