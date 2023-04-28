from.models import jadwal_imsak
from rest_framework import serializers

class jadwal_imsakSerializer(serializers.ModelSerializer):
    class Meta :
        model   = jadwal_imsak
        fields  = ['id','tanggal','imsak','subuh','terbit','duha','zuhur','asar','magrib','isya']