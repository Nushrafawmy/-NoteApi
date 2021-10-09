from django.shortcuts import render
from note.models import Note
from note.serializers import NoteSerializers
from rest_framework.views import APIView
from django.http.response import Http404, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

class NoteList(APIView):
    def get(self,request,format= None):
        notes= Note.objects.all()
        note_serializer= NoteSerializers(notes,many =True)
        return JsonResponse(note_serializer.data,safe=False)


    def post(self,request,format= None):
        note_data  =JSONParser().parse(request)
        note_serializer = NoteSerializers(data= note_data)    
        if note_serializer.is_valid():
            note_serializer.save()
            return JsonResponse(note_serializer.data,status= status.HTTP_201_CREATED)
        return JsonResponse(note_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NoteDetail(APIView):
    def get_object(self,pk):
        try:
            return Note.objects.get(pk=pk)

        except Note.DoesNotExist:
            return JsonResponse({'message':'The Note does not exist'},status= status.HTTP_404_NOT_FOUND)


    def get(self,request,pk,format= None):
        note_obj = self.get_object(pk)
        note_serializer  =NoteSerializers(note_obj)
        return JsonResponse(note_serializer.data,safe=False)



    def put(self,request,pk,format= None):
        note_obj = self.get_object(pk)
        note_serializer  =NoteSerializers(note_obj,data=request.data)
        if note_serializer.is_valid():
            note_serializer.save()
            return JsonResponse(note_serializer.data) 
        return JsonResponse(note_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


    
    def patch(self,request,pk,format= None):
        note_obj = self.get_object(pk)
        note_serializer = NoteSerializers(note_obj,data=request.data,partial = True)
        if note_serializer.is_valid():
            note_serializer.save()
            return JsonResponse(note_serializer.data) 
        return JsonResponse(note_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    def delete(self, request, pk, format=None):
        note_obj = self.get_object(pk)
        note_obj.delete()
        return JsonResponse({'message': 'Note was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
