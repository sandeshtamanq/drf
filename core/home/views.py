from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Person
from .serializers import LoginSerializer, PersonSerializer

# Create your views here.


# Class based view
class PersonView(APIView):
    def get(self, request):
        objs = Person.objects.filter(color__isnull=False)
        serializer = PersonSerializer(objs, many=True)

        return Response({"data": serializer.data})

    def post(self, request):
        data = request.data
        print(data)
        serializer = PersonSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response({"error": serializer.errors})

    def patch(self, request):
        data = request.data
        objs = Person.objects.get(id=id)
        serializer = PersonSerializer(objs, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data})
        return Response({"error": serializer.errors})
        pass

    def put(self, request):
        data = request.data
        serializer = PersonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data})
        return Response({"error": serializer.errors})

    def delete(self, request):
        obj = Person.objects.get(id=id)
        obj.delete()
        return Response({"message": "Person deleted successfully"})


# Function based view
@api_view(["POST"])
def login(request):
    data = request.data
    serializers = LoginSerializer(data=data)

    if serializers.is_valid():
        data = serializers.validated_data
        print(data)
        return Response({"message": "Sup"})

    return Response(serializers.errors)


@api_view(["GET", "POST", "PATCH"])
def index(request):
    courses = {
        "course_name": "python",
        "learn": ["Django", "flask", "tornado"],
        "course_provider": "Sandesh Tamang",
    }

    if request.method == "GET":
        return Response({"Test": "It works"})
    elif request.method == "POST":
        return Response(courses)
    elif request.method == "PATCH":
        pass


@api_view(["GET", "POST", "PUT", "PATCH"])
def people(request):
    if request.method == "GET":
        objs = Person.objects.filter(color__isnull=False)
        serializer = PersonSerializer(objs, many=True)

        return Response({"data": serializer.data})

    elif request.method == "POST":
        print("here")
        data = request.data
        serializer = PersonSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response({"error": serializer.errors})


@api_view(["PUT", "PATCH", "DELETE"])
def single_people(request, id):
    data = request.data
    if request.method == "PUT":
        serializer = PersonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data})
        return Response({"error": serializer.errors})
    elif request.method == "PATCH":
        objs = Person.objects.get(id=id)
        serializer = PersonSerializer(objs, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data})
        return Response({"error": serializer.errors})
    else:
        obj = Person.objects.get(id=id)
        obj.delete()
        return Response({"message": "Person deleted successfully"})


class PeopleViewSet(viewsets.ModelViewSet):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = PersonSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response({"error": serializer.errors})
