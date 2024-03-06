class Renaturee2018to2015Serializer(serializers.GeoFeatureModelSerializer):
    usage_2015 = s.SerializerMethodField()
    usage_2018 = s.SerializerMethodField()
    couverture_2015 = s.SerializerMethodField()
    couverture_2018 = s.SerializerMethodField()

    def get_usage_2015(self, obj):
        return get_label(code=obj.us_2015, label=obj.us_2015_label)

    def get_usage_2018(self, obj):
        return get_label(code=obj.us_2018, label=obj.us_2018_label)

    def get_couverture_2015(self, obj):
        return get_label(code=obj.cs_2015, label=obj.cs_2015_label)

    def get_couverture_2018(self, obj):
        return get_label(code=obj.cs_2018, label=obj.cs_2018_label)

    class Meta:
        fields = (
            "id",
            "surface",
            "",
            "",
            "",
            "",
        )
        geo_field = "mpoly"
        model = Renaturee2018to2015

