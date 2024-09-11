from django.urls import path
from receipes import views
urlpatterns = [
    path('',views.Receipes,name='receipe'),
    path('delete_receipe/<id>',views.deleteItem,name='delete_receipe'),
    path('update_receipe/<id>',views.updateItem,name='update_receipe'),
    path('receipe_register',views.receipe_register,name='receipe_register'),
    path('receipe_login',views.receipe_login,name='receipe_login'),
    path('receipe_logout',views.receipe_logout,name='receipe_logout')
]
