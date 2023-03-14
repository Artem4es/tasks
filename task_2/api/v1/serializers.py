from rest_framework import serializers

from api.models import Product


class GetSerializer(serializers.ModelSerializer):
    file = serializers.FileField(write_only=True)

    class Meta:
        model = Product
        fields = ('article', 'brand', 'title', 'file')
        read_only_fields = ('brand', 'title')
