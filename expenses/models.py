from django.db import models



class Expenses(models.Model):
    CHOICES = (
        ('HOUSING', 'Housing'),
        ('TRANSPORT', 'Transport'),
        ('FOOD', 'Food'),
        ('HEALTH', 'Health'),
        ('EDUCATION', 'Education'),
        ('FINANCIAL', 'Financial'),
    )
    expense = models.CharField(max_length=10000)
    value = models.FloatField()
    category = models.CharField(max_length=50, choices=CHOICES)
    date = models.DateField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description
