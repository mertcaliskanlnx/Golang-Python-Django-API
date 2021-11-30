from rest_framework import serializers
from .models import bigdata


#REST_FRAMEWORK SINIFI
class MovieItemSerializers(serializers.ModelSerializer):

    title = serializers.CharField(max_length=255)
    text = serializers.CharField(style={'base_template': 'textarea.html'})
    price = serializers.FloatField(default=1.00)

    class Meta:
        #model.py'daki model
        model = bigdata
        fields = ('__all__')