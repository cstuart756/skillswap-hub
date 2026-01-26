from django.conf import settings
from django.db import models
from django.db.models import Q

from skills.models import Skill


class ExchangeRequest(models.Model):
    class Status(models.TextChoices):
        PENDING = "pending", "Pending"
        ACCEPTED = "accepted", "Accepted"
        REJECTED = "rejected", "Rejected"
        CANCELLED = "cancelled", "Cancelled"

    skill = models.ForeignKey(
        Skill,
        on_delete=models.CASCADE,
        related_name="exchange_requests",
    )
    requester = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="exchange_requests",
    )
    status = models.CharField(
        max_length=12,
        choices=Status.choices,
        default=Status.PENDING,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["requester", "skill"],
                condition=Q(status="pending"),
                name="uniq_pending_exchange_request_per_requester_skill",
            )
        ]

    def __str__(self) -> str:
        return f"{self.requester} -> {self.skill} ({self.status})"
