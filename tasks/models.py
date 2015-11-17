from django.db import models


class Entry(models.Model):
    url = models.URLField()
    email = models.EmailField()

    def __unicode__(self):
        return self.url


class Keyword(models.Model):
    key = models.CharField(max_length=50)
    entry = models.ForeignKey(Entry)

    def __unicode__(self):
        return self.key


class Result(models.Model):
    isAvailable = models.BooleanField(default=False)
    keyword = models.ForeignKey(Keyword)

    def __unicode__(self):
        return self.keyword + self.isAvailable
