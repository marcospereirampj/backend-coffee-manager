# -*- coding: utf-8 -*-

from django.db import models


class Member(models.Model):
    """
        Model Member represent members who can join the queue.

        @author Marcos Pereira
    """
    name = models.CharField("Name", max_length=200, null=False, blank=False)
    email = models.EmailField("Email", null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'coffee'
        ordering = ['name', ]
        verbose_name = 'Member'
        verbose_name_plural = 'Members'


class Registry(models.Model):
    """
        @author Marcos Pereira
    """
    member = models.ForeignKey(Member, verbose_name="Member", related_name="registries")
    date_created = models.DateTimeField("Date of Registry", auto_now=True)

    def __str__(self):
        return "%s - %s" % (self.member.name, self.date_created)

    class Meta:
        app_label = 'coffee'
        ordering = ['date_created',]
        verbose_name = 'Registry'
        verbose_name_plural = 'Registries'
