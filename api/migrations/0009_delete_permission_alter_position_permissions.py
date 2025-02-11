# Generated by Django 5.1.3 on 2024-11-15 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_permission_position_permissions'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Permission',
        ),
        migrations.AlterField(
            model_name='position',
            name='permissions',
            field=models.ManyToManyField(blank=True, related_name='positions', to='auth.permission'),
        ),
    ]
