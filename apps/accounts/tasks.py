from celery import shared_task
from .models import VerificationCode
from django.template.loader import render_to_string
from config.settings.base import APP
from apps.utils.email import send_email
from datetime import timedelta
from apps.users.models import User


@shared_task
def remove_verification_code(id):
    try:
        VerificationCode.objects.get(id=id).delete()
    except VerificationCode.DoesNotExist:
        return False
    return True


@shared_task
def send_verification_email(email: str):
    code_obj, user = get_verification_code(email)
    if code_obj and user:
        subject = f"{APP.name} - Verification Code"
        context = {
            "name": user.name,
            "app_name": APP.name,
            "code": code_obj.code,
        }
        html_message = render_to_string(
            "email/send_verification_code.html", context=context
        )
    return send_email(subject, [email], html_message)


@shared_task
def send_code_reset_password(email: str):
    code_obj, user = get_verification_code(email)
    if code_obj and user:
        subject = f"{APP.name} - Code Reset Password"
        context = {
            "name": user.name,
            "app_name": APP.name,
            "code": code_obj.code,
        }
        html_message = render_to_string(
            "email/send_code_reset_password.html", context=context
        )
        send_email(subject, [email], html_message)
        return True
    return False


def get_verification_code(email: str):
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return False, False

    code_obj, created = VerificationCode.objects.get_or_create(user=user)
    if created:
        remove_verification_code.apply_async(
            args=[code_obj.id], countdown=timedelta(minutes=10).seconds
        )

    return code_obj, user
