from django.urls import path
from api.views import *


urlpatterns = [
    path('auth/signup/', UserRegistrationView.as_view(), name='register'),
    path('auth/login/', UserLoginView.as_view(), name='login'),
    path('auth/profile/', UserProfileView.as_view(), name='profile'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),
    
    path('employers/', EmployerCreateView.as_view(), name='create'),
    path('employees/', EmployerListView.as_view(), name='employee_list'),
    path('employers/<int:pk>/', EmployerDetailView.as_view(), name='get_employee'),
    path('employers/<int:id>', EmployerDetailView.as_view(), name='update'),
    path('employers/<int:id>', EmployerDetailView.as_view(), name='delete')

]
