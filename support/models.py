from django.db import models
from account.models import User

class ticket_statuses_enum:
    open = 0
    closed = 1

class SupportTicket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tickets_user')
    consultant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='consultant_tickets')
    ticket_status = models.SmallIntegerField(default=ticket_statuses_enum.open)

class SupportTicketHistory(models.Model):
    support_ticket = models.ForeignKey(SupportTicket, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text_content = models.TextField()

class SupportTicketAttachment(models.Model):
    support_ticket = models.ForeignKey(SupportTicket, on_delete=models.CASCADE)
    attachment = models.FileField(upload_to='ticket_attachments')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
