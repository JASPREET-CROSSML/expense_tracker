"""
Django App to track expense in various categories
"""
from django.db import models


class Category(models.Model):
    """
    class to add and manage Category
    """
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Expense(models.Model):
    """
    Class to track expense
    """
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.category.name + ' -> ' + str(self.amount)


