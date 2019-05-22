from django.db import models


class Quote(models.Model):
    # Class for the Quotes Model

    quote_author = models.CharField(max_length=100)
    quote_body = models.TextField()
    context = models.CharField(max_length=240, blank=True)
    source = models.URLField(max_length=130, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.quote_author