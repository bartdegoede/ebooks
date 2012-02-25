from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    isbn = models.IntegerField(max_length=13, null=True, blank=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    wikipedia = models.URLField(null=True, blank=True)
    pub_date = models.DateField(null=True, blank=True)
    language = models.CharField(max_length=50, null=True, blank=True)
    
    lt_work_id = models.CharField(max_length=255, null=True, blank=True)
    lt_original_title = models.CharField(max_length=255, null=True, blank=True)
    lt_canonical_title = models.CharField(max_length=255, null=True, blank=True)
    lt_original_pub_date = models.DateField(null=True, blank=True)
    
    epub = models.FileField(upload_to='epubs', null=True, blank=True)
    
    created = models.DateTimeField(auto_now_add=True, null=True)
    modified = models.DateTimeField(auto_now=True, null=True)
    
    def __unicode__(self):
        return self.title
        
class Reader(User):
    lt_userid = models.CharField(max_length=255, null=True, blank=True)
    lt_userkey = models.CharField(max_length=255, null=True, blank=True)

    books = models.ManyToManyField(Book, through='Ownership')

    def __unicode__(self):
        return self.username
        
class Ownership(models.Model):
    reader = models.ForeignKey(Reader)
    book = models.ForeignKey(Book)

    created = models.DateTimeField(auto_now_add=True, null=True)
    modified = models.DateTimeField(auto_now=True, null=True)
    
class Genre(models.Model):
    book = models.ForeignKey(Book)
    genre = models.CharField(max_length=255)
    
    created = models.DateTimeField(auto_now_add=True, null=True)
    modified = models.DateTimeField(auto_now=True, null=True)
    
    def __unicode__(self):
        return self.genre

class Quote(models.Model):
    book = models.ForeignKey(Book)
    quote = models.TextField()
    quote_type = models.CharField(max_length=1, choices=(
        ('q', 'Quote'),
        ('e', 'Epigraph')
    ))
    
    created = models.DateTimeField(auto_now_add=True, null=True)
    modified = models.DateTimeField(auto_now=True, null=True)
    
class Author(models.Model):
    name = models.CharField(max_length=255)
    firstname = models.CharField(max_length=255, null=True, blank=True)
    lastname = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=1, choices=(
        ('m', 'Male'),
        ('f', 'Female'),
        ('u', 'Unknown')
    ))
    birth_date = models.DateField(null=True, blank=True)
    birth_place = models.CharField(max_length=255, null=True, blank=True)
    
    # make librarything stuff varchar, just in case
    lt_author_id = models.CharField(max_length=255, null=True, blank=True) 
    lt_author_code = models.CharField(max_length=255, null=True, blank=True)
    lt_legal_name = models.CharField(max_length=255, null=True, blank=True)
    lt_canonical_name = models.CharField(max_length=255, null=True, blank=True)
    
    books = models.ManyToManyField(Book)
    
    created = models.DateTimeField(auto_now_add=True, null=True)
    modified = models.DateTimeField(auto_now=True, null=True)
    
    def __unicode__(self):
        return self.name

class Award(models.Model):
    author = models.ForeignKey(Author)
    award = models.CharField(max_length=255)
    
    created = models.DateTimeField(auto_now_add=True, null=True)
    modified = models.DateTimeField(auto_now=True, null=True)
    
class Cover(models.Model):
    book = models.ForeignKey(Book)
    cover = models.ImageField(upload_to='covers', height_field='height',\
                                                        width_field='width')
    
    created = models.DateTimeField(auto_now_add=True, null=True)
    modified = models.DateTimeField(auto_now=True, null=True)