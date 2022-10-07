from django.db import models
from django.urls import reverse


# wifi - bool
#
class AddCard(models.Model):
    title = models.CharField(max_length=160)
    description = models.CharField(max_length=300, blank=True)
    content = models.TextField()
    photo = models.ImageField(upload_to='photo/%Y/%m/%d')

    grade = models.FloatField(blank=True, null=True)
    published = models.DateField(auto_now_add=True)
    price = models.IntegerField()
    wifi = models.BooleanField(default=False)
    pool = models.BooleanField(default=False)
    parking = models.BooleanField(default=False)
    city = models.ForeignKey('city', on_delete=models.DO_NOTHING, null=True)

    def get_absolute_url(self):
        return reverse('show_card', kwargs={'card_id': self.pk})

    def __str__(self):
        return self.title


class city(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Місто')
