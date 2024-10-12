from django.db import models
from django.contrib.auth.models import User

class ServiceRequest(models.Model):
    service_Choices=[
        ('INSTALLATION','Installation'),
        ('MAINTENANCE','Maintenance'),
        ('EMERGENCY','Emergency')
    ]
    customer=models.ForeignKey(User, on_delete=models.CASCADE)
    service_type=models.CharField(max_length=20, choices=service_Choices)
    details=models.TextField()
    attachment=models.FileField(upload_to='attachments/',blank=True, null=True)
    status=models.CharField(max_length=20,default='Pending')
    created_at=models.DateTimeField(auto_now_add=True)
    resolved_at=models.DateTimeField(blank=True, null=True)

    def __str__(self) :
        return f"{self.customer.username}-{self.service_type}-{self.status}"
