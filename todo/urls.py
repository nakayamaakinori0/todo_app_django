from django.urls import path
from todo import views

urlpatterns = [
    # path('root',view, name='name')
    path("", views.todo_list, name="todo_list"),
    path("create/", views.todo_create, name="todo_create"),
    path("update/<int:pk>/", views.todo_update, name="todo_update"),
]
