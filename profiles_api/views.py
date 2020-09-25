from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serlializers



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
        
        