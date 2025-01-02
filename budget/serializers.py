from rest_framework import serializers
from budget.models import Budget


class budgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields=['category','maximum_spend', 'theme_color']