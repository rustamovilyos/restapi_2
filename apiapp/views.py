from .models import Member
from .serializers import MemberSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics, mixins
from rest_framework import viewsets

"""# THIS IS FIRST
class MemberList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class MemberDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)
"""

# NEXT STEP
"""
class MemberList(generics.ListCreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class MemberDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    """


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer