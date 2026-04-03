from django.db import models

# Create your models here.
class department(models.Model):
    dept_name=models.CharField(max_length=100)

    def __str__(self):
        return self.dept_name
    
class faculty(models.Model):
    name=models.CharField(max_length=50)
    dept=models.ForeignKey(department,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class course(models.Model):
    name=models.CharField(max_length=100)
    dept=models.ForeignKey(department,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class student(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    dept=models.ForeignKey(department,on_delete=models.CASCADE)    
    courses=models.ManyToManyField(course)