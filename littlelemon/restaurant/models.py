from django.db import models

# BookingTable Model
class Booking(models.Model):
    id = models.AutoField(primary_key=True)  # Automatically generates a unique ID
    name = models.CharField(max_length=255)  # Name field with max length 255
    no_of_guests = models.IntegerField()  # Number of guests, with an integer constraint
    booking_date = models.DateTimeField()  # Date and time of booking

    def __str__(self):
        return f"{self.name} - {self.booking_date}"


# MenuTable Model
class Menu(models.Model):
    id = models.AutoField(primary_key=True)  # Automatically generates a unique ID
    title = models.CharField(max_length=255)  # Title of the menu item
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price with up to 10 digits, 2 decimal places
    inventory = models.IntegerField()  # Inventory count with integer constraint

    def __str__(self):
        return f"{self.title} - ${self.price}"
