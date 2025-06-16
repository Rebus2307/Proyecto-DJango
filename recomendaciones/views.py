from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Usuario, Libro, Recomendacion
from .serializers import UsuarioSerializer, LibroSerializer, RecomendacionSerializer

class UsuarioCreateView(generics.CreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def perform_create(self, serializer):
        usuario = serializer.save()
        libros = Libro.objects.all()[:5]  # Selecciona los 5 primeros libros
        for libro in libros:
            Recomendacion.objects.create(usuario=usuario, libro=libro, score=1.0)

class LibroListView(generics.ListAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

class RecomendacionesView(APIView):
    def get(self, request, user_id):
        recomendaciones = Recomendacion.objects.filter(usuario_id=user_id).order_by('-score')
        serializer = RecomendacionSerializer(recomendaciones, many=True)
        return Response(serializer.data)
