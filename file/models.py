from django.core.validators import FileExtensionValidator, MinLengthValidator
from django.db import models
from django.core.exceptions import ValidationError


def file_size(value):  # add this to some file where you can import it from
    limit = 20971520
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 20 MB.')


# Create your models here.
class File(models.Model):
    title = models.CharField(max_length=30, validators=[MinLengthValidator(7)])
    files = models.FileField(upload_to='', validators=[file_size,
        FileExtensionValidator(allowed_extensions=['docx', 'xls', 'pdf', 'pptx', 'ppt', 'pptm', 'png', 'jpeg'])])
    Verify = models.BooleanField()

    def __str__(self):
        return self.title


class Catalog(models.Model):
    title = models.CharField(max_length=20)
    file = models.ForeignKey(File, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
