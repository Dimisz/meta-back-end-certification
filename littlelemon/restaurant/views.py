from django.views.generic import TemplateView, ListView, DetailView, FormView
from django.urls import reverse

from .forms import BookingForm
from .models import Menu

# Create your views here.
class HomeView(TemplateView):
    template_name = "index.html"

class AboutView(TemplateView):
    template_name = "about.html"

class BookingView(FormView):
    form_class = BookingForm
    template_name = "book.html"

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        booking = form.save(commit=False)
        booking.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("home")

class MenuListView(ListView):
    model = Menu
    template_name = "menu.html"

class MenuDetailView(DetailView):
    model = Menu
    template_name = "menu_item.html"
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