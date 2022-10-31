from django.contrib import admin
from django.urls import path, include
from workers_tree.employees import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('employees/', views.EmployeesView.as_view(), name='employees'),
    path('users/', include('workers_tree.users.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
