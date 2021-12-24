from django.db import models
from django.contrib.auth import models as authmodel

# Create your models here.

class Project(models.Model):
    created_by = models.ForeignKey(authmodel.User, on_delete=models.CASCADE,
                                   related_name="%(app_label)s_%(class)s_related", related_query_name="%(app_label)s_%(class)ss")
    project_users = models.ManyToManyField(authmodel.User,  related_name="%(app_label)s_%(class)s_related_users", related_query_name="%(app_label)s_%(class)ss_users")
    name = models.CharField(max_length=50)
    desc = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now=True)

class Budget(models.Model):
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    budget = models.DecimalField(decimal_places=3, max_digits=20)
    created_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(authmodel.User, on_delete=models.CASCADE)

class Category(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField(null=True)
    type = models.CharField(max_length=50)

class Planned(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=3, max_digits=20)
    direction = models.CharField(max_length=50)

class Cashflow(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_by = models.ForeignKey(authmodel.User, on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=3, max_digits=20)
    created_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=50)
    desc = models.TextField(null=True)
    direction = models.CharField(max_length=50)