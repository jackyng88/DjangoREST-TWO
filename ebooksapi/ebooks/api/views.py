from rest_framework import generics, mixins

from ebooks.models import Ebook
from ebooks.api.serializers import EbookSerializer


class EbookListCreateAPIView(mixins.ListModelMixin,
                             mixins.CreateModelMixin,
                             generics.GenericAPIView):
    # class for creating an Ebook list API View
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer

    def get(self, request, *args, **kwargs):
        # Get method
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # Post method
        return self.create(request, *args, **kwargs)