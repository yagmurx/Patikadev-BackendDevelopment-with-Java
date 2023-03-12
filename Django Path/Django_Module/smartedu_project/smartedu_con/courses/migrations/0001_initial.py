# Generated by Django 4.1.7 on 2023-03-12 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ] 

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the course name', max_length=200, unique=True, verbose_name='Course Name')),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(default='courses/default_course_image.jpg', upload_to='courses/%Y/%m/%d/')),
                ('date', models.DateTimeField(auto_now=True)),
                ('available', models.BooleanField(default=True)),
            ],
        ),
    ]