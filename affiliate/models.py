from django.db import models
from model_utils.models import TimeStampedModel


class Deal(TimeStampedModel):
    product_title = models.CharField(max_length=255)
    product_image_link = models.TextField()
    product_shortlink = models.URLField()
    product_price = models.DecimalField(max_digits=5, decimal_places=2)
    product_details = models.TextField()

    def __str__(self):
        return self.product_title
