from django.db import models

class Module(models.Model):
    name = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=20, choices=[
        ('installed', 'Installed'),
        ('not_installed', 'Not Installed'),
    ])
    installed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Module'
