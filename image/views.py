from django.shortcuts import render, get_object_or_404
from .models import Image
import requests
from django.http import JsonResponse


# Create your views here.
api_key = "45177013-f367ba3f321762884f4f25506"
category = "food"
color = "white"
data = requests.get(
    f"https://pixabay.com/api/?key={api_key}&q={category}&image_type=photo&pretty=true"
)


def home_view(request):
    global data
    api_data = data.json()

    for image in api_data["hits"]:
        if not Image.objects.filter(previewURL=image["previewURL"]).exists():
            Image.objects.create(
                previewURL=image["previewURL"],
                largeImageURL=image["largeImageURL"],
                tags=image["tags"],
                likes=image["likes"],
                downloads=image["downloads"],
                views=image["views"],
                comments=image["comments"],
            )

    images = Image.objects.all()
    return render(request, "index.html", {"images": images})


def image_detail_view(request, pk):
    image = get_object_or_404(Image, pk=pk)
    return render(request, "detail.html", {"image": image})
