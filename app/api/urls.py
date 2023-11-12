from django.urls import path
from . import views

app_name = 'valentino'

urlpatterns = [
 path('/categories/',
      views.SubjectListView.as_view(),
      name='categories_list'),
path('/menu/',
     views.MyOwnView.as_view(),
     name="JSON_for_frontend")
]