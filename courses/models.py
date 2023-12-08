from django.db import models as m
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from .fields import OrderField

# Create your models here.
class Subject(m.Model):
    title = m.CharField(max_length=200)
    slug = m.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class Course(m.Model):
    owner = m.ForeignKey(User, 
                         related_name='courses_created',
                         on_delete=m.CASCADE)
    subject = m.ForeignKey(Subject,
                           related_name='courses',
                           on_delete=m.CASCADE)
    title = m.CharField(max_length=200)
    slug = m.SlugField(max_length=200, unique=True)
    overview = m.TextField()
    created = m.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

class Module(m.Model):
    course = m.ForeignKey(Course,
                          related_name='courses',
                          on_delete=m.CASCADE)
    title = m.CharField(max_length=200)
    description = m.TextField(blank=True)
    order = OrderField(blank=True, for_fields=['course'])

    class Meta:
        ordering = ['order']

    def __str__(self):
            return f"{self.order}, {self.title}"
    
class Content(m.Model):
    module = m.ForeignKey(Module, 
                           related_name='contents',
                           on_delete=m.CASCADE)
    content_type = m.ForeignKey(ContentType,
                                on_delete=m.CASCADE,
                                limit_choices_to={'model__in': (
                                    'text',
                                    'video',
                                    'image',
                                    'file'
                                )})
    object_id = m.PositiveIntegerField()
    item = GenericForeignKey('content_type', 'object_id')
    order = OrderField(blank=True, for_fields=['module'])

    class Meta:
        ordering = ['order']


class ItemBase(m.Model):
    owner = m.ForeignKey(User,
                         related_name='%(class)s_related',
                         on_delete=m.CASCADE)
    title = m.CharField(max_length=200)
    created = m.DateTimeField(auto_now_add=True)
    updated = m.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True

    def __str__(self):
        return self.title
    
class Text(ItemBase):
    content = m.TextField()

class File(ItemBase):
    file = m.FileField(upload_to='files')

class Image(ItemBase):
    file = m.FileField(upload_to='images')

class Video(ItemBase):
    url = m.URLField()

