import datetime
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Investor


class InvestorModelTests(TestCase):

    def test_kyc_after_whitelist_date_false(self):
        """
        The investor must be kyc'd before being whitelisted.
        """
        kyctime = timezone.now() + datetime.timedelta(days=30)
        investor = Investor(kyc_date=kyctime,whitelist_date=timezone.now())
        self.assertIs(investor.kyc_before_whitelist(), False)
    
    def test_kyc_after_whitelist_date_true(self):
        """
        The investor must be kyc'd before being whitelisted.
        """
        whitelistTime = timezone.now() + datetime.timedelta(days=1)
        investor = Investor(kyc_date=timezone.now(),whitelist_date=whitelistTime)
        self.assertIs(investor.kyc_before_whitelist(), True)

def create_investor(blocktopusid, token,public_address,verto_address):
    """
    Create a question with the given `question_text` and published the
    given number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """
    return Investor.objects.create(blocktopusid=blocktopusid, token=token,public_address=public_address, verto_address=verto_address,kyc_date=timezone.now(), whitelist_date=timezone.now())

class InvestorIndexViewTests(TestCase):

    def test_no_questions(self):
        """
        If no questions exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('manager:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No investors are available.")
        self.assertQuerysetEqual(response.context['latest_investor_list'], [])
    
    def test_one_result(self):
        """
        If one result exists then make sure its displayed
        """
        create_investor(1,"EOS", "EOSjn34lrnnf", "VTXlk3lk4r3r")
        response = self.client.get(reverse('manager:index'))
        self.assertQuerysetEqual(
            response.context['latest_investor_list'],
            ['<Investor: EOS>']
        )
