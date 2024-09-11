
from django.urls import path
from members import views
urlpatterns = [
    path('',views.first,name="first"),
    path('p/',views.my_members,name="members")
]