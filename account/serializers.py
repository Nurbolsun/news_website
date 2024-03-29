from rest_framework import serializers

from .models import User, Subscriber, Newsletter


class SubscriptionSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField(max_length=100)


class UnsubscribeSerializer(serializers.Serializer):
    email = serializers.EmailField()


class NewsletterSerializer(serializers.Serializer):
    class Meta:
        model = Newsletter
        fields = (
            'id',
            'subject',
            'content',
            'sent_at',
        )

class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'password',
            'password_confirmation',
        )

    def validate(self, attrs):
        password = attrs.get('password')
        password_confirmation = attrs.pop('password_confirmation', None)

        if password != password_confirmation:
            raise serializers.ValidationError("Пароли не совпадают")
        return attrs

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                "Пользователь с таким email уже существует.")
        return value


    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if not email:
            raise serializers.ValidationError('Укажите электронную почту для входа.')

        if not password:
            raise serializers.ValidationError('Укажите пароль.')

        user = User.objects.filter(email=email).first()

        if not user:
            raise serializers.ValidationError("Пользователь с такой электронной почтой не зарегистрирован")

        if not user.check_password(password):
            raise serializers.ValidationError("Неверный пароль")

        return data


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'phone_number',
            'avatar',
            'gender',
            'age',
        )


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()


class OTPVerificationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp_reset = serializers.CharField()


class CreateNewPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True)

    def validate(self, attrs):
        password = attrs.get('password')
        password_confirmation = attrs.pop('password_confirmation', None)

        if password != password_confirmation:
            raise serializers.ValidationError("Пароли не совпадают")
        return attrs