from django.db import models
from django.urls import reverse

# Create your models here.
from django.utils.translation import gettext as _
from django.utils.text import slugify

class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    discount_price = models.FloatField()
    category = models.CharField(max_length=200)
    desc = models.TextField()
    image = models.CharField(max_length=500)
    slug = models.SlugField(_("slug") , blank=True, null=True)

    

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
       if not self.slug:
           self.slug = slugify(self.title)
       super(Product, self).save(*args, **kwargs) # Call the real save() method


    def get_absolute_url(self):
        return reverse("shop:detail", kwargs={"slug": self.slug})
    



class Order(models.Model):
    items = models.CharField(max_length=1000)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=1000)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    total = models.CharField(max_length=100)

    

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")

    def __str__(self):
        return self.name

