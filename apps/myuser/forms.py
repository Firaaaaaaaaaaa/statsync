from django import forms
from .models import BRSExcel

class PDFUploadForm(forms.Form):
    pdf_file = forms.FileField(label="Upload PDF")
    tgl_terbit = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

class BRSExcelForm(forms.ModelForm):
    class Meta:
        model = BRSExcel
        fields = ['judul_brs', 'tgl_terbit']