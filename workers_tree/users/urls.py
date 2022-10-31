from django.urls import path
from workers_tree.users import views


urlpatterns = [
    path('sign-up/',
         views.UserCreateView.as_view(),
         name='sign-up'),
    path('login/',
         views.LoginView_.as_view(),
         name='login'),
    path('logout/',
         views.LogoutView_.as_view(),
         name='logout'),
    path('<int:pk>/update/',
         views.UserUpdateView.as_view(),
         name='update'),
    path('<int:pk>/delete/',
         views.UserDeleteView.as_view(),
         name='delete'),
]
