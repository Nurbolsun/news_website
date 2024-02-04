from rest_framework import serializers, validators
from account.models import CustomUser


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'email')


class RegisterSerializer(serializers.ModelSerializer):
    class Neta:
        model = CustomUser
        fields = ('username', 'password1', 'password2' 'email', 'first_name', 'last_name')

        extra_kwargs = {
            "password": {"write_only": True},
            'email': {
                "required": True,
                "allow_blank": False,
                "validators": [validators.UniqueValidator(
                    CustomUser.objects.all(), "Такими почтами существует"
                )]
            }
        }

    def create(self, validated_data):
        username = validated_data.get('username')
        password1 = validated_data.get('password1')
        password2 = validated_data.get('password2')
        email = validated_data.get('email')
        first_name = validated_data.get('first_name')
        last_name = validated_data.get('last_name')

        user = CustomUser.objects.create_user(
            username=username,
            password1=password1,
            password2=password2,
            email=email,
            first_name=first_name,
            last_name=last_name
        )
        return user
