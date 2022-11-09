from django.urls import path
from workers_tree.employees import views


urlpatterns = [
    path('', views.EmployeesView.as_view(), name='employees'),
    path('tree', views.TreeView.as_view(), name='tree'),
    path('js-tree', views.TreeJsonView.as_view(), name='js-tree'),
    path('cabinet', views.PersonalCabinet.as_view(), name='cabinet'),
    path(
        'management',
        views.PersonnelManagement.as_view(),
        name='management',
    ),
    path('<int:pk>',
         views.EmployeeUpdateView.as_view(),
         name='update-employee'),
]
