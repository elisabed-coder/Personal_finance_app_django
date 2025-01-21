from django.db import models
from api.models import User

class Budget(models.Model):
    CATEGORY_CHOICES = [
        ('Bills', 'Bills'),
        ('Entertainment', 'Entertainment'),
        ('Groceries', 'Groceries'),
        ('Diningout', 'Diningout'),
        ('Transportation', 'Transportation'),
        ('PersonalCare', 'PersonalCare'),
        ('Education', 'Education'),
        ('LifeStyle', 'LifeStyle'),
        ('Shopping', 'Shopping'),
        ('General', 'General'),
    ]

    THEME_CHOICES = [
        ('#394a51', 'Charcoal Gray'),
        ('#7fa99b', 'Seafoam Green'),
        ('#fbf2d5', 'Light Cream'),
        ('#fdc57b', 'Goldenrod'),
        ('#fad662', 'Light Yellow'),
        ('#e57b5c', 'Coral'),
        ('#be4747', 'Burgundy'),
        ('#ffb6b9', 'Light Pink')
    ]
    id=models.AutoField(primary_key=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    category=models.CharField(max_length=255, choices=CATEGORY_CHOICES)
    theme_color = models.CharField(max_length=255, choices=THEME_CHOICES)
    maximum_spend = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'budget_budget'


    def save(self, *args, **kwargs):
        if self.category:
            self.category = self.category.capitalize()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.user.name}'s Budget for {self.category}"