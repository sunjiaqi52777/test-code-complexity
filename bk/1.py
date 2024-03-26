class Meta:
    fields = (
        "id",
        "surface",
        "usage_2015",
        "usage_2018",
        "couverture_2015",
        "couverture_2018",
    )
    geo_field = "mpoly"
    model = Artificialisee2015to2018