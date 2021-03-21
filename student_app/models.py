from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Student(models.Model):
    PILIHAN_JENIS_KELAMIN = models.TextChoices(
        'Jenis Kelamin',
        'Laki-laki Perempuan',
    )

    nama_lengkap = models.CharField(max_length=50,)
    nama_panggilan = models.CharField(max_length=10,)
    jenis_kelamin = models.CharField(
        max_length=10,
        choices=PILIHAN_JENIS_KELAMIN.choices,
    )
    tempat_lahir = models.CharField(max_length=10,)
    tanggal_lahir = models.DateField(
        help_text='format "tahun-bulan-tanggal" (Contoh "2000-01-31")',
    )

    alamat_tinggal = models.CharField(max_length=100, blank=True,)
    alamat_kotakab = models.CharField('Alamat Kota/ Kab.', max_length=20, blank=True,)
    nomor_ponsel = models.CharField(max_length=20, blank=True,)
    deskripsi = models.TextField(
        max_length=100,
        help_text='harapan latihan, penyakit, kebiasaan, dll',
        blank=True,
    )

    # KHUSUS STUDENT

    PILIHAN_AFILIASI = models.TextChoices(
        'Afiliasi',
        'Dnurs',
    )

    afiliasi = models.CharField(
        max_length=10,
        choices=PILIHAN_AFILIASI.choices,
        blank=True,
        null=True
    )

    class Meta:
        ordering = ['-nama_lengkap']

    def get_absolute_url(self):
        return reverse('student-app:student-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.nama_lengkap} ({self.nama_panggilan})'

    def usia(self):
        return int((timezone.now().date() - self.tanggal_lahir).days / 365.25)


class Rapor(models.Model):
    order = models.ForeignKey(
        'admin_app.Order',
        on_delete=models.SET_NULL,
        null=True)
    pengenalan_air_1 = models.IntegerField(
        'Pengaturan Nafas',
        blank=True, null=True,
        validators=[MaxValueValidator(10), MinValueValidator(0)])
    pengenalan_air_2 = models.IntegerField(
        'Mengapung Telungkup dan Telentang',
        blank=True, null=True,
        validators=[MaxValueValidator(10), MinValueValidator(0)])
    pengenalan_air_3 = models.IntegerField(
        'Teknik Meluncur',
        blank=True, null=True,
        validators=[MaxValueValidator(10), MinValueValidator(0)])
    gaya_bebas_1 = models.IntegerField(
        'Teknik Kaki dan Pengambilan Nafas',
        blank=True, null=True,
        validators=[MaxValueValidator(10), MinValueValidator(0)])
    gaya_bebas_2 = models.IntegerField(
        'Teknik Tangan dan Pengambilan Nafas',
        blank=True, null=True,
        validators=[MaxValueValidator(10), MinValueValidator(0)])
    gaya_bebas_3 = models.IntegerField(
        'Koordinasi Kaki, Tangan, Nafas',
        blank=True, null=True,
        validators=[MaxValueValidator(10), MinValueValidator(0)])
    gaya_punggung_1 = models.IntegerField(
        'Teknik Kaki dan Pengambilan Nafas',
        blank=True, null=True,
        validators=[MaxValueValidator(10), MinValueValidator(0)])
    gaya_punggung_2 = models.IntegerField(
        'Teknik Tangan dan Pengambilan Nafas',
        blank=True, null=True,
        validators=[MaxValueValidator(10), MinValueValidator(0)])
    gaya_punggung_3 = models.IntegerField(
        'Koordinasi Kaki, Tangan, Nafas',
        blank=True, null=True,
        validators=[MaxValueValidator(10), MinValueValidator(0)])
    gaya_dada_1 = models.IntegerField(
        'Teknik Kaki dan Pengambilan Nafas',
        blank=True, null=True,
        validators=[MaxValueValidator(10), MinValueValidator(0)])
    gaya_dada_2 = models.IntegerField(
        'Teknik Tangan dan Pengambilan Nafas',
        blank=True, null=True,
        validators=[MaxValueValidator(10), MinValueValidator(0)])
    gaya_dada_3 = models.IntegerField(
        'Koordinasi Kaki, Tangan, Nafas',
        blank=True, null=True,
        validators=[MaxValueValidator(10), MinValueValidator(0)])
    gaya_kupu_1 = models.IntegerField(
        'Teknik Kaki dan Pengambilan Nafas',
        blank=True, null=True,
        validators=[MaxValueValidator(10), MinValueValidator(0)])
    gaya_kupu_2 = models.IntegerField(
        'Teknik Tangan dan Pengambilan Nafas',
        blank=True, null=True,
        validators=[MaxValueValidator(10), MinValueValidator(0)])
    gaya_kupu_3 = models.IntegerField(
        'Koordinasi Kaki, Tangan, Nafas',
        blank=True, null=True,
        validators=[MaxValueValidator(10), MinValueValidator(0)])
    komentar = models.TextField(
        max_length=200,
        blank=True)
    waktu_post = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-waktu_post']

    def __str__(self):
        return f'{self.order} | {self.waktu_post}'

    def skor_pengenalan_air(self):
        if self.pengenalan_air_1 or self.pengenalan_air_2 or self.pengenalan_air_3:
            x = [
                self.pengenalan_air_1,
                self.pengenalan_air_2,
                self.pengenalan_air_3
                ]
            y = sum(x)/len(x)
            return round(y, 2)
        else:
            return None

    def skor_gaya_bebas(self):
        if self.gaya_bebas_1 or self.gaya_bebas_2 or self.gaya_bebas_3:
            x = [
                self.gaya_bebas_1,
                self.gaya_bebas_2,
                self.gaya_bebas_3
                ]
            y = sum(x)/len(x)
            return round(y, 2)
        else:
            return None

    def skor_gaya_punggung(self):
        if self.gaya_punggung_1 or self.gaya_punggung_2 or self.gaya_punggung_3:
            x = [
                self.gaya_punggung_1,
                self.gaya_punggung_2,
                self.gaya_punggung_3
                ]
            y = sum(x)/len(x)
            return round(y, 2)
        else:
            return None

    def skor_gaya_dada(self):
        if self.gaya_dada_1 or self.gaya_dada_2 or self.gaya_dada_3:
            x = [
                self.gaya_dada_1,
                self.gaya_dada_2,
                self.gaya_dada_3
                ]
            y = sum(x)/len(x)
            return round(y, 2)
        else:
            return None

    def skor_gaya_kupu(self):
        if self.gaya_kupu_1 or self.gaya_kupu_2 or self.gaya_kupu_3:
            x = [
                self.gaya_kupu_1,
                self.gaya_kupu_2,
                self.gaya_kupu_3
                ]
            y = sum(x)/len(x)
            return round(y, 2)
        else:
            return None
