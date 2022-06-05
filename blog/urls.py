from django.urls import path
from .views import post_create, post_delete, post_detail, post_update

urlpatterns = [
   path('post-create/', post_create, name='post-create'),
   path('detail/<int:id>', post_detail, name="detail"),
   path('update/<int:id>', post_update, name="update"),
   path('delete/<int:id>', post_delete , name="delete"),

   
    
   
]