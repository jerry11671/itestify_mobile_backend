from common.responses import CustomResponse
from .serializers import TextTestimonySerializer
from rest_framework.generics import GenericAPIView
from .permissions import IsAuthenticatedOrReadOnly


class AddTextTestimonyAPIView(GenericAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly,]
    serializer_class = TextTestimonySerializer
    
    def post(self, request):
        user = request.user
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data["uploaded_by"] = user
        serializer.save()
        
        return CustomResponse.success(message="Text testimony added successfully", data=serializer.data, status_code=201)
        
    
    

