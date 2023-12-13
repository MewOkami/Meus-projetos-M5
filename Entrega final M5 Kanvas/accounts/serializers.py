from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        max_length=150,
        validators=[UniqueValidator(queryset=Account.objects.all())]
    )
    email = serializers.EmailField(
        max_length=100,
        validators=[UniqueValidator(queryset=Account.objects.all())]
    )
    password = serializers.CharField(
        max_length=128,
        write_only=True
    )
    is_superuser = serializers.BooleanField(default=False)

    class Meta:
        model = Account
        fields = [
            "id",
            "username",
            "password",
            "email",
            "is_superuser",
        ]

    def create(self, validated_data):
        if validated_data["is_superuser"]:
            return Account.objects.create_superuser(**validated_data)
        else:
            return Account.objects.create_user(**validated_data)
