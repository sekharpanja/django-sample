from django.conf import settings

from django.db import models


class Lei(models.Model):
    lei = models.CharField(max_length=25)
    legal_name = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.legal_name


class Bond(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    isin = models.CharField(max_length=15)
    size = models.IntegerField()
    currency = models.CharField(max_length=4)
    maturity = models.DateField(default=None)
    lei = models.ForeignKey(Lei, on_delete=models.CASCADE)
