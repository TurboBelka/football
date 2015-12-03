from datetime import timedelta
from django.core.urlresolvers import reverse_lazy
from django.test import TestCase
from django.utils import timezone
from teams.models import Team
from tournament.models import Tournament


class AllToursViewTest(TestCase):
    def test_view_with_no_tours(self):
        response = self.client.get(reverse_lazy('teams:teams'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['tours'], [])

    def test_view_with_tours_gt_date_end(self):
        date_start = timezone.now()
        date_end = timezone.now() - timedelta(days=5)
        new_tour = Tournament.objects.create(date_start=date_start, date_end=date_end,
                              name='tour1', mode=1)
        response = self.client.get(reverse_lazy('teams:teams'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['tours'], ['<Tournament: Tournament object>'])
        # self.assertQuerysetEqual(response.context['tours'], [])

    def test_team_in_tour(self):
        team = Team.objects.create()
