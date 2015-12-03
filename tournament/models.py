from django.db import models


class Tournament(models.Model):
    MODE_TOUR = (
        (1, 'finished'),
        (2, 'current'),
        (3, 'not_started'),
        (4, 'voted'),
    )

    mode = models.SmallIntegerField(choices=MODE_TOUR)
    name = models.CharField(max_length=200)
    date_start = models.DateField()
    date_end = models.DateField()

    def check_date(self):
        if self.date_end > self.date_start:
            return True
        else:
            return False