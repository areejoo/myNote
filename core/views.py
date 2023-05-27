from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.views import APIView
from .serializer import *
from  .models import *
from rest_framework.response import *
from rest_framework import status


# create Api using class based view
class NoteApi(APIView):
    def get(self, request,*args, **kwargs):
        # get note by id
        #id is sent using url
        try:
            id = request.query_params["id"]
            if id != None:
                is_exists = Note.objects.filter(id=id).exists()
                if is_exists:
                    data = Note.objects.get(id=id)
                    serialize = NoteSerializer(data)
                else:    
                    return Response({'status': status.HTTP_400_BAD_REQUEST, 'data': 'note dose not exists'})
        except:
        # get all  notes 
               data = Note.objects.all()
               serialize = NoteSerializer(data, many=True)
        return Response({'status':status.HTTP_200_OK,'data':serialize.data})


    def post(self, request):
       data=request.data
       serialize=NoteSerializer(data=data)

       if serialize.is_valid():
           serialize.save()
           return Response({'status': status.HTTP_201_CREATED, 'data': 'note added successfuly'})
       else:
            return Response({'status':status.HTTP_500_INTERNAL_SERVER_ERROR,'data':serialize.errors})

           

    #not required in this task
    def put(self, request):
        pass
    # not required in this task
    def patch(self, request):
       pass

    def delete(self, request,*args, **kwargs):
        #id is sent using url
        try:
            id = request.query_params["id"]
            if id != None:
                is_exists = Note.objects.filter(id=id).exists()
                if  is_exists:
                    Note.objects.get(id=id).delete()
                    return Response({'status':status.HTTP_200_OK,'data':'note deleted successfuly'})
        #  if not exists   
                return Response({'status': status.HTTP_400_BAD_REQUEST, 'data': 'note dose not exists'})
        except:
                    return Response({'status': status.HTTP_400_BAD_REQUEST, 'data': 'you must send id of note'})
            


        

        







