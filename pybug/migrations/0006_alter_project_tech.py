# Generated by Django 4.1.3 on 2022-11-22 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybug', '0005_project_tech_alter_project_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='tech',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
