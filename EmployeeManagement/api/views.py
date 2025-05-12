from api.models import Employee
from rest_framework import status
from api.renderers import UserRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from api.serializers import UserRegistrationSerializer, UserLoginSerializer, UserProfileSerializer, EmployeeSerializer

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class UserRegistrationView(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request):
        serializer = UserRegistrationSerializer(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = get_tokens_for_user(user)
            return Response({'token': token, 'msg': 'Registration Successful'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)
    

class UserLoginView(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request):
        serializer = UserLoginSerializer(data = request.data)
        if serializer.is_valid():
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email = email, password = password)

            if user is not None:
                token = get_tokens_for_user(user)
                return Response({'token': token,'msg': 'Login Success'}, status=status.HTTP_200_OK)
            return Response({'errors': {'non_field_errors': ['Email or Password is not valid']}}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class UserProfileView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"msg": "Logout Successful!"}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"error": "Invalid or expired refresh token"}, status=status.HTTP_400_BAD_REQUEST)


class EmployerCreateView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployerListView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        employees = Employee.objects.filter(user=request.user)
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)


class EmployerDetailView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get_employee(self, pk, user):
        try:
            return Employee.objects.get(pk=pk, user=user)
        except Employee.DoesNotExist:
            return None
    
    def get(self, request, pk):
        employer = self.get_employee(pk, request.user)
        if employer is None:
            return Response({'error': "Employer not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = EmployeeSerializer(employer)
        return Response(serializer.data)
    
    def put(self, request, pk):
        employer = self.get_employee(pk, request.user)
        if employer is None:
            return Response({'error': "Employer not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = EmployeeSerializer(employer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    
    def delete(self, request, pk):
        employee = self.get_employee(pk, request.user)
        if employee is None:
            return Response({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)
        employee.delete()
        return Response({"msg": "Employer deleted"}, status=status.HTTP_204_NO_CONTENT)