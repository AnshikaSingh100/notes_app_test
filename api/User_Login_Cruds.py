from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import Userserialiser,Noteserialiser
from modelapp.models import Users,Notes

@api_view(['GET'])
def getallusers(request):
    data = Users.objects.all()
    serializer = Userserialiser(data, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getauser(request,pk):
    data = Users.objects.filter(id=pk)
    serializer = Userserialiser(data, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def createauser(request):
    print(request.data)
    serializer = Userserialiser(data=request.data)

    print("We are going to save it")
    email = request.data['Email']
    password = request.data['Password']
    print("yes")
    if email in [None, ""] or password in [None, ""]:
        return Response("Email/ Password Cannot be null or empty!!")
    elif serializer.is_valid():
        print("yes it is possible to save it")
        serializer.save()
        print("we have saved it")
        return Response(serializer.data)


@api_view(['PUT'])
def updateauser(request,pk):
    instance=Users.objects.get(id=pk)
    serializer=Userserialiser(instance ,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

@api_view(['DELETE'])
def deleteauser(request, pk):

    database=Users.objects.get(id=pk)
    database.delete()
    return Response()