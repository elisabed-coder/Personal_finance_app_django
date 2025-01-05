from django.urls import path

from budget.models import Budget
from budget.views import BudgetCreateView,BudgetChoicesView,BudgetsView

urlpatterns = [
    path('create_budget/', BudgetCreateView.as_view(), name='create_budget'),
    path('budget/choices/', BudgetChoicesView.as_view(), name='budget_choices'),

    path('get_budgets/', BudgetsView.as_view(), name='get_budgets'),



]