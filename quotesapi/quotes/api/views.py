from rest_framework import generics, mixins, permissions
from rest_framework.generics import get_object_or_404

from quotes.models import Quote
from quotes.api.serializers import QuoteSerializer
from quotes.api.permissions import IsAdminUserOrReadOnly


class QuoteListCreateAPIView(generics.ListCreateAPIView):
    # Quote List Create API View

    queryset = Quote.objects.all().order_by('-id')
    serializer_class = QuoteSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class QuoteDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    # Quote Detail API View

    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    permission_classes = [IsAdminUserOrReadOnly]