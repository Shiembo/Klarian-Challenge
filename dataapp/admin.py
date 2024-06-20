from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import DataFile, DataEntry
from .resource import DataFileResource, DataEntryResource

@admin.register(DataFile)
class DataFileAdmin(ImportExportModelAdmin):
    resource_class = DataFileResource

@admin.register(DataEntry)
class DataEntryAdmin(ImportExportModelAdmin):
    resource_class = DataEntryResource


