from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Like, Painting
from .serializers import PaintingSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, permissions

class LikePaintingAPIView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, painting_ID):
        try:
            painting = Painting.objects.get(ID=painting_ID)
        except Painting.DoesNotExist:
            return Response({'error': 'Painting not found'}, status=status.HTTP_404_NOT_FOUND)

        like, created = Like.objects.get_or_create(user=request.user, painting=painting)
        if created:
            return Response({'message': 'Painting liked successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Painting already liked'}, status=status.HTTP_200_OK)

class PaintingApiView(APIView):
    permission_classes = (IsAuthenticated,)
    # queryset = Painting.objects.all()  # Added .queryset attribute
    # permission_classes = [DjangoModelPermissions]  # Using DjangoModelPermissions

    def get(self, request, painting_ID=None):
        if painting_ID:
            try:
                painting = Painting.objects.get(ID=painting_ID)
                serializer = PaintingSerializer(painting)
                likes_count = Like.objects.filter(painting=painting).count()
                user_has_liked = Like.objects.filter(user=request.user, painting=painting).exists()
                painting_data = serializer.data
                painting_data['likes_count'] = likes_count
                painting_data['user_has_liked'] = user_has_liked
                return Response(painting_data)
            except Painting.DoesNotExist:
                return Response({'error': 'Painting not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            paintings = Painting.objects.all()
            serializer = PaintingSerializer(paintings, many=True)
            painting_data = serializer.data
            for painting in painting_data:
                painting_obj = Painting.objects.get(ID=painting['ID'])
                likes_count = Like.objects.filter(painting=painting_obj).count()
                user_has_liked = Like.objects.filter(user=request.user, painting=painting_obj).exists()
                painting['likes_count'] = likes_count
                painting['user_has_liked'] = user_has_liked
            return Response(painting_data)

    def post(self, request):
        serializer = PaintingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, painting_ID):
        try:
            painting = Painting.objects.get(ID=painting_ID)
        except Painting.DoesNotExist:
            return Response({'error': 'Painting not found'}, status=status.HTTP_404_NOT_FOUND)

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
        
        serializer = PaintingSerializer(painting, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
