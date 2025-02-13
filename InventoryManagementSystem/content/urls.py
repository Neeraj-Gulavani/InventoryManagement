from django.urls import path
from . import views
app_name = "content"
urlpatterns = [
    path("",views.index,name="index"),
    path("add",views.add_view,name="add_view"),
    path("edit/<int:id>",views.edit_view,name="edit_view"),
    path("delete/<int:id>",views.delete_view,name="delete_view")
]