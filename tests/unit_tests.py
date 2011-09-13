import time
import datetime
from test_factory import Factory
from djangosanetesting.cases import DatabaseTestCase, DestructiveDatabaseTestCase
from qi_toolkit.selenium_test_case import QiUnitTestMixin
from django.test import TestCase

from django.core import mail
from django.conf import settings
from django.test.client import Client
from pychargify.api import Chargify
from accounts import CANCELLED_SUBSCRIPTION_STATII

class Dummy(object):
    pass

class TestRewrite(TestCase, QiUnitTestMixin, DestructiveDatabaseTestCase):

    def setUp(self):
        pass

    def test_factory_account_can_be_run_multiple_times(self):
        # for i in range(0,Factory.rand_int(2,6)):
        #     Factory.create_demo_site("test%s" % i, quick=True)

