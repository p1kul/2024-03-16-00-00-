from django.contrib import admin
from .models import Buyer, Game

@admin.register(Buyer)
class Buyer_admin(admin.ModelAdmin):
    list_display = ('name', 'balance', 'age')
    search_fields = ('name',)

@admin.register(Game)
class Game_admin(admin.ModelAdmin):
    list_display = ('title', 'cost', 'size', 'age_limited')
    list_filter = ('cost', 'size', 'age_limited')
    search_fields = ('title',)
    fields = (
        (None, {
            'fields': ('title', 'cost'),
        }),
        ('Description', {
            'fields': ('description', 'size', 'age_limited'),
        }),
    )



