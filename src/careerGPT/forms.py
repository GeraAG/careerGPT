from django import forms
from django.core.validators import FileExtensionValidator


class UploadForm(forms.Form):
    pdf_file = forms.FileField(label='',
                               validators=[FileExtensionValidator(allowed_extensions=['pdf'])],
                               widget=forms.FileInput(attrs={'class': 'w-4/12 block border border-gray-200 shadow-sm rounded-lg text-sm text-gray-500 file:me-4 file:py-2 file:px-4 file:rounded-lg file:border-0 file:text-sm file:font-semibold file:bg-copper-canyon-600 file:text-white hover:file:bg-copper-canyon-700 file:disabled:opacity-50 file:disabled:pointer-events-none dark:text-neutral-500 dark:file:bg-copper-canyon-500 dark:hover:file:bg-copper-canyon-400 m-2'}))
    #w-full border rounded p-2
