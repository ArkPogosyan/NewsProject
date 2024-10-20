from django.contrib import admin
from django.urls import path


from News.views import index, get_category, view_news, add_news

urlpatterns = [
    path('', index, name='Home'),
    path('category/<int:category_id>/', get_category, name='Category'),
    path('news/<int:news_id>/', view_news, name='view_news'),
    path('news/add_news', add_news, name='Add_news'),
]
