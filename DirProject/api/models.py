from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

# Create your models here.


class Directory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, unique=True)
    creation_date = models.DateTimeField(default=timezone.now)
    parent_directory  = models.ForeignKey('self',on_delete=models.CASCADE ,default=None,null=True)

    def __str__(self):
        

        return 'directory name: '+self.name + ',  parent directory: '+ str(self.parent_directory) 


class File(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, unique=True)
    size = models.IntegerField(default=0)
    creation_date = models.DateTimeField(default=timezone.now)
    directory = models.ForeignKey(Directory, on_delete=models.CASCADE, related_name='files')

    def __str__(self):
        return ' file name: ' + self.name + ', directory: ' + str(self.directory) + ', creation date: '+str(self.creation_date)
