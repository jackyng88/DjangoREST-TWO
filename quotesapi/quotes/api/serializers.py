from rest_framework import serializers

from quotes.models import Quote


class QuoteSerializer(serializers.ModelSerializer):
    # Class for the quote serializer

    class Meta:
        model = Quote
        fields = '__all__'