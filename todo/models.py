from django.db import models

# Create your models here.


class Item(models.Model):
    """ Create class of an Item """
    name = models.CharField(max_length=50, null=False, blank=False)
    done_status = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        return self.name
