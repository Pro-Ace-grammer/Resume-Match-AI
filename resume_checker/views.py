from django.shortcuts import render
from .serializers import JobDescription,JobDescriptionSerializer, Resume,ResumeSerializer
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .analyzer import process_resume


class JobDescriptionAPI(APIView):
    def get(self, request):
        queryset = JobDescription.objects.all()
        serializer = JobDescriptionSerializer(queryset,many=True)
        return Response({
            'status':True,
            'data':serializer.data
        })
    

class AnalyzeResumeAPI(APIView):
    def post(self, request):
        try:
            data = request.data
            print(data)
            if not data.get('job_description'):
                return Response({
                    'status':False,
                    'message':'Job Description is Required',
                    'data':{}
                })
            serializer = ResumeSerializer(data=data)
            if not serializer.is_valid():
                return Response({
                        'status':False,
                        'message':'errors',
                        'data':{serializer.errors}
                    })
            
            serializer.save()
            _data = serializer.data
            resume_instance = Resume.objects.get(id = _data['id'])
            resum_path = resume_instance.resume.path
            data = process_resume(resum_path,
                           JobDescription.objects.get(id=data.get('job_description')).job_description
                           )
            return Response({
                        'status':True,
                        'message':'Resume Analyzed',
                        'data':data
                    })
        except Exception as e:
            return Response({
                'data':False,
            })

