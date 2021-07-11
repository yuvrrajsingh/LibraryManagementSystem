from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=100)
    summary = models.CharField(max_length=1000)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    total_copies = models.PositiveIntegerField()
    available_copies = models.PositiveIntegerField()
    pic = models.ImageField(blank=True, null=True, upload_to='book_image')


    def __str__(self):
        return self.title

CHOICES_COURSE = (
    ('B.Tech', 'B.Tech'),
    ('M.Tech', 'M.Tech'),
    ('BBA', 'BBA'),
    ('MBA', 'MBA'),
    ('B.Arch', 'B.Arch'),
)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=10, unique=True)
    email = models.EmailField()
    contact_no = models.CharField(max_length=10)
    course = models.CharField(max_length=20, choices=CHOICES_COURSE, default=None)
    total_books_Due = models.PositiveIntegerField(default=0)
    pic = models.ImageField(blank=True, upload_to='profile_img')

    def __str__(self):
        return self.roll_no

class Borrower(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    issue_date = models.DateField(null=True, blank=True)
    return_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username