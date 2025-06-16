from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo

class Recomendacion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='recomendaciones')
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    score = models.FloatField(default=0.0)  # Puede usarse para ordenar

    class Meta:
        unique_together = ('usuario', 'libro')
