from django.db import models
from django.contrib.auth.models import AbstractUser



OTDEL = [
    ('Коммерческий', 'Коммерческий'),
    ('Финансовый', 'Финансовый'),
    ('Маркетинговый', 'Маркетинговый'),
]


class CustomUser(AbstractUser):
    middle_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Отчество")
    email = models.EmailField(blank=False, null=False, verbose_name="Почта")
    Verify = models.BooleanField()
    otdel = models.CharField(choices=OTDEL,max_length=255, verbose_name="Отдел")
    is_active = models.BooleanField(default=False)



    def __str__(self):
        return self.email


