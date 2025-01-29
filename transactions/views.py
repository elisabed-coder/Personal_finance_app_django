from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models import User
from transactions.models import Transaction
from transactions.serializers import TransactionSerializer

SALT = "43b1e54d90aaf2e1a6a13a7a7de60f7d"
URL = "http://localhost:5173"


class TransactionsView(APIView):
    def get(self, request):
        user_email = request.query_params.get('user_email')

        if not user_email:
            return Response(
                {"success": False, "message": "User email is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        user = User.objects.filter(email__iexact=user_email).first()
        if not user:
            return Response({"success": False, "message": "User not found"},)

        budgets = Transaction.objects.filter(user=user).order_by('id')

        serializer = TransactionSerializer(budgets, many=True)

        return Response(
            {
                "success": True,
                "budgets": serializer.data
            },
            status=status.HTTP_200_OK
        )
