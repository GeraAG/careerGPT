from django import forms
from django.core.validators import FileExtensionValidator


class UploadForm(forms.Form):
    pdf_file = forms.FileField(label='Upload PDF File',
                               validators=[FileExtensionValidator(allowed_extensions=['pdf'])],
                               widget=forms.FileInput(attrs={'class': 'w-full border rounded p-2'}))
