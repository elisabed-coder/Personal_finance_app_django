from tkinter.font import names

from django.urls import path

from budget.models import Budget
from budget.views import BudgetCreateView, BudgetChoicesView, BudgetsView, DeleteBudget

urlpatterns = [
    path('create_budget/', BudgetCreateView.as_view(), name='create_budget'),
    path('budget/choices/', BudgetChoicesView.as_view(), name='budget_choices'),

    path('get_budgets/', BudgetsView.as_view(), name='get_budgets'),
    path('deleteBudget/', DeleteBudget.as_view(), name="deleteBudget"),



]