from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render 
from .models import Post
from django.views import View
from .  forms import addPostForm
from django.http import HttpResponseRedirect


cars=Post.objects.all()
# def landing_page(request):
#     cars = Post.objects.all().order_by('-id')[:3]
    
#     cars = cars[::-1]
    
#     return render(request, 'portfol/landing_page.html',{'cards':cars})
class landingPage(View):
    def get(self,request):
        cars = Post.objects.all().order_by('-id')[:3]
        
        cars = cars[::-1]
        
        return render(request, 'portfol/landing_page.html',{'cards':cars})

def card_page(request):
    cars=Post.objects.all()
    # cards_datas = cards_data
    return render(request, 'includes/card.html',{'cards':cars})


# def contact_page(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             # Process the form data here
#             return HttpResponse('Thank you for contacting me!')
#     else:
#         form = ContactForm()

#     return render(request, 'main/contact_page.html', {'form': form})
class addpost(View):
    def get(self, request):
        form = addPostForm()
        return render(request, 'portfol/addPost.html', {'form': form})

    def post(self, request):
        submittedform = addPostForm(request.POST, request.FILES)

        if submittedform.is_valid():
           
            connect = Post(
                card_title=submittedform.cleaned_data['card_title'],
                card_description=submittedform.cleaned_data['card_description'],
                img_url=submittedform.cleaned_data['img_url']
            )
            connect.save()
            return HttpResponseRedirect('/addpost/')

        return render(request, 'portfol/addPost.html', {'form': submittedform})



def post_detail(request,card_id):
    
    for c in cars:
        if c.id == int(card_id):
            car_detail = c
    return render(request, 'portfol/detail_page.html',{'card':car_detail})
