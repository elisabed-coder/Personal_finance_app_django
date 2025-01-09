from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Budget
from .serializers import BudgetSerializer
import logging
from api.models import User

logger = logging.getLogger(__name__)

SALT = "43b1e54d90aaf2e1a6a13a7a7de60f7d"
URL = "http://localhost:5173"

class BudgetChoicesView(APIView):
    def get(self, request):
        return Response({
            'categories': Budget.CATEGORY_CHOICES,
            'theme_colors': Budget.THEME_CHOICES
        })

class BudgetCreateView(APIView):
    def post(self, request, format=None):
        user_email = request.data.get('api_user')

        if not user_email:
            return Response(
                {"success": False, "message": "User email is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        user = User.objects.filter(email__iexact=user_email).first()

        if not user:
            return Response(
                {"success": False, "message": "User not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        try:
            data = {
                "user": user.id,  # Ensure the user instance is passed here
                "category": request.data.get("category"),
                "maximum_spend": request.data.get("maximum_spend"),
                "theme_color": request.data.get("theme_color")
            }

            serializer = BudgetSerializer(data=data)

            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"success": True, "message": "Budget created successfully!"},
                    status=status.HTTP_201_CREATED
                )

            return Response(
                {"success": False, "message": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST
            )

        except Exception as e:
            return Response(
                {"success": False, "message": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class BudgetsView(APIView):
    def get(self, request):
        user_email = request.query_params.get('user_email')  # You can pass the user_email as a query parameter

        if not user_email:
            return Response(
                {"success": False, "message": "User email is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        user = User.objects.filter(email__iexact=user_email).first()
        if not user:
            return Response({"success": False, "message": "User not found"},)

        budgets = Budget.objects.filter(user__id=user.id)
        serializer = BudgetSerializer(budgets, many=True)

        return Response(
            {
                "success": True,
                "budgets": serializer.data
            },
            status=status.HTTP_200_OK
        )




