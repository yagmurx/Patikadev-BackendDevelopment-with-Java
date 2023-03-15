from django.db import models
from teachers.models import Teacher

class Category(models.Model):
    name = models.CharField(max_length=50, null=True)
    slug = models.SlugField(max_length=50, unique=True, null=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50, null=True)
    slug = models.SlugField(max_length=50, unique=True, null=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name="Course Name", help_text="Enter the course name")
    category = models.ForeignKey(Category, null=True, on_delete=models.DO_NOTHING)
    tags = models.ManyToManyField(Tag, blank=True, null=True)
    teacher = models.ForeignKey(Teacher, null=True, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="courses/%Y/%m/%d/", default="default_course_image.jpg")
    date = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name