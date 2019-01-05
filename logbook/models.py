from django.db import models


# Logbook names/locatons
class LogbookNames(models.Model):
    logbook_name = models.CharField(max_length=250, default='')

    def __str__(self):
        return str(self.logbook_name)