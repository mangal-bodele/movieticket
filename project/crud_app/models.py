from django.db import models

class MovieTicket(models.Model):
    SEAT=[('F','Front'),('Mid','Middle'),('BAL','Balcony')]
    name = models.CharField(max_length=10)
    movie = models.CharField(max_length=10)
    multiplex = models.CharField(max_length=10)
    date = models.DateTimeField(auto_now_add=True)
    no_seat= models.IntegerField()
    seat_type = models.CharField(max_length=5,choices=SEAT)
    mobile = models.IntegerField()





