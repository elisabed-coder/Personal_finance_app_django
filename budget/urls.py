from django.urls import path
from budget.views import BudgetCreateView,BudgetChoicesView

urlpatterns = [
    path('create_budget/', BudgetCreateView.as_view(), name='create_budget'),
    path('budget/choices/', BudgetChoicesView.as_view(), name='budget_choices'),

]