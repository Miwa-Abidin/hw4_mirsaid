from rest_framework import serializers

from . models import Good, Firma, Category

# class GoodSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Good
#         fields = '__all__'
#
# class FirmaSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Firma
#         fields = '__all__'

class CategorySerializer(serializers.Serializer):
    category_name = serializers.CharField(max_length=30)

    def create(self, validated_data):
        category = Category.objects.create(**validated_data)
        return category

    def update(self, instance, validated_data):
        instance.save(**validated_data)
        return instance

class GoodSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    price = serializers.IntegerField()
    firm_id = serializers.IntegerField()
    category_id = serializers.IntegerField()

    def create(self, validated_data):
        good = Good.objects.create(**validated_data)
        return good

    def update(self, instance, validated_data):
        instance.save(**validated_data)
        return instance

class FirmaSerializer(serializers.Serializer):
    firm_name = serializers.CharField(max_length=50)
    adress = serializers.CharField(max_length=50)

    def create(self, validated_data):
        firm = Firma.objects.create(**validated_data)
        return firm

    def update(self, instance, validated_data):
        instance.save(**validated_data)
        return instance




