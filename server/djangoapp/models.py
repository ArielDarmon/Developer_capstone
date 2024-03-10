from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # Other fields as needed

    def __str__(self):
        return self.name  # Return the name as the string representation


class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)  # Many-to-One relationship
    name = models.CharField(max_length=100)
    CAR_TYPES = [
        ('MICROCAR', 'Microcar'),
        ('MINI', 'Minicompact'),
        ('SUPERMINI', 'Supermini'),
        ('COMPACT', 'Compact'),
        ('MIDSIZE', 'Mid-size'),
        ('FULLSIZE', 'Full-size'),
        ('FULLLUX', 'Full-size Luxury'),
        ('SPORTS', 'Sports Car'),
        ('SEDAN', 'Sports Sedan'),
        ('SUPERCAR', 'Supercar/Hypercar'),
        ('SUV', 'SUV'),
        ('CROSSOVER', 'Crossover SUV'),
        ('WAGON', 'Wagon'),
        ('MPV', 'MPV'),
        ('CMPV', 'Compact MPV'),
        ('LMPV', 'Large MPV'),
        ('PREMIEUM', 'Premium Compact'),
        ('LUXURY', 'Luxury Compact'),
        ('EXECUTIVE', 'Executive'),        
        ('CONVERT', 'Converible'),
        ('ROADSTAR', 'Roadster'),
        ('COMPACT', 'Compact'),
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')
    year = models.IntegerField(default=2023,
        validators=[
            MaxValueValidator(2023),
            MinValueValidator(2015)
        ])
    # Other fields as needed

    def __str__(self):
        return self.name  # Return the name as the string representation
