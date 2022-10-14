from django.shortcuts import redirect, render

# Create your views here.
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