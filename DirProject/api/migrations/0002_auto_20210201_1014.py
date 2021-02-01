# Generated by Django 3.0.4 on 2021-02-01 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='directory',
            name='sub_directories',
        ),
        migrations.AddField(
            model_name='directory',
            name='parent_directory',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.PROTECT, to='api.Directory'),
        ),
    ]