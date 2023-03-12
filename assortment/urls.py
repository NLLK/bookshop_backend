from django.contrib.auth import views
from django.urls import path

import assortment.views as views

urlpatterns = [
    path('get_assortment_list/', views.GetAssortmentListView.as_view()),
    path('get_books_info/', views.GetAssortmentBookInfo.as_view())
]