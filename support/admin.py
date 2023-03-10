from django.contrib import admin
from support import models

admin.site.register(models.SupportTicket)
admin.site.register(models.SupportTicketAttachment)
admin.site.register(models.SupportTicketHistory)
