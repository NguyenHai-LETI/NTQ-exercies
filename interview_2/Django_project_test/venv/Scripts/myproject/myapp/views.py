from django.http import JsonResponse, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Item
from .serializers import ItemSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.decorators import action
from rest_framework import status


# Home
def home(request):
    return HttpResponse("""
    <h1>Welcome to Django Project</h1>
    <p>Public endpoints:</p>
    <ul>
        <li><a href="/admin/">Admin Panel</a></li>
        <li><a href="/api/items/">Items API (FBV - Read Only)</a></li>
        <li><a href="/api/items-api/">Items API (CBV - Read Only)</a></li>
        <li><a href="/api/items/1/">Item Detail (CBV - Read/Write)</a></li>
        <li><a href="/api/public-items/">Public Items API</a></li>
        
    </ul>
    <p>Private endpoints:</p>
    <ul>
        <li>POST /api/auth/register/ - User Registration</li>
        <li>POST /api/auth/login/ - User Login</li>
        <li>GET POST /api/api/items/ - Get/add items</li>
    </ul>
    <h3>Cách sử dụng:</h3>
    <ol>
        <li>Register: POST /api/auth/register/ with {"username": "test", "password": "test123"}</li>
        <li>Login: POST /api/auth/login/ with {"username": "test", "password": "test123"}</li>
        <li>Sử dụng token trong Authorization header: "Bearer &lt;token&gt;"</li>
    </ol>
    """)


# FBV
def item_list(request):
    items = Item.objects.all()
    data = [{"name": item.name, "description": item.description} for item in items]
    return JsonResponse(data, safe=False)

# CBV
class ItemList(APIView):
    permission_classes = [AllowAny]  # Allow anyone to read
    
    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

# CBV - Read/Write with authentication
class ItemDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request, pk):
        try:
            item = Item.objects.get(pk=pk)
            serializer = ItemSerializer(item)
            return Response(serializer.data)
        except Item.DoesNotExist:
            return Response({"error": "Item not found"}, status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, pk):
        try:
            item = Item.objects.get(pk=pk)
            serializer = ItemSerializer(item, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Item.DoesNotExist:
            return Response({"error": "Item not found"}, status=status.HTTP_404_NOT_FOUND)

# Public API - No authentication
class PublicItemList(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request):
        items = Item.objects.all()[:5]
        serializer = ItemSerializer(items, many=True)
        return Response({
            "message": "Public API - No authentication required",
            "items": serializer.data
        })

#ViewSet - Full authentication
class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]
    
    @action(detail=True, methods=['get'])
    def detail_info(self, request, pk=None):
        """Custom action - Get detailed item information"""
        item = self.get_object()
        return Response({
            "id": item.id,
            "name": item.name,
            "description": item.description,
            "created_at": item.id,  # Using id as proxy for created_at
            "message": "This is a custom action requiring authentication"
        })