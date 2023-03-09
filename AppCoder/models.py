from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()

class Estudiantes(models.Model):
    nombre = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)

class Profesor(models.Model):
    nombre = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
