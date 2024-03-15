from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Painting
from .serializers import PaintingSerializer
import ipdb;

from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import DjangoModelPermissions


class PaintingApiView(APIView):
    permission_classes = (IsAuthenticated,)
    # queryset = Painting.objects.all()  # Added .queryset attribute
    # permission_classes = [DjangoModelPermissions]  # Using DjangoModelPermissions

    def get(self, request, painting_ID=None):
        if painting_ID:
            
            painting = Painting.objects.get(ID=painting_ID)
            serializer = PaintingSerializer(painting)
            return Response(serializer.data)
        else:
            
            paintings = Painting.objects.all()
            serializer = PaintingSerializer(paintings, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = PaintingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, painting_ID):
        try:
            print("Testing")
            painting = Painting.objects.get(ID=painting_ID)
            print(painting_ID)
            print(painting_ID)
        except Painting.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        print(painting.ID)
        painting.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, painting_ID):
        try:
            painting = Painting.objects.get(ID=painting_ID)
        except Painting.DoesNotExist:
            return Response({'error': 'Painting not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = PaintingSerializer(painting, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def patch(self, request, painting_ID):
        try:
            painting = Painting.objects.get(ID=painting_ID)
        except Painting.DoesNotExist:
            return Response({'error': 'Painting not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = PaintingSerializer(painting, data=request.data, partial=True)  # Set partial=True for partial updates
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
