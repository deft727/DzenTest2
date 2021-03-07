from django.shortcuts import render,redirect
from django.views.generic import View
from django.views.generic import ListView,DeleteView
from .forms import ReviewsForm
from .models import Reviews

class IndexView(View):
    def get(self,request,*args,**kwargs):
        form=ReviewsForm(request.POST or None)
        reviews=Reviews.objects.filter(parent__isnull=True).order_by('-id')
    
        context={
            'form':form,
            'title':'Отзывы',
            'reviews':reviews
                            }
        return render (request,'otziv.html', context) 


class AddReview(View):
    def post(self,request):
        form = ReviewsForm(request.POST)
        if form.is_valid():
            form=form.save(commit=False)
            if request.POST.get("parent",None):
                form.parent_id=int(request.POST.get("parent"))
                # print(request.POST.get("parent"))
            form.order_id=1
            form.save()
        return redirect("/")