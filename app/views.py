from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

import app.models as models
import app.serializers as serializers


class FactsViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = models.Fact.objects.all()
        serializer = serializers.FactSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = models.Fact.objects.all()
        fact = get_object_or_404(queryset, pk=pk)
        serializer = serializers.FactSerializer(fact)
        return Response(serializer.data)
