from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from .models import Product, User
from .serializers import ProductSerializer, ProductUserSerializer
import random



class ProductViewSet(viewsets.ViewSet):

    queryset = Product.objects.all()

    def list(self, request):

        try:
            products = self.queryset
            serializer = ProductSerializer(products, many=True)
            data= {
                "Status": "SUCCESS",
                "Message": serializer.data
            }
            return Response(status=status.HTTP_200_OK, data=data)
        except Exception as e:
            error_data= {
                "Status": "FAILED",
                "Message": "Products not listed"
            }
            
            return Response(data=error_data, status=status.HTTP_400_BAD_REQUEST)


    def create(self, request): 
        try:
            serializer = ProductSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            data= {
                "Status": "SUCCESS",
                "Message": serializer.data
            }
            return Response(status=status.HTTP_201_CREATED, data=data)
        except Exception as e:
            error_data= {
                "Status": "FAILED",
                "Message": "Products not created"
            }
            
            return Response(data=error_data, status=status.HTTP_400_BAD_REQUEST)


    def retrieve(self, request, pk=None):
        try:
            product= self.queryset.filter(id=pk)[0]
            serializer = ProductSerializer(product)
            data= {
                "Status": "SUCCESS",
                "Message": serializer.data
            }
            return Response(data=data, status=status.HTTP_200_OK)
        except Exception as e:
            error_data= {
                "Status": "SUCCESS",
                "Message": "Products successfully deleted"
            }
            
            return Response(data=error_data, status=status.HTTP_400_BAD_REQUEST)
 

    def update(self, request,pk=None): 

        try:
            product= self.queryset.filter(id=pk)[0]
            serializer = ProductSerializer(instance=product, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            data= {
                "Status": "SUCCESS",
                "Message": serializer.data
            }

            return Response(data=data, status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            error_data= {
                "Status": "SUCCESS",
                "Message": "Products successfully deleted"
            }
            return Response(data=error_data, status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request,pk=None): 
        try:
            product= self.queryset.filter(id=pk)[0]
            print(product.id)
            product.delete() 
            data= {
                "Status": "SUCCESS",
                "Message": "Product(s) successfully deleted"
            }
            
            return Response(data=data, status=status.HTTP_204_NO_CONTENT)

        except Exception as e:
            print(e)
            error_data= {
                "Status": "FAILED",
                "Message": "Product(s) not deleted or does not exists"
            }
            
            return Response(data=error_data, status=status.HTTP_400_BAD_REQUEST)

class UserViewSet(viewsets.ViewSet):
    queryset = User.objects.all()
    
    def list(self, request):
        
        try:
            users = self.queryset
            user = random.choice(users)
            data = {"id": user.id}

            return_data= {
                "Status": "SUCCESS",
                "Message": data
            }
            return Response(status=status.HTTP_200_OK, data=return_data)
        except Exception as e:
            error_data= {
                "Status": "FAILED",
                "Message": "user not listed"
            }
            
            return Response(data=error_data, status=status.HTTP_400_BAD_REQUEST)


    def create(self, request): 
        try:
            serializer = ProductUserSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            data= {
                "Status": "SUCCESS",
                "Message": serializer.data
            }
            return Response(status=status.HTTP_201_CREATED, data=data)
        except Exception as e:
            error_data= {
                "Status": "FAILED",
                "Message": "Product(s) user not created"
            }
            
            return Response(data=error_data, status=status.HTTP_400_BAD_REQUEST)


    # def retrieve(self, request, pk=None):
    #     try:
    #         product= self.queryset.filter(id=pk)[0]
    #         serializer = ProductSerializer(product)
    #         data= {
    #             "Status": "SUCCESS",
    #             "Message": serializer.data
    #         }
    #         return Response(data=data, status=status.HTTP_200_OK)
    #     except Exception as e:
    #         error_data= {
    #             "Status": "SUCCESS",
    #             "Message": "Products successfully deleted"
    #         }
            
    #         return Response(data=error_data, status=status.HTTP_400_BAD_REQUEST)



