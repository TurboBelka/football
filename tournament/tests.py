from datetime import timedelta
from django.test import TestCase, Client
from django.test.utils import setup_test_environment
from django.utils import timezone
from models import Tournament


class CreateTourTests(TestCase):
    def test_check_date_tour(self):
        """
            should create new instance if
            date_end < date_start
        """
        date_start = timezone.now()
        date_end = timezone.now() - timedelta(days=5)
        new_tour = Tournament(date_start=date_start, date_end=date_end)

        self.assertEqual(new_tour.check_date(), False)
