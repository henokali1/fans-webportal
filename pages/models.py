from django.db import models

# Contact Us Form 
class ContactUsForm(models.Model):
    name = models.CharField(max_length=250, default='')
    phone = models.CharField(max_length=250, default='')
    email = models.EmailField(default='')
    msg = models.TextField(default='')

    def __str__(self):
        return self.name + ' - ' + str(self.email)