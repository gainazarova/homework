from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    nationality = models.CharField(max_length=100)
    height = models.IntegerField(blank=True)

    def __str__(self):
        return f'{self.last_name} {self.first_name}'

class Musician(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)
    def __str__(self): return f'{self.name}'
class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()
    def __str__(self): return f'{self.artist}:{self.name}'


#Создали проект
#   1. установка (Django, psycopg2-binary)
#   2. создание проекта django-admin startproject <name> .
#   3. создали приложение при помощи  ./manage.py startapp <name>
#
# Настройка проекта
#   1. в installed apps записали наше приложение
#   2. настроили базу данных(создать базу данных в постгресе, а потом зайти в настройки проекта settings.py)
#   3. проведение миграций
#
# Написали Модельку Person
# зарегистрировали в админ-панеле
# создали супер-юзера ./manage.py create superuser

#д.з развернуть 3-5 проектов


class Teacher(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    number = models.CharField(max_length=30)
    language = models.CharField(max_length=100)

    def __str__(self): return f'{self.name} {self.last_name}'


class Students(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self): return f'{self.name} {self.last_name}'

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'


class Group(models.Model):
    title = models.CharField(max_length=50)
    teacher = models.ForeignKey(Teacher, related_name='teachers', on_delete=models.CASCADE)
    def __str__(self): return f'{self.title}'


class GroupStudents(models.Model):
    student = models.ForeignKey(Students, related_name='students', on_delete=models.CASCADE)
    group = models.ForeignKey(Group, related_name='groups', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Group student'
        verbose_name_plural = 'Group students'

    def __str__(self): return f'{self.student} - {self.group}'


