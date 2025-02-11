from django.db import models

class Employee(models.Model):
    employee_id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.employee_id} - {self.name}"
