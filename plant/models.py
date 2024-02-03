from django.db import models
from category.models import Category
# from django.core.validators import MaxValueValidator
# , validators=[MaxValueValidator(999)]
class Plant (models.Model):
    categories = models.ManyToManyField(Category)

    image = models.ImageField(upload_to='plant/media/')
    name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    description = models.TextField()

    def __str__(self):
        return self.name


# class Profile(models.Model):
#     account = models.OneToOneField(UserAccount, on_delete=models.CASCADE, null= True, blank= True)
    
#     def __str__(self):
#         return f"Profile: {self.account}"