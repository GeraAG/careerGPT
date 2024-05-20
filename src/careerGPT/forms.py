from django import forms
from django.core.validators import FileExtensionValidator


class UploadForm(forms.Form):
    pdf_file = forms.FileField(
        label="",
        validators=[FileExtensionValidator(allowed_extensions=["pdf"])],
    )
