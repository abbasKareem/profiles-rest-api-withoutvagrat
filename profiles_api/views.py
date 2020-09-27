from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from profiles_api import models
from profiles_api import serlializers
from profiles_api import permissions



class HelloApiView(APIView):
    """Test API View"""
    serlializer_class = serlializers.HelloSerlializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, put, patch, delete)'
            'Is similar to a traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLS',
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        """Create hello message with our name"""
        serlializer = self.serlializer_class(data=request.data)

        if serlializer.is_valid():
            name = serlializer.validated_data.get('name')
            message = f'Hello {name}'

            return Response({'message': message})
        else:
            return Response(
                serlializer.errors,
                status = status.HTTP_400_BAD_REQUEST,
                 )
    
    def put(self, request, pk=None):
        """handle updating an object"""
        return Response({"method": "PUT"})

    def patch(self, request, pk=None):
        """handle partial update of an object"""
        return Response({'method': 'patch'})
    
    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'delete'})


class HelloViewSet(viewsets.ViewSet):
    """Test Api ViewSet"""
    serlializer_class = serlializers.HelloSerlializer


    def list(self, request):
        """Return a hello message"""
        a_viewset = [
            'Use actions list, create , retrieve, update, partial_update, ',
            'Automatically maps to URLS using Routers',
            'provides more functionality with less code'
        ]
        
        return Response({'message': 'Hello', 'a_viewset': a_viewset})

    def create(self, request):
        """Create a new hello message"""
        serlializers = self.serlializer_class(data=request.data)
        
        if serlializers.is_valid():
            name = serlializers.validated_data.get('name')
            message = f'hello {name}'
            return Response({'message': message})

        else:
            return Response(
                serlializers.errors,
                status = status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handles getting an object by ID"""
        return Response({'httpMethod': 'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""
        return Response({'httpMethod': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of object"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle Removing an object"""
        return Response({'http_method': 'DELETE'})

        
class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serlializers.UserProfileSerilalizer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)








