from django.contrib.auth.models import AbstractUser
from django.db import models



OTDEL = [
    ('Коммерческий', 'Коммерческий'),
    ('Финансовый', 'Финансовый'),
    ('Маркетинговый', 'Маркетинговый'),
]


class CustomUser(AbstractUser):
    middle_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Отчество")
    email = models.EmailField(blank=False, null=False, verbose_name="Почта")
    verify_user_access = models.BooleanField(default=False, verbose_name='Уровень доступа сотрудника - расширенный')
    otdel = models.CharField(choices=OTDEL, max_length=255, verbose_name="Отдел")

    def str(self):
        return self.email