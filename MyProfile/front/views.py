from profile import Profile
from django.shortcuts import render
from front.models import get_value

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
            "skills": get_value("programming_skills"),
            "interests": get_value("interests"),
        },
    )
