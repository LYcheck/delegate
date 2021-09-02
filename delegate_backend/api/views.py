from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.serializers import Serializer
from .models import *
from .serializers import *
from django.core.exceptions import ObjectDoesNotExist
import json

error_message = 'Something terrible went wrong'

# Create your views here.

def welcome(request):
  content = {"message": "D E L E G A T E"}
  return JsonResponse(content)

# ---------- LIST ----------

@api_view(["POST"])
@csrf_exempt
def get_list(request):
  payload = json.loads(request.body)
  try:
    list_list = list(List.objects.filter(id=payload["id"]).values_list())
    # serializer = ListSerializer(list_list)
    return JsonResponse({'list': list_list}, safe=False, status=status.HTTP_200_OK)
  except ObjectDoesNotExist as e:
    return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
  except Exception:
    return JsonResponse({'error': error_message}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["GET"])
@csrf_exempt
def get_lists(requst):
  try:
    list_list = list(List.objects.values_list());
    # serializer = ListSerializer(list_list)
    return JsonResponse({'lists': list_list}, safe=False, status=status.HTTP_200_OK)
  except ObjectDoesNotExist as e:
    return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
  except Exception:
    return JsonResponse({'error': error_message}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
  

@api_view(["POST"])
@csrf_exempt
def create_list(request):
  payload = json.loads(request.body)

  try:
      list = List.objects.create(
          name=payload["name"],
          type=payload["type"],
          description=payload["description"],
          author=payload["author"],
          time=None
      )
      serializer = ListSerializer(list)
      return JsonResponse({'lists': serializer.data}, safe=False, status=status.HTTP_201_CREATED)

  except ObjectDoesNotExist as e:
      return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
      
  except Exception:
      return JsonResponse({'error': error_message}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["DELETE"])
@csrf_exempt
def delete_list(request):
  return HttpResponse("hello4")


@api_view(["PUT"])
def update_list(request):
  payload = json.loads(request.body)
  list_id = payload["id"]
  del payload["id"]
  try:
    Item.objects.filter(id=list_id).update(**payload)
    # serializer = ItemSerializer(list_list)
    return JsonResponse("Update Successful", safe=False, status=status.HTTP_200_OK)
  except ObjectDoesNotExist as e:
    return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
  except Exception:
    return JsonResponse({'error': error_message}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# ---------- ITEM ----------
@api_view(["POST"])
@csrf_exempt
def get_item(request):
  payload = json.loads(request.body)
  try:
    item_list = list(Item.objects.filter(id=payload["id"]).values_list());
    # serializer = ItemSerializer(list_list)
    return JsonResponse({'item': item_list}, safe=False, status=status.HTTP_200_OK)
  except ObjectDoesNotExist as e:
    return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
  except Exception:
    return JsonResponse({'error': error_message}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["GET"])
@csrf_exempt
def get_items(request):
  try:
    item_list = list(Item.objects.values_list());
    # serializer = ItemSerializer(list_list)
    return JsonResponse({'items': item_list}, safe=False, status=status.HTTP_200_OK)
  except ObjectDoesNotExist as e:
    return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
  except Exception:
    return JsonResponse({'error': error_message}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["POST"])
@csrf_exempt
def create_item(request):
  payload = json.loads(request.body)
  try:
    item = Item.objects.create(
      name=payload["name"],
      type=payload["type"],
      description=payload["description"],
      parent_list=payload["parent_list"],
      time=None
    )
    serializer = ItemSerializer(item)
    return JsonResponse({'items': serializer.data}, safe=False, status=status.HTTP_201_CREATED)

  except ObjectDoesNotExist as e:
    return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    
  except Exception as e:
    return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["DELETE"])
@csrf_exempt
def delete_item(request):
  return HttpResponse("hello")


@api_view(["PUT"])
def update_item(request):
  payload = json.loads(request.body)
  item_id = payload["id"]
  del payload["id"]
  try:
    Item.objects.filter(id=item_id).update(**payload)
    # serializer = ItemSerializer(list_list)
    return JsonResponse("Update Successful", safe=False, status=status.HTTP_200_OK)
  except ObjectDoesNotExist as e:
    return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
  except Exception:
    return JsonResponse({'error': error_message}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# ---------- GROUP ----------
@api_view(["POST"])
@csrf_exempt
def get_group(request):
  payload = json.loads(request.body)
  try:
    group_list = list(Group.objects.filter(id=payload["id"]).values_list())
    # serializer = ItemSerializer(list_list)
    return JsonResponse({'group': group_list}, safe=False, status=status.HTTP_200_OK)
  except ObjectDoesNotExist as e:
    return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
  except Exception:
    return JsonResponse({'error': error_message}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["GET"])
@csrf_exempt
def get_groups(request):
  try:
    group_list = list(Group.objects.values_list());
    # serializer = GroupSerializer(group_list)
    return JsonResponse({'groups': group_list}, safe=False, status=status.HTTP_200_OK)
  except ObjectDoesNotExist as e:
    return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
  except Exception:
    return JsonResponse({'error': error_message}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["POST"])
@csrf_exempt
def create_group(request):
  payload = json.loads(request.body)
  try:
    group = Group.objects.create(
      name=payload["name"],
      author=payload["author"],
      description=payload["description"],
      )
    serializer = GroupSerializer(group)
    return JsonResponse({'groups': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
  except ObjectDoesNotExist as e:
    return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
  except Exception:
    return JsonResponse({'error': error_message}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["POST"])
@csrf_exempt
def join_group(request):
  return HttpResponse("hello")


@api_view(["DELETE"])
@csrf_exempt
def leave_group(request):
  return HttpResponse("hello")


@api_view(["PUT"])
def update_group(request):
  payload = json.loads(request.body)
  group_id = payload["id"]
  del payload["id"]
  try:
    Item.objects.filter(id=group_id).update(**payload)
    # serializer = ItemSerializer(list_list)
    return JsonResponse("Update Successful", safe=False, status=status.HTTP_200_OK)
  except ObjectDoesNotExist as e:
    return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
  except Exception:
    return JsonResponse({'error': error_message}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# ---------- EVENT ----------
@api_view(["POST"])
@csrf_exempt
def get_event(request):
  payload = json.loads(request.body)
  try:
    event_list = list(Event.objects.filter(id=payload["id"]).values_list());
    # serializer = ItemSerializer(list_list)
    return JsonResponse({'event': event_list}, safe=False, status=status.HTTP_200_OK)
  except ObjectDoesNotExist as e:
    return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
  except Exception:
    return JsonResponse({'error': error_message}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["GET"])
@csrf_exempt
def get_events(request):
  try:
    event_list = list(Event.objects.values_list());
    # serializer = EventSerializer(event_list)
    return JsonResponse({'events': event_list}, safe=False, status=status.HTTP_200_OK)
  except ObjectDoesNotExist as e:
    return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
  except Exception:
    return JsonResponse({'error': error_message}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["POST"])
@csrf_exempt
def create_event(request):
  payload = json.loads(request.body)
  try:
    event = Event.objects.create(
      name=payload["name"],
      author=payload["author"],
      description=payload["description"],
      parent_list=payload["parent_list"],
      parent_group=payload["parent_group"],
      time=None
    )
    serializer = EventSerializer(event)
    return JsonResponse({'events': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
  except ObjectDoesNotExist as e:
    return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
  except Exception:
    return JsonResponse({'error': error_message}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["POST"])
@csrf_exempt
def add_to_event(request):
  return HttpResponse("hello")


@api_view(["DELETE"])
@csrf_exempt
def remove_from_event(request):
  return HttpResponse("hello")


@api_view(["PUT"])
def update_event(request):
  payload = json.loads(request.body)
  event_id = payload["id"]
  del payload["id"]
  try:
    Item.objects.filter(id=event_id).update(**payload)
    # serializer = ItemSerializer(list_list)
    return JsonResponse("Update Successful", safe=False, status=status.HTTP_200_OK)
  except ObjectDoesNotExist as e:
    return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
  except Exception:
    return JsonResponse({'error': error_message}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# ---------- ADMIN ----------
@api_view(["POST"])
@csrf_exempt
def login_submit(request):
  return HttpResponse("hello")


@api_view(["POST"])
@csrf_exempt
def signup_submit(request):
  return HttpResponse("hello")


@api_view(["POST"])
@csrf_exempt
def signout_submit(request):
  return HttpResponse("hello")
  