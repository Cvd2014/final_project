from django.db import models
import uuid
from django.conf import settings
from django.utils import timezone
from paypal.standard.forms import PayPalPaymentsForm

# Create your models here.

class Catalogue(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.name

class CatalogueCatagory(models.Model):
    catalogue = models.ForeignKey(Catalogue, related_name='catagories')
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children')
    name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=150)
    description = models.TextField(blank=True)

    def __str__(self):
        if self.parent:
            return '%s: %s-%s' % (self.catalogue.name, self.parent.name, self.name)
        return '%s:%s' % (self.catalogue.name, self.name)




class Product(models.Model):
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='Sales')
    catagory = models.ForeignKey(CatalogueCatagory, related_name='products')
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='product_images', blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    @property
    def paypal_form(self):
        paypal_dict = {
            "business": settings.PAYPAL_RECEIVER_EMAIL,
            "amount": self.price,
            "currency": "USD",
            "item_name": self.name,
            "invoice": "%s=%s" % (self.pk, uuid.uuid4()),
            "notify_url": settings.PAYPAL_NOTIFY_URL,
            "return_url": "%s/paypal-return" % settings.SITE_URL,
            "cancel_return": "%s/paypal-cancel" % settings.SITE_URL
        }

        return PayPalPaymentsForm(initial=paypal_dict)

    def __str__(self):
        return self.name




class ProductDetail(models.Model):
    # used to extend info in product model with specific details
    product = models.ForeignKey(Product, related_name='details')
    attribute = models.ForeignKey('ProductAttribute')
    value = models.CharField(max_length=500)
    description = models.TextField(blank=True)

    def __str__(self):
        return '%s:%s-%s' % (self.product, self.attribute, self.name)


class ProductAttribute(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
