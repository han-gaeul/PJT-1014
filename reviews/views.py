from django.shortcuts import redirect, render
from .models import Review
from .forms import ReviewForm

# Create your views here.
def index(request):
    reviews = Review.objects.order_by('-pk')
    context = {
        'reviews' : reviews
    }
    return render(request, 'reviews/index.html', context)

def create(request):
    if request.method == 'POST':
        reviews_form = ReviewForm(request.POST)
        if reviews_form.is_valid():
            reviews_form.save()
            return redirect('review:index')
    else:
        reviews_form = ReviewForm()
    context = {
        'reviews_form' : reviews_form
    }
    return render(request, 'reviews/form.html', context=context)

def detail(request, pk):
    reviews = Review.objects.get(pk=pk)
    context = {
        'reviews' : reviews
    }
    return render(request, 'reviews/detail.html', context)

def update(request, pk):
    reviews = Review.objects.get(pk=pk)
    if request.method == 'POST':
        reviews_form = ReviewForm(request.POST, instance=review)
        if reviews_form.is_valid():
            reviews_form.save()
            return redirect('review:detail', review.pk)
    else:
        reviews_form = ReviewForm(instance=review)
    context = {
        'reviews_form' : reviews_form
    }
    return render(request, 'reviews/form.html', context)

def delete(request, pk):
    Review.objects.get(pk=pk).delete()
    return redirect('review:index')