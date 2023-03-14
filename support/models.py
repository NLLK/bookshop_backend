from django.db import models
from account.models import User

class SupportTicket(models.Model):

    class TicketChoices(models.IntegerChoices):
        OPEN = 0,
        CLOSED = 1,

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tickets_user')
    consultant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='consultant_tickets')
    ticket_status = models.SmallIntegerField(default=TicketChoices.OPEN, choices=TicketChoices.choices)

    def __str__(self):
        return f'{self.pk}; {self.TicketChoices(self.ticket_status).label};{self.user.pk}-{self.user.last_name}; {self.consultant.pk}-{self.consultant.last_name}'

class SupportTicketAttachment(models.Model):
    attachment = models.FileField(upload_to='ticket_attachments')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.pk}; {self.uploaded_by.pk}-{self.uploaded_by.last_name}'

class SupportTicketHistory(models.Model):
    support_ticket = models.ForeignKey(SupportTicket, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text_content = models.TextField()
    attachments = models.ManyToManyField(SupportTicketAttachment)
    def __str__(self):
        return f'{self.pk}; {self.support_ticket.pk}; {self.user.pk}-{self.user.last_name}'

