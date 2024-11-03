from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from provider.models import Provider
from rest_framework.response import Response


class ListProviders(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        providers = [prov.provider_code for prov in Provider.objects.filter(user=self.request.user)]
        return Response(providers)