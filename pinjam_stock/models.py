from django.db import models
from accounts.models import User

class jenis_barang(models.Model):
    kode_jenis = models.CharField(max_length=10, unique=True)
    nama_jenis = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.kode_jenis} - {self.nama_jenis}"

class daftar_barang(models.Model):
    jenis = models.ForeignKey(jenis_barang, on_delete=models.CASCADE)
    nama = models.CharField(max_length=255)
    kode_inventaris = models.CharField(max_length=12)
    

    def __str__(self):
        return f"{self.nama}"

class pinjam_barang(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ForeignKey(daftar_barang, on_delete=models.CASCADE)
    keterangan = models.TextField()
    tgl_pinjam = models.DateTimeField(auto_now_add=True)
    tgl_balik = models.DateTimeField(blank=True, null=True)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.items.nama}"