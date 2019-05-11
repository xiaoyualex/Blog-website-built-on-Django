from django.urls import path

from . import views
app_name = 'blog'
urlpatterns = [
    path('index',views.index),
    path('article/<int:article_id>',views.article_page),
    path('edit/<int:article_id>',views.edit_page),
    path('action',views.edit_action),
    path('delete/<int:article_id>',views.delete_article),
    path('about',views.about)
]