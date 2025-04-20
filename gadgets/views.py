from rest_framework import generics
from .models import Gadget
from .serializers import GadgetSerializer

class GadgetList(generics.ListAPIView):
    serializer_class = GadgetSerializer

    def get_queryset(self):
        category = self.request.query_params.get('category', None)
        if category:
            return Gadget.objects.filter(category__icontains=category)
        return Gadget.objects.all()

class GadgetDetail(generics.RetrieveAPIView):
    queryset = Gadget.objects.all()
    serializer_class = GadgetSerializer