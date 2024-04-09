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
    read={x for x in Notes.objects.values_list('Readaccess')}

    data = Notes.objects.filter(User=r)
    serializer = Noteserialiser(data, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getanote(request,pk):
    r = request.query_params['user']
    # dataa = Notes.objects.filter(User=r)

    data = Notes.objects.filter(id=pk, User=r)
    if len(data)==0:
        data_by_only_id = Notes.objects.filter(id=pk)
        if len(data_by_only_id)==0:
            return Response("Not a valid note id")
        myread={x for x in data_by_only_id[0].Readaccess if x == str(r)}
        if len(myread)!=0:
            serializer = Noteserialiser(data_by_only_id, many=True)
            return Response(serializer.data)


    serializer = Noteserialiser(data, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def createnote(request):

    serializer = Noteserialiser(data=request.data)
    print(serializer.is_valid(),serializer.errors)
    if request.data['User'] in [None, ""]:
        return Response("User Cannot be null or empty")
    print("We are going to save it")
    read_access_csv = request.data['Readaccess']
    read_access_list = read_access_csv.split(',')
    for i in read_access_list:
        try:
            check=Users.objects.get(id=i)
        except Users.DoesNotExist:
            return Response("User "+i+" does not exist")

    if serializer.is_valid():
        print("yes it is possible to save it")
        serializer.save()
        print("we have saved it")
        return Response(serializer.data)


@api_view(['PUT'])
def updatenote(request,pk):
    r = request.query_params['user']


    try:
        instance=Notes.objects.get(id=pk, User=r)
    except Notes.DoesNotExist:
        return Response("There is no note created by you with noteid ="+pk)
    serializer=Noteserialiser(instance,data=request.data)
    print(serializer.is_valid(),serializer.errors)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

@api_view(['DELETE'])
def deleteanote(request, pk):

    database=Notes.objects.get(id=pk)
    database.delete()
    return Response()