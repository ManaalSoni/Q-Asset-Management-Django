from django.db import models
from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth.models import User #default django user model
from django.contrib.auth import authenticate
from .models import AssetRequest, Assets

User._meta.get_field('email')._unique = True
# User Serializer
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'is_active','is_superuser')
    #     actions_readonly_fields = {
    #     ('update', 'partial_update'): ('id', 'username', 'email', 'password')
    # }

    # def get_extra_kwargs(self):
    #     extra_kwargs = super(UserSerializer, self).get_extra_kwargs()
    #     action = self.context['view'].action
    #     actions_readonly_fields = getattr(self.Meta, 'actions_readonly_fields', None)
    #     if actions_readonly_fields:
    #         for actions, fields in actions_readonly_fields.items():
    #             if action in actions:
    #                 for field in fields:
    #                     if extra_kwargs.get(field):
    #                         extra_kwargs[field]['read_only'] = True
    #                     else:
    #                         extra_kwargs[field] = {'read_only': True}
    #     return extra_kwargs

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")

class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assets
        fields = '__all__'

class AssetRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetRequest
        fields = ('requestId', 'assetId', 'employeeId', 'description','requestStatus','requested_date', 'updated_date')
