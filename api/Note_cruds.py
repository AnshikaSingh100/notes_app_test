from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import Userserialiser,Noteserialiser
from modelapp.models import Users,Notes


@api_view(['GET'])
def getallnotes(request):
    try:
        r = request.query_params['user']
    except KeyError as e:
        return Response('No user specified')
    data = Notes.objects.filter(User=r)
    serializer = Noteserialiser(data, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getanote(request,pk):
    r = request.query_params['user']
    # dataa = Notes.objects.filter(User=r)
    data = Notes.objects.filter(id=pk, User=r)
    serializer = Noteserialiser(data, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def createnote(request):


    serializer = Noteserialiser(data=request.data)


    #if request.data['Email'] in [None, ""]:
        #return Response("Email Cannot be null or empty")
    print("We are going to save it")
    if serializer.is_valid():
        print("yes it is possible to save it")
        serializer.save()
        print("we have saved it")
        return Response(serializer.data)


@api_view(['PUT'])
def updatenote(request,pk):
    instance=Notes.objects.get(id=pk)
    serializer=Noteserialiser(instance ,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

@api_view(['DELETE'])
def deleteanote(request, pk):

    database=Notes.objects.get(id=pk)
    database.delete()
    return Response()