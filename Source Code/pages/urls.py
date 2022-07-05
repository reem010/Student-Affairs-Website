from django.urls import path
from .import views
urlpatterns=[
    path( '', views.outer , name='outer'),
    path( 'home.html', views.home , name='home'),
    path( 'addstudent.html', views.add , name='addstudent'),
    path( 'allstudents.html', views.allstudents , name='allstudents'),
    path( 'depart.html', views.departmentt, name='department'),
    path( 'login.html', views.login, name='login'),
    path( 'register.html', views.register, name='register'),
    path( 'search.html', views.search , name='search'),
    path( 'outerpage.html', views.outer, name='outer'),
    path( 'StudentUpdate.html', views.StudentUpdate, name='update'),
    path('update/<int:id>',views.update ,name='update'),
    path('<int:id>/delete', views.delete ,name='delete'),
    path('<int:id>/department', views.department ,name='department'),
    path('changestat/<int:id>', views.changestat ,name='change'),
]