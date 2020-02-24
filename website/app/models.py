from django.db import models

# Create your models here.

class StudentModel(models.Model):
    batch_number =models.AutoField(primary_key=True)
    name=models.CharField(max_length=25)
    email=models.EmailField(max_length=30,unique=True)
    password=models.CharField(max_length=8)
    phone_number =models.IntegerField()
    # photo =models.ImageField(upload_to="images/")

    def __str__(self):
        return self.batch_number

class Question(models.Model):
    body = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)


class Quiz(models.Model):
    questions = models.ManyToManyField(Question)