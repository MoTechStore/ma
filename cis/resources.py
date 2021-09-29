from import_export import resources
from .models import Moses

class MosesResource(resources.ModelResource):
    class Meta:
        model = Moses