from rest_framework import serializers
from profileInfo.models import Profile, Portfolio, Education


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class PortfolioSerializer(serializers.ModelSerializer):
    created_at = serializers.CharField(source="get_local_date", read_only=True)

    class Meta:
        model = Portfolio
        fields = "__all__"


class EducationSerializer(serializers.ModelSerializer):
    from_date = serializers.CharField(source="get_from_date", read_only=True)
    to_date = serializers.CharField(source="get_to_date", read_only=True)

    class Meta:
        model = Education
        fields = "__all__"
