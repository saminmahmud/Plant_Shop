from django.db import models
from account.models import UserAccount
from plant.models import Plant

STATUS = [
    ('Completed', 'Completed'),
    ('Pending', 'Pending'),
]

class Order(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    status = models.CharField(choices = STATUS, max_length = 10, default = "Pending")

    def __str__(self):
        return str(self.user.username)


