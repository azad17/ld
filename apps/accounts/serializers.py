from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model

User = get_user_model()

class SignupSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email','password','confirm_password']

        extra_kwargs = {
            "password": {"write_only":True}
        }

    def validate(self,attrs):
        print("validate-")
        if attrs['confirm_password'] != attrs['password']:
            raise serializers.ValidationError("Password Not matching")
        return attrs

    def validate_password(self,value):
        print("validatepassword-")
        if value == 'password':
            raise serializers.ValidationError("This passsword cannot be used !")
        return value


    def create(self, validated_data):
        print("create-")
        validated_data.pop("confirm_password")
        return User.objects.create_user(
            email=validated_data['email'],
            password = validated_data['password']
        )

class SigninSerilizer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def save(self):
        try:
            token = RefreshToken(self.validated_data['refresh'])
            token.blacklist()
        except Exception:
            raise serializers.ValidationError({"error":"Invalid or expired token"})
            

class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields =['email','age','team',]