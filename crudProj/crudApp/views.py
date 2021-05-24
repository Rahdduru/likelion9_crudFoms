from django.shortcuts import render, redirect, get_object_or_404
from .models import Post

# Create your views here.

#메인페이지
def main(request):
    return render(request, 'crudApp/main.html')

#글쓰기페이지
def new(request):
    return render(request, 'crudApp/new.html')

#글쓰기 함수

#읽기페이지
def read(request):
    return render(request, 'crudApp/read.html')

#디테일페이지
def detail(request):
    return render(request, 'crudApp/detail.html')

#수정페이지
def edit(request):
    return render(request, 'crudApp/edit.html')

#수정 함수