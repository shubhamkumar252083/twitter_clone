from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from hashids import Hashids
from .forms import PassData


def encode_id(id, secret_key="8434939102"):
    hashids = Hashids(salt=secret_key, min_length=50)
    return hashids.encode(id)

def decode_id(encoded_id, secret_key="8434939102"):
    hashids = Hashids(salt=secret_key, min_length=50)
    decoded_ids = hashids.decode(encoded_id)
    return decoded_ids[0] if decoded_ids else None


@method_decorator(login_required(login_url='login'), name='dispatch')
class HashUrl(View):
    def get(self, request, format=None):
        form = PassData()
        return render(request, "hash_url.html", {"form":form})
    
    def post(self, request, format=None):
        form = PassData(request.POST)
        if form.is_valid():
            pass_data = form.cleaned_data["pass_data"]
            encode_url = f'http://127.0.0.1:8000/hash_url/encode/{encode_id(pass_data, secret_key=request.user.email)}'
        return render(request, "hash_url.html", {"form":form, "encode_url":encode_url})
    

@method_decorator(login_required(login_url='login'), name='dispatch')
class CheckHash(View):
    def get(self, request, encoded_id, format=None):
        print(f'encoded_id ==> {encoded_id}')
        _decode_id = decode_id(encoded_id, secret_key=request.user.email)
        if _decode_id:
            return HttpResponse(f"decode success ==> {_decode_id}")
        else:
            return HttpResponse(f"decode failed")


