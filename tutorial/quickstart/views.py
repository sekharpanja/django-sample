from rest_framework.generics import ListCreateAPIView

from tutorial.quickstart.models import Bond
from tutorial.quickstart.serializers import BondSerializer


class BondListCreateAPIView(ListCreateAPIView):
    serializer_class = BondSerializer

    def get_queryset(self):
        return Bond.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
