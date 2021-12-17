from rest_framework import serializers
from .models import studentform


class studentformSerializer(serializers.ModelSerializers):
    class Meta:
        model = studentform
        fields = ["student name", "Email id", "contact number", "Address"]