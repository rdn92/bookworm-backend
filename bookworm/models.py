from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

    def __unicode__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Book(models.Model):
    title = models.CharField(max_length=200)
    isbn = models.CharField(max_length=20)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.PROTECT)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

    def __unicode__(self):
        return self.title
