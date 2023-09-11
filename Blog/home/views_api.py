from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


class LoginView(APIView):
    
    def post(self, request):
        response = {}
        response['status'] = 500
        response['message'] = "Something went wrong"
        
        try:
            data = request.data

            if data.get('username') is None:
                response['message'] = 'username not found'
                raise Exception('username not found')
            if data.get('password') is None:
                response['message'] = 'key password not found'
                raise Exception("key password is not found")
            
            check_user = User.objects.filter(username = data.get('username')).first()
            if check_user is None:
                response['message'] = 'invalid username, username not found'
                raise Exception('username not found')
            
            user_obj = authenticate(username = data.get('username'), password = data.get('password'))
            if user_obj:
                response['status'] = 200
                response['message'] = "welcome"
            else:
                response['message'] = 'invalid username or password'
                raise Exception("invalid username or password")
                
        except Exception as e:
            print(e)
            
        return Response(response)
    
LoginView = LoginView.as_view()


class SignupView(APIView):
    
    def post(self, request):
        response = {}
        response['status'] = 500
        response['message'] = "Something went wrong"
        
        try:
            data = request.data

            if data.get('username') is None:
                response['message'] = 'username not found'
                raise Exception('username not found')
            if data.get('password') is None:
                response['message'] = 'password not found'
                raise Exception("password not found")
            
            check_user = User.objects.filter(username = data.get('username')).first()
            if check_user:
                response['message'] = 'username already taken'
                raise Exception('username already taken')
            
            user_obj = User.objects.create(username = data.get('username'))
            user_obj.set_password(data.get('password'))
            user_obj.save()
            response['status'] = 200
            response['message'] = "user created successfully"
        except Exception as e:
            print(e)
            
        return Response(response)
            
SignupView = SignupView.as_view()