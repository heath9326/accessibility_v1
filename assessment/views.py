from rest_framework import mixins, viewsets, status
from rest_framework.response import Response


class FrontPageViewSet(viewsets.GenericViewSet):

    def get(self, request, *args, **kwargs):
        return Response(template_name="index.html")

    def post(self, request, *args, **kwargs):
        pass