from django.db import models
from django.utils import timezone

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Genre(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Author(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    publication_date = models.DateField()
    #isbn = models.CharField(max_length=13)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, blank=True)
    authors = models.ManyToManyField(Author)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title

class Publisher(BaseModel):
    name = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.name

class Magazine(BaseModel):
    title = models.CharField(max_length=200)
    publication_date = models.DateTimeField()
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Reader(BaseModel):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Review(BaseModel):
    content = models.TextField()
    rating = models.DecimalField(max_digits=5, decimal_places=2)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.reader} - {self.book}"
