from django.db import models


class Result(models.Model):
    isAvailable = models.BooleanField(default=False)
    keyword = models.ForeignKey('Keyword')
    count = models.IntegerField()

    def __unicode__(self):
        return str(self.keyword) + str(self.isAvailable)
    

class Keyword(models.Model):
    key = models.CharField(max_length=50)
    entry = models.ForeignKey('Entry')

    def __unicode__(self):
        return self.key


class Entry(models.Model):
    url = models.URLField()
    email = models.EmailField()

    def __unicode__(self):
        return self.url

    def get_keywords(self):
        keywords = Keyword.objects.filter(entry__url=self.url)

        str_keys = []

        for keyword in keywords:
            str_keys.append(str(keyword))

        return ','.join(str_keys)
