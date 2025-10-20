from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from product.models import Product, Category, Review, ProductImage
from product.serializers import ProductSerializers, CategorySerializers, ReviewSerializers, ProductImageSerializer
from django.db.models import Count
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from product.filters import ProductFilter
from rest_framework.filters import SearchFilter, OrderingFilter
from product.paginations import DefaultPagination
from rest_framework.permissions import IsAdminUser, AllowAny
from api.permissions import IsAdminOrReadOnly, FullDjangoModelPermission
from rest_framework.permissions import DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly
from product.permissions import IsReviewAuthorOrReadOnly
from drf_yasg.utils import swagger_auto_schema
# Create your views here.

# class ViewProducts(APIView):
#     def get(self, request):
#         products = Product.objects.select_related('category').all()
#         serializer = ProductSerializers(products, many=True, context = {'request':request})
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = ProductSerializers(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_NO_CONTENT)
        

class ProductViewSet(ModelViewSet):
    '''
    API endpoint for managing product E-commerce store
    - Allows authenticated admin to create a product
    - Allows user browes and filter product
    - Support searching by name, description, category
    - Support Ordering by price and updated at
    
    '''

    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # filterset_fields = ['category_id', 'price']
    filterset_class = ProductFilter
    search_fields = ['name', 'description']
    ordering_fields = ['price', 'name', 'created_at']
    pagination_class = DefaultPagination
    permission_classes = [IsAdminOrReadOnly]

    def list(self, request, *args, **kwargs):
        '''Retrieve all the products'''
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
            operation_summary="Create a product by Admin",
            operation_description="This allow an admin to create a product",
            request_body= ProductSerializers,
            responses={
                201: ProductSerializers,
                404: "Bad request"
            }
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    

class ProductImageViewSet(ModelViewSet):
    serializer_class = ProductImageSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        return ProductImage.objects.filter(product_id=self.kwargs.get('product_pk'))
    
    def perform_create(self, serializer):
        serializer.save(product_id=self.kwargs.get('product_pk'))
    


# class ProductList(ListCreateAPIView):

#     queryset = Product.objects.select_related('category').all()
#     serializer_class = ProductSerializers

    # def get_queryset(self):
    #     return Product.objects.select_related('category').all()
    
    # def get_serializer_class(self):
    #     return ProductSerializers

    
# class ViewSpecificProduct(APIView):
#     def get(self, request, id):
#         product = get_object_or_404(Product, pk=id)
#         serializer = ProductSerializers(product)

#         return Response(serializer.data)
    
#     def put(self, request, id):
#         product = get_object_or_404(Product, pk=id)
#         serializer = ProductSerializers(product, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

#         return Response(serializer.data)
    
#     def delete(self, request, id):
#         product = get_object_or_404(Product, pk=id)
#         product.delete()

#         return Response({'message': 'Successfully product deleted'}, status=status.HTTP_204_NO_CONTENT)
    

# class ViewCategories(APIView):
#     def get(self, request):
#         categories = Category.objects.annotate(product_count=Count('products'))     #category er sathe total product er count dekhanor jnno annonate kora hoise
#         serializer = CategorySerializers(categories, many=True)

#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = CategorySerializers(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_NO_CONTENT)
    
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.annotate(product_count=Count('products'))
    serializer_class = CategorySerializers
    permission_classes = [IsAdminOrReadOnly]

# class CategoryList(ListCreateAPIView):
#     queryset = Category.objects.annotate(product_count=Count('products'))
#     serializer_class = CategorySerializers


# class ViewSpecificCategory(APIView):
#     def get(self, request, id):
#         category = get_object_or_404(Category, pk=id)
#         serializer = CategorySerializers(category)

#         return Response(serializer.data)
    
#     def put(self, request, id):
#         category = get_object_or_404(Category, pk=id)
#         serializer = CategorySerializers(category, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

#         return Response(serializer.data)
    
#     def delete(self, request, id):
#         category = get_object_or_404(Category, pk=id)
#         category.delete()

#         return Response({'message':'Successfully category deleted'}, status=status.HTTP_204_NO_CONTENT)


# class CategoryDetails(RetrieveUpdateDestroyAPIView):
#     queryset = Category.objects.annotate(product_count=Count('products'))
#     serializer_class = CategorySerializers
#     lookup_field = 'id'



class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializers
    permission_classes = [IsReviewAuthorOrReadOnly]

    def get_queryset(self):
        return Review.objects.filter(product_id = self.kwargs.get('product_pk'))
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_context(self):
        return {'product_id': self.kwargs.get('product_pk')}