from django.conf.urls import url

from expense_app import views

app_name = 'expense_app'

urlpatterns = [
    # Consisting of urls '/' routing to home and 'add/' routing to form
    url(r'^$', views.home, name='home'),
    url(r'^add/', views.ExpenseFormView.as_view(), name='expense_form')
]
