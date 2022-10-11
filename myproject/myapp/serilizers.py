from rest_framework import serializers
from ordered_model.serializers import OrderedModelSerializer

from .models import Contact, User


class UserSerilizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'contacts']
        read_only_fields = ['contacts']


class ContactSerializer(OrderedModelSerializer):
    # Don't require order but allow it. If none, add to back
    order = serializers.IntegerField(required=False)

    class Meta:
        model = Contact
        fields = ['id', 'name', 'email', 'avatar', 'order', 'user']
        read_only_fields = ['avatar']
        extra_kwargs = {
            'user': {'write_only': True}
        }
