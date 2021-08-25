from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    # path('', views.IndexView.as_view(), name='index'),
    path('', views.report, name='report'),
    path('expense', views.expense_form, name='expense'),

]
