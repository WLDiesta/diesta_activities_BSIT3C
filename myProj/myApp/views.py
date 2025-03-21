from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
def home(request):
    context={}
    return render(request, "myApp/home.html", context)

def dashboard(request):
    data = [
        {"title": "Users", "count": 150},
        {"title": "Orders", "count": 320},
        {"title": "Revenue", "count": "12450"},
    ]
    return render(request, 'myApp/dashboard.html', {"data": data})

items = [
    {"id": 1, "name": "Laptop", "price": 1000},
    {"id": 2, "name": "Mouse", "price": 50},
    {"id": 3, "name": "Keyboard", "price": 75},
]

# GET /api/items/ → Return all items.
def get_items(request):
    return JsonResponse(items, safe=False)

# GET /api/items/?search=Item → Filter items using a query parameter.
def search_items(request):
    search_query = request.GET.get('search', '').lower()
    filtered_items = [item for item in items if search_query in item['name'].lower()]
    return JsonResponse(filtered_items, safe=False)

# GET /api/items/<int:item_id>/ → Get a single item.
def get_item(request, item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    return JsonResponse(item if item else {"error": "Item not found"}, safe=False)

# POST /api/items/add/ → Add a new item (JSON or form data).
@csrf_exempt
def add_item(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            new_item = {
                "id": len(items) + 1,
                "name": data["name"],
                "price": data["price"],
            }
            items.append(new_item)
            return JsonResponse({"message": "Item added", "item": new_item}, status=201)
        except:
            return JsonResponse({"error": "Invalid data"}, status=400)

# PUT /api/items/update/<int:item_id>/ → Update an item (JSON or form data).
@csrf_exempt
def update_item(request, item_id):
    if request.method == "PUT":
        try:
            data = json.loads(request.body)
            for item in items:
                if item["id"] == item_id:
                    item.update(data)
                    return JsonResponse({"message": "Item updated", "item": item})
            return JsonResponse({"error": "Item not found"}, status=404)
        except:
            return JsonResponse({"error": "Invalid data"}, status=400)

# DELETE /api/items/delete/<int:item_id>/ → Delete an item.
@csrf_exempt
def delete_item(request, item_id):
    global items
    items = [item for item in items if item["id"] != item_id]
    return JsonResponse({"message": "Item deleted"}, status=200)