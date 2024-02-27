from django.forms import ModelForm
from .models import Email


class ContactForm(ModelForm):
    class Meta:
        model = Email
        fields = ["first_name", "last_name", "email_id","subject","text_area"]