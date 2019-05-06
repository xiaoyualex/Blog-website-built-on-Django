from django.urls import path

from . import views
app_name = 'blog'
urlpatterns = [
    path('index/',views.index,name='index'),
    path('article/<article_id>',views.article_page,name='article_page'),
    path('edit/<article_id>',views.edit_page,name='edit_page'),
    path('action',views.edit_action,name='edit_action'),
    path('delete/<article_id>',views.delete_article,name='delete_article')
]