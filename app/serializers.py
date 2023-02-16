from rest_framework import serializers

import app.models as models


class FactSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Fact
        fields = ('fact_title',)
