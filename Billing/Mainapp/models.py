from django.db import models


class Inventory(models.Model):
    Rs2000          = models.IntegerField(default = 0)
    Rs500           = models.IntegerField(default = 0)
    Rs100           = models.IntegerField(default = 0)
    Rs50            = models.IntegerField(default = 0)
    Rs20            = models.IntegerField(default = 0)
    Rs10            = models.IntegerField(default = 0)
    Rs5             = models.IntegerField(default = 0)
    Rs2             = models.IntegerField(default = 0)
    Rs1             = models.IntegerField(default = 0)
    created         = models.DateTimeField(auto_now = True)
    updated         = models.DateTimeField(auto_now = True)

    def __str__(self):
        return "%d " % (self.id)


class BillDetails(models.Model):
    bill            = models.IntegerField(default = 0)
    paid            = models.IntegerField(default = 0)
    change          = models.IntegerField(default = 0)
    Rs2000          = models.IntegerField(default = 0)
    Rs500           = models.IntegerField(default = 0)
    Rs100           = models.IntegerField(default = 0)
    Rs50            = models.IntegerField(default = 0)
    Rs20            = models.IntegerField(default = 0)
    Rs10            = models.IntegerField(default = 0)
    Rs5             = models.IntegerField(default = 0)
    Rs2             = models.IntegerField(default = 0)
    Rs1             = models.IntegerField(default = 0)
    created         = models.DateTimeField(auto_now = True)

    def __str__(self):
        return "%d " % (self.id)
