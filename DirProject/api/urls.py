
from django.urls import path

from . import views
app_name = 'api'
urlpatterns = [
    path('addFile', views.AddFile.as_view(), name='add_file'),
    path('addDir', views.AddDirectory.as_view(), name='add_directory'),
    path('showFileSystem', views.ShowSystem.as_view(), name='show_file_system'),
    path('deleteFile', views.DeleteFile.as_view(), name='delete_file'),
    path('deleteDir', views.DeleteDirectory.as_view(), name='delete_directory')

]
