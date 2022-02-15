from profile import Profile
from django.shortcuts import render

# Create your views here.
from profileInfo.serializers import (
    ProfileSerializer,
    PortfolioSerializer,
    EducationSerializer,
)
from profileInfo.models import *


def index(request):
    return render(
        request,
        "index.html",
        {
            "profile": ProfileSerializer(Profile.objects.get()).data,
            "educations": EducationSerializer(Education.objects.all(), many=True).data,
            "portfolios": PortfolioSerializer(Portfolio.objects.all(), many=True).data,
        },
    )
