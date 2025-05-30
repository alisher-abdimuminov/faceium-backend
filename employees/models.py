from uuid import uuid4
from django.db import models


GENDER = (
    ("male", "Erkak"),
    ("female", "Ayol")
)

ACCESS_STATUS = (
    ("arrived", "Kelgan"),
    ("late", "Kech qoldi"),
    ("failed", "Failed"),
    ("in_vocation", "Ta'tilda"),
)

OUTPUT_STATUS = (
    ("gone", "Ketgan"),
    ("failed", "Failed"),
)


class Coordinate(models.Model):
    latitude = models.CharField(max_length=20)
    longitude = models.CharField(max_length=20)

    def __str__(self):
        return self.latitude + " " + self.longitude
    

class Area(models.Model):
    name = models.CharField(max_length=100)
    coordinates = models.ManyToManyField(Coordinate, related_name="area_coordinates")

    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=1000)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    

class Employee(models.Model):
    handle = models.CharField(max_length=100)
    uuid = models.CharField(max_length=100, default=uuid4)

    full_name = models.CharField(max_length=1000)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    position = models.CharField(max_length=1000)
    gender = models.CharField(max_length=100, choices=GENDER)
    working_time = models.CharField(max_length=100, default="1", null=True, blank=True)
    birth_date = models.DateField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to="images/employees", null=True, blank=True)

    country = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    town = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=200, default=None, null=True, blank=True)

    active = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name


class AccessControl(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=20, choices=ACCESS_STATUS)
    latitude = models.CharField(max_length=200, null=True, blank=True)
    longitude = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to="image/access_control", null=True, blank=True)

    active = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.status} - {self.employee.full_name} - {self.created}"


class OutputControl(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=20, choices=OUTPUT_STATUS)
    latitude = models.CharField(max_length=20, null=True, blank=True)
    longitude = models.CharField(max_length=20, null=True, blank=True)
    image = models.ImageField(upload_to="image/output_control", null=True, blank=True)

    active = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.status


class Vocation(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    type = models.CharField(max_length=1000, default="Mehnat ta'tili")
    file = models.FileField(upload_to="files/vocations")
    start = models.DateField()
    end = models.DateField()
    active = models.BooleanField(default=True)

    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.start.__str__()
