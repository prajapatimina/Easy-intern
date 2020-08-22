from django.db import models

class students(models.Model):
   StudentName = models.CharField(max_length=50)
   RedgNo = models.CharField(max_length= 20)
   CollegeName = models.CharField(max_length=100)
   Interest = models.CharField(max_length=100)
   Level = models.CharField(max_length=100)
   Email = models.EmailField(max_length=255,unique=True)
   Password = models.CharField(max_length=8)
   ConformPassword = models.CharField(max_length=8)

   def __str__(self):
      return self.Email

