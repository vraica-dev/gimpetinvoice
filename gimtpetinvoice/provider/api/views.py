from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from provider.models import Provider
from rest_framework.response import Response
from base.core_utils import ProviderVersioning


class ListProviders(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    versioning_class = ProviderVersioning

    def get(self, request, *args, **kwargs):
        version = self.request.version

        if version == 'v1':
            providers = [prov.provider_code for prov in Provider.objects.filter(user=self.request.user)]
        elif version == 'v2':
            providers = [f'{prov.provider_code}-{prov.name}' for prov in Provider.objects.filter(user=self.request.user)]
        else:
            return Response(status=400)
        return Response(providers)