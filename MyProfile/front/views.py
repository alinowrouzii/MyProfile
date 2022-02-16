from django.shortcuts import render
from front.models import get_value

# Create your views here.
from profileInfo.serializers import (
    ProfileSerializer,
    PortfolioSerializer,
    EducationSerializer,
)
from profileInfo.models import Education, Profile, Portfolio


def index(request):
    try:
        return render(
            request,
            "index.html",
            {
                "profile": ProfileSerializer(Profile.objects.get()).data,
                "educations": EducationSerializer(
                    Education.objects.all(), many=True
                ).data,
                "portfolios": PortfolioSerializer(
                    Portfolio.objects.all(), many=True
                ).data,
                "skills": get_value("programming_skills"),
                "interests": get_value("interests"),
            },
        )
    except Exception:
        return render(request, "404.html", {})
