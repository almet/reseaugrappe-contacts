# -*- coding: utf-8 -*-
from django.contrib import admin
from reseaugrappe.contacts.models import *


class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'pub_date'
    fieldsets = (
        ("", {
            'fields': [('surname', 'name'),
                       'role',
                       ('phone', 'cellphone'),
                        'email', 'amap']
        }),
        (u"Autres informations (détails)", {
            'fields': ['address', 'url', 'field', 'description', 'based_at']
        }),
    )
    list_display = ['surname', 'name', 'role', 'email', 'cellphone', 'phone']
    list_editable = [] #['email', 'cellphone', 'phone']
    save_on_top = True
    search_fields = ['surname', 'name', 'email', 'cellphone', 'phone',
            'based_at', 'description', 'address', 'field', 'amap']

    list_filter = ('based_at', 'amap')


class GrappeAdmin(ContactAdmin):
    fieldsets = (
        ("", {
            'fields': [('surname', 'name'),
                       ('role', 'association'),
                       ('phone', 'cellphone'),
                       'email', 'amap']
        }),
        (u"Autres informations (détails)", {
            'fields': ['address', 'url', 'field', 'description', 'based_at']
        }),
    )
    list_display = ['surname', 'name', 'association', 'role', 'email', 'cellphone', 'phone']
    search_fields = ['surname', 'name', 'email', 'cellphone', 'phone', 'based_at', 'description', 'address', 'field', 'association']

    list_filter = ('based_at', 'association')


class StructureAdmin(ContactAdmin):

    fieldsets = (
        ("", {
            'fields': ['structure_name',
                       ('surname', 'name'),
                       'role',
                       ('phone', 'cellphone'),
                       'email', 'amap']
        }),
        (u"Autres informations (détails)", {
            'fields': ['address', 'url', 'field', 'description', 'based_at',
                'contact_grappe']
        }),
    )
    list_display = ['structure_name', ] + ContactAdmin.list_display
    search_fields = ['structure_name', ] + ContactAdmin.search_fields


class AnimationAdmin(ContactAdmin):

    fieldsets = (
        ("", {
            'fields': [('title', 'cost'),
                       ('surname', 'name'),
                       'role',
                       ('phone', 'cellphone'),
                       'email', 'amap']
        }),
        (u"Autres informations (détails)", {
            'fields': ['address', 'url', 'field', 'description', 'based_at',
                'contact_grappe']
        }),
    )
    list_display = ['title'] + ContactAdmin.list_display + ['cost']
    search_fields = ['title', ] + ContactAdmin.search_fields


class RencontresAMAPAdmin(StructureAdmin):
    fieldsets = (
        ("", {
            'fields': ['structure_name',
                       ('surname', 'name'),
                       'role',
                       ('phone', 'cellphone'),
                       'email',
                       ('orga', 'atelier', 'participant')]
        }),
        (u"Autres informations (détails)", {
            'fields': ['address', 'url', 'field', 'description', 'based_at',
                'contact_grappe']
        }),
    )
    list_display = StructureAdmin.list_display + ['orga', 'atelier', 'participant', ] 
    search_fields = StructureAdmin.list_display + ['orga', 'atelier', 'participant', ] 
    list_filter = ('orga', 'atelier', 'participant')


admin.site.register((Radio, Tv, Website, Press, Administration,
                     Entreprise, Association), StructureAdmin)
admin.site.register(RencontresAMAP, RencontresAMAPAdmin)
admin.site.register((Conf, Film, AnimPedago, Musique, Exposition), AnimationAdmin)
admin.site.register(ContactGrappe, GrappeAdmin)
admin.site.register(Contact, ContactAdmin)
