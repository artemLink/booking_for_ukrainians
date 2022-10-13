from django.db import models
from django.urls import reverse


class AddCard(models.Model):
    title = models.CharField(max_length=160)
    description = models.CharField(max_length=300, blank=True)
    content = models.TextField()
    photo = models.ImageField(upload_to='photo/%Y/%m/%d')
    grade = models.FloatField(blank=True, null=True)
    published = models.DateField(auto_now_add=True)
    is_publish = models.BooleanField(default=False)
    price = models.IntegerField()
    wifi = models.BooleanField(default=False)
    pool = models.BooleanField(default=False)
    parking = models.BooleanField(default=False)
    city = models.CharField(max_length=100)
    adress = models.CharField(max_length=400)
    single_rooms = models.IntegerField()
    double_rooms = models.IntegerField()

    def get_absolute_url(self):
        return reverse('show_card', kwargs={'card_id': self.pk})

    def __str__(self):
        return self.title


class rent_rooms(models.Model):
    day_from = models.DateField(blank=True)
    day_to = models.DateField(blank=True)
    rent_room_id = models.IntegerField()
    type_rent_room = models.IntegerField()
