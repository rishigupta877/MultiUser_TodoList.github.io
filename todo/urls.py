

from unicodedata import name
from django.urls import path
from .import views

urlpatterns = [
    path('', views.home ,name='home'),
    path('login',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('add-todo',views.add_todo,name="add_todo"),
    path('logout',views.signout,name="signout"),
    path('delete-todo<int:id>',views.delete_todo,name="delete"),
    #the <int:id> part here we use in the url in dynamic content it will chaneg it is the new format that you have to understand or agr nhi aaye to django documentation main dekho
    path('change_status<int:id><str:status>',views.change_todo),
]
