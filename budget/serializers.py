from rest_framework import serializers
from budget.models import Budget


class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields=['id', 'category','maximum_spend', 'theme_color', "user"]