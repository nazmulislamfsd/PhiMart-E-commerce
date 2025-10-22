from rest_framework import serializers
from product.models import Product, Category, Review, ProductImage
from decimal import Decimal
from users.models import User

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'product_count']

    product_count = serializers.IntegerField(read_only=True, help_text='`Return number of product in this category`')

# class ProductSerializers(serializers.Serializer):
#     id = serializers.IntegerField()
#     name = serializers.CharField()
#     description = serializers.CharField()
#     unit_price = serializers.DecimalField(max_digits=10, decimal_places=2, source='price')
#     stock = serializers.IntegerField()
#     created_at = serializers.DateTimeField()
#     updated_at = serializers.DateTimeField()
#     price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
#     # category = CategorySerializers()
#     category = serializers.HyperlinkedRelatedField(
#         queryset = Category.objects.all(),
#         view_name = 'category'
#     )


#     def calculate_tax(self, product):
#         return round(product.price * Decimal(1.1), 2)

class ProductImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()
    class Meta:
        model = ProductImage
        fields = ['id','product_id', 'image']


class ProductSerializers(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'stock', 'created_at', 'updated_at', 'price_with_tax', 'category', 'images']
    
    # category = serializers.StringRelatedField()
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')

    def calculate_tax(self, product):
        return round(product.price * Decimal(1.1), 2)
    
    def create(self, validated_data):
        product = Product(**validated_data)
        '''customization er kno kaj thakle seta kore then save hbe'''
        product.save()
        return product

    
    '''field validate'''
    # def validate_price(self, price):
    #     if price < 0:
    #         raise serializers.ValidationError("price could not be negative!")
        
    #     return price

    '''object level validate'''
    # def validate(self, attrs):

    #     if attrs['password1'] != attrs['password2']:
    #         raise serializers.ValidationError("password digit dont match!")
    #     return attrs


class SimpleUserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(method_name='get_current_user_name')
    class Meta:
        model = User
        fields = ['id', 'name',]

    def get_current_user_name(self, obj):
        return obj.get_full_name()


class ReviewSerializers(serializers.ModelSerializer):
    # user = SimpleUserSerializer()
    user = serializers.SerializerMethodField(method_name='get_user')
    class Meta:
        model = Review
        fields = ['id', 'user', 'product', 'ratings', 'comment', 'created_at', 'updated_at']
        read_only_fields = ['user', 'product']

    def get_user(self, obj):
        return SimpleUserSerializer(obj.user).data

    def create(self, validated_data):
        product_id = self.context['product_id']
        review = Review.objects.create(product_id=product_id, **validated_data)
        return review
