from django.db import models
from django.utils import timezone
from coach_app.models import Coach
from student_app.models import Student

# Create your models here.


class Product(models.Model):
    nama_produk = models.CharField(max_length=50)
    jumlah_siswa = models.IntegerField()
    jumlah_pertemuan = models.IntegerField()
    harga = models.IntegerField()
    fee_pelatih = models.IntegerField(null=True)

    class Meta:
        ordering = ['nama_produk']

    def __str__(self):
        return self.nama_produk


class Order(models.Model):
    PILIHAN_JENIS_ORDER = (
        ('p', 'Privat'),
        ('k', 'Kelas')
    )

    student = models.ForeignKey(Student,on_delete=models.SET_NULL,null=True)
    coach = models.ForeignKey(Coach, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    jenis_order = models.CharField(
        max_length=1,
        choices=PILIHAN_JENIS_ORDER,
        default='p',
    )

    diskon = models.FloatField(blank=True, null=True)

    tanggal_transaksi = models.DateField()
    tanggal_expired = models.DateField()

    arsip = models.BooleanField(default=False)

    p1 = models.DateField('Pertemuan 1', null=True, blank=True)
    p2 = models.DateField('Pertemuan 2', null=True, blank=True)
    p3 = models.DateField('Pertemuan 3', null=True, blank=True)
    p4 = models.DateField('Pertemuan 4', null=True, blank=True)
    p5 = models.DateField('Pertemuan 5', null=True, blank=True)
    p6 = models.DateField('Pertemuan 6', null=True, blank=True)
    p7 = models.DateField('Pertemuan 7', null=True, blank=True)
    p8 = models.DateField('Pertemuan 8', null=True, blank=True)

    p1_c = models.BooleanField(default=False)
    p2_c = models.BooleanField(default=False)
    p3_c = models.BooleanField(default=False)
    p4_c = models.BooleanField(default=False)
    p5_c = models.BooleanField(default=False)
    p6_c = models.BooleanField(default=False)
    p7_c = models.BooleanField(default=False)
    p8_c = models.BooleanField(default=False)

    p1_a = models.BooleanField(default=False)
    p2_a = models.BooleanField(default=False)
    p3_a = models.BooleanField(default=False)
    p4_a = models.BooleanField(default=False)
    p5_a = models.BooleanField(default=False)
    p6_a = models.BooleanField(default=False)
    p7_a = models.BooleanField(default=False)
    p8_a = models.BooleanField(default=False)

    class Meta:
        ordering = ['student']

    def __str__(self):
        return f'{self.id}/{self.student.nama_panggilan}'

    def is_expired(self):
        if self.tanggal_expired < timezone.now().date():
            return "✘EXPIRED"
        else:
            return ""

    def bill(self):
        x = 0
        if self.diskon:
            x = (1 - self.diskon) * self.product.harga
            return int(x)
        return int(self.product.harga)

    def p_total(self):
        count = 0
        if self.p1:
            count += 1
        if self.p2:
            count += 1
        if self.p3:
            count += 1
        if self.p4:
            count += 1
        if self.p5:
            count += 1
        if self.p6:
            count += 1
        if self.p7:
            count += 1
        if self.p8:
            count += 1
        return count

    def p_c_total(self):
        count = 0
        if self.p1_c:
            count += 1
        if self.p2_c:
            count += 1
        if self.p3_c:
            count += 1
        if self.p4_c:
            count += 1
        if self.p5_c:
            count += 1
        if self.p6_c:
            count += 1
        if self.p7_c:
            count += 1
        if self.p8_c:
            count += 1
        return count

    def margin_p_c(self):
        x = int(self.p_total())
        y = int(self.p_c_total())
        if x != y:
            return x-y
        else:
            return ''

    def income_coach_normal(self):
        return int(self.p_c_total() * self.product.fee_pelatih)

    def potential_income_coach_normal(self):
        return int(
            (self.product.jumlah_pertemuan - self.p_c_total())
            * self.product.fee_pelatih
            )

    def p_status(self):
        if self.p_total() >= self.product.jumlah_pertemuan:
            return "✘SELESAI"
        else:
            return ""

    def income_coach_actual_normal(self):
        return self.margin_p_c() * self.product.fee_pelatih

    # def share_dnurs(self):
    #     x = self.bill() * 0.2
    #     return int(x)

    # def share_maestro(self):
    #     x = self.bill() * 0.8
    #     return int(x)

    # def coach_share(self):
    #     x = self.coach.bagi_hasil * self.bill()
    #     y = self.product.jumlah_pertemuan
    #     return int(x/y)

    # def coach_share_dnurs(self):
    #     x = int(self.coach.bagi_hasil * self.share_maestro())
    #     y = self.product.jumlah_pertemuan
    #     return int(x/y)


    # def p_a_total(self):
    #     count = 0
    #     if self.p1_a:
    #         count += 1
    #     if self.p2_a:
    #         count += 1
    #     if self.p3_a:
    #         count += 1
    #     if self.p4_a:
    #         count += 1
    #     if self.p5_a:
    #         count += 1
    #     if self.p6_a:
    #         count += 1
    #     if self.p7_a:
    #         count += 1
    #     if self.p8_a:
    #         count += 1
    #     return count

    # def margin_p_a(self):
    #     x = int(self.p_total())
    #     y = int(self.p_a_total())
    #     if x != y:
    #         return x-y
    #     else:
    #         return ''

    # def income_coach_normal(self):
    #     return int(self.p_c_total() * self.coach_share())

    # def income_coach_dnurs(self):
    #     return int(self.p_c_total() * self.coach_share_dnurs())

    # def potential_income_coach_normal(self):
    #     return int(
    #         (self.product.jumlah_pertemuan - self.p_c_total())
    #         * self.coach_share()
    #         )

    # def potential_income_coach_dnurs(self):
    #     return int(
    #         (self.product.jumlah_pertemuan - self.p_c_total())
    #         * self.coach_share_dnurs()
    #         )

    # def income_coach_actual_normal(self):
    #     return self.margin_p_a() * self.coach_share()

    # def income_coach_actual_dnurs(self):
    #     return self.margin_p_a() * self.coach_share_dnurs()