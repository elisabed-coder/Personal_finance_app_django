from django.db import models
from api.models import User
from budget.models import Budget

class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
    amount = models.FloatField()

    @property
    def category(self):
        return self.budget.category

    class Meta:
        db_table = 'transactions'

    def __str__(self):
        return f"Transaction by {self.user.name} for {self.category} - {self.amount}"
