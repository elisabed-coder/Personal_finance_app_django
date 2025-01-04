from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Budget
from .serializers import BudgetSerializer


class BudgetChoicesView(APIView):
    def get(self, request):
        return Response({
            'categories': Budget.CATEGORY_CHOICES,
            'theme_colors': Budget.THEME_CHOICES
        })
class BudgetCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        data = {
            "user": request.user.id,
            "category": request.data["category"],
            "maximum_spend": request.data["maximum_spend"],
            "theme_color": request.data["theme"]
        }
        serializer = BudgetSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"success": True, "message": "Budget created successfully!"},
                status=status.HTTP_201_CREATED,
            )
        else:
            error_msg = ""
            for key in serializer.errors:
                error_msg += serializer.errors[key][0]
            return Response(
                {"success": False, "message": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )
