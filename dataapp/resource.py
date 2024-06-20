from import_export import resources
from .models import DataFile, DataEntry

class DataFileResource(resources.ModelResource):
    class Meta:
        model = DataFile

class DataEntryResource(resources.ModelResource):
    class Meta:
        model = DataEntry
