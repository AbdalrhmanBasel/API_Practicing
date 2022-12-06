from django.http import JsonResponse


def api_homePage(request, *args, **kwargs):
    return JsonResponse({"message": "Hey, this is home page API response!"})