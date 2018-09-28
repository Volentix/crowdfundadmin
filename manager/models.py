from django.db import models

class Investor(models.Model):
    blocktopusid = models.IntegerField()
    token = models.CharField(max_length=10)
    public_address = models.CharField(max_length=200, null=True)
    verto_address = models.CharField(max_length=200, null=True)
    kyc_date = models.DateTimeField('date published')
    whitelist_date = models.DateTimeField('date published', null=True)

    def __str__(self):
        return self.token
    
    def kyc_before_whitelist(self):
        return self.kyc_date < self.whitelist_date

