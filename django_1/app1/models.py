from django.db import models
from  django.urls import reverse
class Izoh_011(models.Model):
    mavzusi=models.CharField(max_length=100)
    izohi=models.TextField()
    def __repr__(self):
        return self.mavzusi
class Izoh(models.Model):
    mavzusi=models.CharField(max_length=100)
    izohi=models.TextField()
    def __repr__(self):
        return self.mavzusi
class Muzqaymoqlar(models.Model):
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=6,decimal_places=2)
    turi=models.CharField(max_length=100)
    ishlab_ch_sana=models.DateTimeField()
    yaroqlilik_muddati=models.DateTimeField()
    sqladdagi_soni=models.IntegerField(blank=True, null=True)
    def __str__(self):
        return self.name
class Hodimlar_00(models.Model):
    ism=models.CharField(max_length=100)
    familiya=models.CharField(max_length=100)
    tel_raqam=models.CharField(max_length=100)
    ish_boshlagan_sana=models.DateTimeField()
    ishlagan_kunlar_soni=models.DecimalField(max_digits=10000,decimal_places=0)
    belgilangan_narx=models.IntegerField(blank=True, null=True)
    karta=models.CharField(max_length=100)
    Bank_Tranzit=models.CharField(max_length=100)
    bank_mfo=models.CharField(max_length=100)
    def __repr__(self):
        return self.ism
    def get_absolute_url(self):
        return reverse('hodim')
