from django.urls import path
from .views import UsuarioCreateView, LibroListView, RecomendacionesView

urlpatterns = [
    path('usuarios/registro/', UsuarioCreateView.as_view(), name='registrar-usuario'),
    path('libros/', LibroListView.as_view(), name='listar-libros'),
    path('recomendaciones/<int:user_id>/', RecomendacionesView.as_view(), name='ver-recomendaciones'),
]
