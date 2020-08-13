from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    photo = models.ImageField(upload_to='authors', default=None)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    bio = models.TextField()

    def __str__(self):
        return self.surname


class Book(models.Model):
    title = models.CharField(max_length=150)
    poster = models.ImageField(upload_to='posters')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    DIFFICULTIES = [
        ('L', 'Low'),
        ('M', 'Medium'),
        ('H', 'Hard'),
    ]
    difficulty = models.CharField(max_length=20, choices=DIFFICULTIES, default='L')
    LANGUAGES = [
        ('EN', 'English'),
        ('RU', 'Russian'),
    ]
    TECHNOLOGIES = [
        ('C++', 'C_Plus_Plus'),
        ('Python', 'Python'),
        ('JS', 'JavaScript'),
        ('Java', 'Java'),
        ('Others', 'Others'),
    ]
    technology = models.CharField(max_length=30, choices=TECHNOLOGIES, default='Others')
    language = models.CharField(max_length=20, choices=LANGUAGES, default='EN')
    content = models.TextField(default=None)
    score = models.FloatField()
    main_file = models.FileField(upload_to='books', default=None)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    comment_body = models.CharField(max_length=255)
    pub_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user_name.username


class Feedback(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    feed = models.TextField()

    def __str__(self):
        return self.name
