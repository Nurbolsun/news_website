from rest_framework import serializers, validators
from account.models import CustomUser


class UserSerializers(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password', 'password2')

    def validate(self, data):
        password = data.get('password')
        password2 = data.get('password2')

        if password and password2 and password != password2:
            raise serializers.ValidationError("Пароли не совпадают.")
        return data

    def create(self, validated_data):
        password = validated_data.pop('password')
        password2 = validated_data.pop('password2')
        if password and password2 and password == password2:
            user = CustomUser.objects.create_user(**validated_data, password=password)
            return user
        raise serializers.ValidationError("Пароли не совпадают.")


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
