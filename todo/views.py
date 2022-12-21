from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Todo
from .serializers import TodoSerializer

# Create your views here.
class TodoView(viewsets.ModelViewSet):
  
  # queryset = Todo.objects.all()
  # queryset = self.get_queryset()
  serializer_class = TodoSerializer
  authentication_classes = [TokenAuthentication, ]
  permission_classes = [IsAuthenticated, ]
  
  def get_queryset(self):
    user = self.request.user
    print(user)
    queryset = Todo.objects.filter(user=user)
    return queryset
  
    