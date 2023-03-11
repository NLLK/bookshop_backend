from django.db import models
from account.models import User

class ticket_statuses_enum:
    open = 0
    closed = 1

class SupportTicket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tickets_user')
    consultant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='consultant_tickets')
    ticket_status = models.SmallIntegerField(default=ticket_statuses_enum.open)

def user_directory_path(instance, filename):
    return 'ticket_attachments/'+f'{filename}'

class SupportTicketAttachment(models.Model):
    attachment = models.FileField(upload_to=user_directory_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)

class SupportTicketHistory(models.Model):
    support_ticket = models.ForeignKey(SupportTicket, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text_content = models.TextField()
    attachments = models.ManyToManyField(SupportTicketAttachment)
