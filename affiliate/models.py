from django.db import models
from model_utils.models import TimeStampedModel


class Customizer(TimeStampedModel):
    IMAGE_SIZE_CHOICE = (
        ('L', 'Large'),
        ('M', 'Medium'),
        ('S', 'Small')
    )
    image_size = models.CharField(
                 max_length=1,
                 choices=IMAGE_SIZE_CHOICE,
                 default='L', blank=True)
    title_length = models.IntegerField(default=-1, blank=True)
    details_length = models.IntegerField(default=-1, blank=True)
    
    class Meta:
        abstract = True
    
    def get_title(self):
        if self.title_length < 0:
            return self.product_title
        elif self.title_length >= 0:
            return self.product_title[:self.title_length] + '...'
    
    def get_details(self):
        if self.details_length < 0:
            return self.product_title
        elif self.details_length >= 0:
            return self.product_details[:self.details_length] + '...'


class Deal(Customizer):
    product_title = models.CharField(max_length=255)
    product_image_link = models.TextField()
    product_shortlink = models.URLField()
    product_price = models.DecimalField(max_digits=5, decimal_places=2)
    product_details = models.TextField()

    def __str__(self):
        return self.product_title
