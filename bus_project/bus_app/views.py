from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def hello_rest_api(request):
    data = {'message': 'Hello, API'}
    return Response(data)

def hello(request):
    return HttpResponse("Hello ,world!")
