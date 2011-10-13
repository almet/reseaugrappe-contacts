import xlrd
from reseaugrappe.contacts.models import *

u = ContactGrappe(association="unknown")
u.save()

def import_admin():
    wb = xlrd.open_workbook('BDD_interne.xls')
    sh = wb.sheet_by_name('administrations')
    for rownum in range(sh.nrows):
        structure_name, name, surname, role, phone, cellphone, email, address, url, based_at, field, description, projet, contact, date = sh.row_values(rownum)
        a = Administration(structure_name=structure_name, name=name, surname=surname, role=role, phone=phone, cellphone=cellphone, email=email, address=address, url=url, based_at=based_at, field=field, description=description, contact_grappe=u)
        a.save()

def import_grappuleux():
    wb = xlrd.open_workbook('BDD_interne.xls')
    sh = wb.sheet_by_name('Individus_Grappe')
    for rownum in range(sh.nrows):
        association, name, surname, phone, cellphone, email, based_at, date, role = sh.row_values(rownum)
        a = ContactGrappe(association=association, name=name, surname=surname, role=role, phone=phone, cellphone=cellphone, email=email, based_at=based_at)
        a.save()

def import_press():
    wb = xlrd.open_workbook('BDD_medias.xls')
    sh = wb.sheet_by_name('presse_ecrite')

    for rownum in range(sh.nrows):

        structure_name, name, surname, role, phone, cellphone, email, address, url, based_at, field, description, projet, date = sh.row_values(rownum)
        a = Press(structure_name=structure_name, name=name, surname=surname, role=role, phone=phone, cellphone=cellphone, email=email, address=address, url=url, based_at=based_at, field=field, description=description, contact_grappe=u)
        a.save()
