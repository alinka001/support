from django.db import models

from users.models import User


class Ticket(models.Model):
    STATUS_CHOICES = (
        ('new', 'New'),
        ('done', 'Done')
    )
    author = models.ForeignKey(User, max_length=50, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    message = models.CharField(max_length=200)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(unique=True, primary_key=True, editable=False)
    def __str__(self):
        return self.description


class Answer(models.Model):

    ticket_id = models.OneToOneField(Ticket, on_delete=models.CASCADE, unique=True)
    answer = models.TextField(max_length=500)

    def __str__(self):
        return self.answer


class Feedback(models.Model):

    answer_id = models.OneToOneField(Answer, on_delete=models.CASCADE, unique=True)
    feedback = models.TextField(max_length=500)

    def __str__(self):
        return self.feedback