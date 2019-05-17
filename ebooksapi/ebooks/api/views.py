from rest_framework import generics, mixins
from rest_framework.generics import get_object_or_404

from ebooks.models import Ebook, Review
from ebooks.api.serializers import EbookSerializer, ReviewSerializer


class EbookListCreateAPIView(generics.ListCreateAPIView):
    '''
    Class to create an Ebook List API View extending Concrete API View class
    does the same thing as the commented code at the bottom of this file. 
    Of course this is at a higher abstraction level. 

    Minor note - In the Browsable API function provided by Django, the
    HTML Form for various REST HTTP functions is provided because we extended
    from the GenericAPIView class.
    '''
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer


class EbookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    ''' 
    Like EbookListCreateAPIView - using a Concrete API View class. Again
    at a higher abstraction level. Browsing the documentation shows us that
    this concrete view class extends three different mixins and GenericAPIView.
    Has functionalities of GET, PUT, PATCH, DELETE.
    '''
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer


class ReviewCreateAPIView(generics.CreateAPIView):
    # Review Create API View extending from Concrete Create API View class
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        # Overriding the inherited perform_create method 
        ebook_pk = self.kwargs.get('ebook_pk')
        ebook = get_object_or_404(Ebook, pk=ebook_pk)
        serializer.save(ebook=ebook)


class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    # Review detail API View
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    

'''
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
'''