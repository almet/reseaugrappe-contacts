# -*- coding: utf-8 -*-
from django.db import models

AMAP_CHOICES = (('orga', 'organisation'),
                ('commission', 'commission'),
                ('participant', 'participant'))


class Contact(models.Model):

    name = models.CharField("Nom", max_length=500, blank=True)
    surname = models.CharField(u"Prénom", max_length=500 ,blank=True)
    role = models.CharField("fonction/rôle", max_length=500, blank=True)
    phone = models.CharField(u"téléphone fixe", max_length=500, blank=True)
    cellphone = models.CharField(u"téléphone portable", max_length=500, blank=True)
    email = models.EmailField(max_length=75, blank=True)
    address = models.CharField("Adresse postale", max_length=500, blank=True)
    url = models.URLField("Site web", verify_exists=False, max_length=200, blank=True)
    field = models.CharField("champ d'action", max_length=500, blank=True, help_text="Specificité de ce contact")
    description = models.TextField("Description", blank=True)
    based_at = models.CharField("Basé à", help_text="lieu ou le contact est basé", max_length=500, blank=True)
    pub_date = models.DateField(auto_now_add=True, auto_now=True, blank=True, null=True)
    amap = models.CharField("Participe aux rencontres AMAP", max_length=200, choices=AMAP_CHOICES, blank=True, null=True)

    class Meta:
        ordering = ['-pub_date']
#        abstract = True


class RencontresAMAP(Contact):
    structure_name = models.CharField("Structure", max_length=500, blank=True)
    contact_grappe = models.ForeignKey('ContactGrappe', to_field='id')
    orga = models.BooleanField('Organisateur?')
    atelier = models.BooleanField('Comission Ateliers?')
    participant = models.BooleanField('Participe?')


class Structure(Contact):
    structure_name = models.CharField("Structure", max_length=500)
    contact_grappe = models.ForeignKey('ContactGrappe', to_field='id')

    class Meta:
        ordering = ['-pub_date', 'structure_name']

    def __unicode__(self):
        return u'%s' % self.structure_name


class Animation(Contact):
    title = models.CharField("Titre", max_length=500)
    cost = models.IntegerField(u"Coût")
    contact_grappe = models.ForeignKey('ContactGrappe', to_field='id')

    class Meta:
        ordering = ['-pub_date', 'title']

    def __unicode__(self):
        return u'%s' % self.title


class ContactGrappe(Contact):

    association = models.CharField("Association", max_length=500)

    class Meta:
        verbose_name_plural = "Grappuleux"

    def __unicode__(self):
        return u"%s %s" % (self.surname, self.name)


class Radio(Structure):
    pass


class Press(Structure):
    class Meta:
        verbose_name = u"Journal"
        verbose_name_plural = "Journaux"


class Website(Structure):
    class Meta:
        verbose_name = u"Site web"
        verbose_name_plural = "Sites web"


class Tv(Structure):
    class Meta:
        verbose_name = "Tv"
        verbose_name_plural = "Tv"


class Administration(Structure):
    pass

class Entreprise(Structure):
    pass

class Association(Structure):
    pass


class Conf(Animation):
    class Meta:
        verbose_name = u"Conférence"

class Film(Animation):
    pass

class AnimPedago(Animation):
    class Meta:
        verbose_name = u"Animation pédagogique"
        verbose_name_plural = u"Animations pédagogiques"

class Musique(Animation):
    class Meta:
        verbose_name = "Groupe de musique"
        verbose_name_plural = "Groupes de musique"

class Spectacle(Animation):
    pass

class Exposition(Animation):
    pass
