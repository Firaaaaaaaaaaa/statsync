from django.db import models
from django.conf import settings

class BRSExcel(models.Model):
    id_brsexcel = models.AutoField(primary_key=True)
    judul_brs = models.CharField(max_length=250, null=False)
    id_file = models.CharField(max_length=100, null=False)  # Nama file PDF
    url_file = models.CharField(max_length=500, null=False)  # Link Excel di Google Drive
    tgl_terbit = models.DateField(null=False)
    tgl_up = models.DateTimeField(auto_now=True)
    id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.judul_brs

class BRSsheet(models.Model):
    id_brssheet = models.AutoField(primary_key=True)
    id_brsexcel = models.ForeignKey(BRSExcel, on_delete=models.CASCADE)
    judul_sheet = models.CharField(max_length=250, null=False)
    file_sheet = models.CharField(max_length=500, null=False)  # Link ke sheet di Google Drive

    def __str__(self):
        return self.judul_sheet
