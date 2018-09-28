from django.db import models

class Investor(models.Model):
    blocktopusid = models.IntegerField()
    token = models.CharField(max_length=10)
    public_address = models.CharField(max_length=200)
    verto_address = models.CharField(max_length=200)
    kyc_date = models.DateTimeField('date published')
    whitelist_date = models.DateTimeField('date published')

    def __str__(self):
        return self.token
