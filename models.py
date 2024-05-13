from django.db import models

class LogEntry(models.Model):
    LEVEL_CHOICES = [
        ('info', 'Info'),
        ('error', 'Error'),
        ('success', 'Success'),
    ]

    level = models.CharField(max_length=10, choices=LEVEL_CHOICES)
    log_string = models.CharField(max_length=255)
    timestamp = models.DateTimeField()
    source = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.timestamp} - {self.log_string} ({self.level})"
