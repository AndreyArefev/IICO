from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Category
from .serializers import CategorySerializer
from ..iico_api import Iico_API
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer

class SubjectListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class MyOwnView(APIView):
    def get(self, request):
        menu = Iico_API()
        response = menu.all_products_for_frontend
        return Response(response)

'''
def view_menu(request):
    menu = Iico_API()
    response = menu.all_products_for_frontend
    response_JSON = JSONRenderer().render(response)
    print(response_JSON)
    return response_JSON
'''