from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post

cards_data = [
    {'id': 1, 'card_title': 'Card 1', 'card_description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.', 'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSj7Fnx0Fx2kOHAU9715pcAAwfJHrML3rml7Q&s'},
    {'id': 2, 'card_title': 'Card 2', 'card_description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.', 'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcROYjj94a1EKPObxDQCbqSdwmIbkhQt5Np5lQ&s'},
    {'id': 3, 'card_title': 'Card 3', 'card_description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.', 'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRI2RLOBO8DYvk8aAUNEs6DJzCJzlgHT7HfAg&s'},
]
def landing_page(request):
    return render(request, 'portfol/landing_page.html')

def card_page(request):

    # cards_datas = cards_data
    return render(request, 'includes/card.html',{'cards':cards_data})


def contact_page(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data here
            return HttpResponse('Thank you for contacting me!')
    else:
        form = ContactForm()

    return render(request, 'main/contact_page.html', {'form': form})

from django.shortcuts import render, get_object_or_404
from .models import Post  # You need to define this model

def post_detail(request, card_id):
    post = get_object_or_404(Post, id=card_id)
    return render(request, 'main/post.html', {'post': post})

def detail_page(request, card_id):
    for c in cards_data:
        if c['id'] == int(card_id):
            card = c
    return render(request, 'portfol/detail_page.html', {'card': card})
