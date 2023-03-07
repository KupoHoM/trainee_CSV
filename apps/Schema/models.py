from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class TypeModel(models.Model):
    COLUMN_TYPES = [
        ('full_name', 'Full Name (First + Last)'),
        ('job', 'Job'),
        ('integer', 'Integer'),
        ('email', 'Email'),
        ('domain_name', 'Domain Name'),
        ('phone_number', 'Phone Number'),
        ('company_name', 'Company Name'),
        ('address', 'Address'),
        ('date', 'Date')
    ]
    column_type = models.CharField(max_length=20, choices=COLUMN_TYPES)

    def __str__(self):
        return self.column_type


class SchemaModel(models.Model):
    name = models.CharField(max_length=200)
    columns = models.ForeignKey(TypeModel, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
