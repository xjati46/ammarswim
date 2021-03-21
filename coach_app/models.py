from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Coach(models.Model):
    PILIHAN_JENIS_KELAMIN = models.TextChoices(
        'Jenis Kelamin',
        'Laki-laki Perempuan',
    )

    user = models.OneToOneField(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    nama_lengkap = models.CharField(max_length=50,)
    nama_panggilan = models.CharField(max_length=10,)
    jenis_kelamin = models.CharField(
        max_length=10,
        choices=PILIHAN_JENIS_KELAMIN.choices,
    )
    tempat_lahir = models.CharField(
        max_length=10,
        )
    tanggal_lahir = models.DateField(
        help_text='format "tahun-bulan-tanggal" (Contoh "2000-01-31")',
    )

    nomor_ktp = models.CharField(
        max_length=20,
        blank=True,
        )
    alamat_tinggal = models.CharField(
        max_length=100,
        blank=True,
        )
    alamat_kotakab = models.CharField(
        'Alamat Kota/ Kab.', 
        max_length=20,
        blank=True,
        )
    nomor_ponsel = models.CharField(
        max_length=20,
        blank=True,
        )
    nama_bank = models.CharField(
        max_length=20,
        help_text='Diutamakan Bank Mandiri',
        blank=True,
    )
    nomor_rekening = models.CharField(
        max_length=30, 
        blank=True,
        )
    deskripsi = models.TextField(
        max_length=100,
        help_text='latar belakang, pendidikan, keahlian',
        blank=True,
    )

    class Meta:
        ordering = ['nama_panggilan']

    def __str__(self):
        return f'Coach {self.nama_panggilan}'

    def usia(self):
        return int((timezone.now().date() - self.tanggal_lahir).days / 365.25)
