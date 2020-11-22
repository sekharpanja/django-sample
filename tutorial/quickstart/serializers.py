from django.contrib.auth.models import User
from rest_framework import serializers
from tutorial.quickstart.models import Bond



class BondSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bond
        fields = ("id", "isin", "size", "currency", "maturity", "lei",)