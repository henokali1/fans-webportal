from django.db import models


# All logbook names/locatons
class LogbookName(models.Model):
    logbook_name = models.CharField(max_length=250, default='')

    def __str__(self):
        return str(self.logbook_name)


# New Logbook data
class NewLog(models.Model):
    posted_on = models.DateTimeField(auto_now=True)
    posted_by = models.EmailField(max_length=254, default='')
    posted_by_name = models.CharField(max_length=250, default='')
    date = models.CharField(max_length=50, default='')
    time = models.CharField(max_length=50, default='')
    logbook_name = models.CharField(max_length=250, default='')
    description = models.TextField()
    

    def __str__(self):
        return str(self.pk)