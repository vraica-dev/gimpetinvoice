from rest_framework.versioning import URLPathVersioning


class CustomVersioning(URLPathVersioning):
    allowed_versions = ['v1']
    version_param = 'version'


class ProviderVersioning(CustomVersioning):
    allowed_versions = ['v1', 'v2']

class InvoicingVersioning(CustomVersioning):
    allowed_versions = ['v1']