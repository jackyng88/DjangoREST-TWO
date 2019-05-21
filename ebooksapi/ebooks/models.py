from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User


class Ebook(models.Model):
    # Ebook class extending from Model
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=60)
    description = models.TextField()
    publication_date = models.DateField()

    def __str__(self):
        return self.title


class Review(models.Model):
    # Review class extending from Model
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    review_author = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.TextField(blank=True, null=True)
    # rating has the PositiveIntegerField with validator fields imported
    # enforcing that min value is 1 and max value is 5.
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1),
                                                     MaxValueValidator(5)])
    ebook = models.ForeignKey(Ebook,
                              on_delete=models.CASCADE,
                              related_name='reviews')

    def __str__(self):
        return str(self.rating)