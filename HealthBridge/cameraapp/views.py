from django.shortcuts import render

import os
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
import base64


def webcam_view(request):
    return render(request, "camera.html")


def save_cropped_photo(request):
    if (
        request.method == "POST"
        and request.headers.get("x-requested-with") == "XMLHttpRequest"
    ):
        cropped_photo_data = request.POST.get("cropped_photo_data", None)

        if cropped_photo_data:
            # Decode base64 image data
            _, encoded = cropped_photo_data.split(",", 1)
            image_data = encoded.encode("utf-8")

            # Create a filename for the new image
            filename = os.path.join(settings.MEDIA_ROOT, "cropped_photo.jpg")

            # Save the image to the media directory
            with open(filename, "wb") as f:
                f.write(base64.b64decode(image_data))

            return JsonResponse(
                {"success": True, "message": "Cropped photo saved successfully."}
            )
        else:
            return JsonResponse(
                {"success": False, "message": "No image data provided."}
            )

    return JsonResponse({"success": False, "message": "Invalid request."})
