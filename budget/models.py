from django.db import models
from api.models import User

class Budget(models.Model):
    CATEGORY_CHOICES = [
        ('bills', 'Bills'),
        ('entertainment', 'Entertainment'),
        ('groceries', 'Groceries'),
        ('diningout', 'Diningout'),
        ('transportation', 'Transportation'),
        ('personalCare', 'PersonalCare'),
        ('education', 'Education'),
        ('lifeStyle', 'LifeStyle'),
        ('shopping', 'Shopping'),
        ('general', 'General'),
    ]

    THEME_CHOICES = [
        ('#FF6B6B', 'Coral Red'),
        ('#4ECDC4', 'Turquoise'),
        ('#45B7D1', 'Sky Blue'),
        ('#96CEB4', 'Sage Green'),
        ('#FFEEAD', 'Soft Yellow'),
        ('#D4A5A5', 'Dusty Rose'),
        ('#9370DB', 'Purple'),
        ('#3CB371', 'Forest Green')
    ]
    id=models.AutoField(primary_key=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    category=models.CharField(max_length=255, choices=CATEGORY_CHOICES)
    theme_color = models.CharField(max_length=255, choices=THEME_CHOICES)
    maximum_spend = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.user.name}'s Budget for {self.category}"