from django.db import models
from taggit.managers import TaggableManager
from django.urls import reverse
from django.contrib.auth.models import User


class City(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('explorer:places_list_by_category', args=[self.slug])


class Address(models.Model):
    street = models.CharField(max_length=60)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    location_number = models.CharField(max_length=10, blank=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=8, null=True, blank=True)
    length = models.DecimalField(max_digits=11, decimal_places=8, null=True, blank=True)

    def __str__(self):
        address = (self.street, self.location_number, self.city.name)
        return ' '.join(address)


class Place(models.Model):
    name = models.CharField(max_length=60)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    category = models.ForeignKey(Category, related_name='places', on_delete=models.CASCADE)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images/%Y/%m/%d', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True)
    sum_of_rating = models.DecimalField(max_digits=9, decimal_places=2, default=5)
    num_of_ratings = models.IntegerField(default=1)
    tags = TaggableManager()

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('explorer:place_detail', args=[self.id, self.slug])


class Comment(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    rate = models.IntegerField()