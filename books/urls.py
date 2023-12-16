from.import views
from django.urls import path,include

urlpatterns = [
    
    path('add/',views.Add,name="add"),
    path('view/',views.viewAll,name='view'),
    path('search/',views.Search,name='search'),
    path('delete',views.Delete,name='delete')
   
]