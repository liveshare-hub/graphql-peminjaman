from django.contrib import admin

from .models import jenis_barang, daftar_barang, pinjam_barang

admin.site.register(jenis_barang)
admin.site.register(daftar_barang)
admin.site.register(pinjam_barang)
