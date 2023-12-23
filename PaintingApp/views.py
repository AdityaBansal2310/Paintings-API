from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Painting
from .serializers import PaintingSerializer

class PaintingApiView(APIView):
    def get(self, request, painting_ID=None):
        if painting_ID:
            # Retrieve a specific painting by ID
            painting = Painting.objects.get(ID=painting_ID)
            serializer = PaintingSerializer(painting)
            return Response(serializer.data)
        else:
            # Retrieve all paintings
            paintings = Painting.objects.all()
            serializer = PaintingSerializer(paintings, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = PaintingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    # def delete(self, request, painting_ID):
    #     painting = Painting.objects.get(ID=painting_ID)
    #     painting.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
