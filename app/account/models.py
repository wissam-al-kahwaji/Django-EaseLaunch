from django.db import models
from django.utils.translation import gettext_lazy as _
from octo.utils.generate import generate_key, generate_code
from django.contrib.auth import get_user_model

User = get_user_model()


class VerificationCode(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="code_verified"
    )
    code = models.CharField(_("Code"), max_length=6, blank=True)
    key = models.CharField(_("Key"), max_length=40, blank=True)
    created = models.DateTimeField(_("The time it was created"), auto_now_add=True)

    class Meta:
        ordering = ["-created", "user"]
        indexes = [
            models.Index(fields=["user"]),
        ]

    def save(self, *args, **kwargs):
        self.key = generate_key()
        self.code = generate_code()
        return super().save(*args, **kwargs)
