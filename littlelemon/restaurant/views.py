from django.views.generic import TemplateView, ListView

from .forms import BookingForm
from .models import Menu
# Create your views here.
# Create your views here.
class HomeView(TemplateView):
    template_name = "index.html"

class AboutView(TemplateView):
    template_name = "about.html"


class BookingView(TemplateView):
    template_name = "book.html"

class MenuListView(ListView):
    model = Menu
    template_name = "menu.html"
# def home(request):
#     return render(request, 'index.html')

# def about(request):
#     return render(request, 'about.html')

# def book(request):
#     form = BookingForm()
#     if request.method == 'POST':
#         form = BookingForm(request.POST)
#         if form.is_valid():
#             form.save()
#     context = {'form':form}
#     return render(request, 'book.html', context)