from django.contrib import admin
from student_app.models import Student, Rapor
from import_export.admin import ImportExportModelAdmin

# Register your models here.


@admin.register(Student)
class StudentAdmin(ImportExportModelAdmin):
    list_display = ('__str__', 'nama_lengkap', 'usia')
    exclude = ['afiliasi']


@admin.register(Rapor)
class RaporAdmin(admin.ModelAdmin):
    pass
