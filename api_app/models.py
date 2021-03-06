from django.db import models
from .validators import validate_xml
import onixcheck

class SingletonModel(models.Model):

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

class OnixFile(SingletonModel):
    onix_file = models.FileField(blank=False, null=False)
    def __str__(self):
        return self.onix_file.name

    def get_path(self):
        return self.onix_file.path
