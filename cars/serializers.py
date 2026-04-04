from rest_framework import serializers
from .models import Car, Brand, Feature


class CarSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    brand_name = serializers.ReadOnlyField(source='brand.name')

    feature_names = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name',
        source='features'
    )

    class Meta:
        model = Car
        fields = '__all__'
        read_only_fields = ('owner',)


class BrandSerializer(serializers.ModelSerializer):
    car_count = serializers.IntegerField(source='car_set.count', read_only=True)

    class Meta:
        model = Brand
        fields = '__all__'


class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = ['id', 'name']
