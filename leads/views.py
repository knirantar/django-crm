from django.shortcuts import render,redirect,reverse
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Lead,Agent
from .forms import LeadForm,LeadModelForm
# Create your views here.

class LandingPageView(TemplateView):
    template_name = "landing.html"

def landing_page(request):
    return render(request,'landing.html')

class LeadListView(ListView):
    template_name = 'leads/home_page.html'
    queryset = Lead.objects.all()
    context_object_name = 'leads'

def home_page(request):
    leads = Lead.objects.all()
    context = {
        'leads':leads
    }
    return render(request,'leads/home_page.html',context)

class LeadDetailView(DetailView):
    template_name = 'leads/lead_detail.html'
    queryset = Lead.objects.all()
    context_object_name = 'lead'

def lead_detail(request,pk):
    lead = Lead.objects.get(id = pk)
    context = {
        'lead':lead
    }
    return render(request,'leads/lead_detail.html',context)

class LeadCreateView(CreateView):
    template_name = 'leads/lead_create.html'
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:home")

def lead_create(request):
    print(request.POST)
    form = LeadModelForm()
    if(request.method == 'POST'):
        print("Receiving a post request")
        form = LeadModelForm(request.POST)
        if form.is_valid():
            '''print("form data")
            print(form.cleaned_data)
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            age = form.cleaned_data['age']
            agent = Agent.objects.first()
            Lead.objects.create(
                first_name = first_name,
                last_name = last_name,
                age = age,
                agent = agent)'''
            form.save()
            print("lead has been created ")
            return redirect('/leads')
    context = {
        'form':form
    }
    return render(request,'leads/lead_create.html',context)

class LeadUpdateView(UpdateView):
    template_name = 'leads/lead_update.html'
    form_class = LeadModelForm
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse("leads:home")


def lead_update(request,pk):
    lead = Lead.objects.get(id = pk)
    form = LeadModelForm(instance = lead)
    if(request.method == 'POST'):
        print("Receiving a post request")
        form = LeadModelForm(request.POST,instance=lead)
        if form.is_valid():
            form.save()
            print("lead has been created ")
            return redirect('/leads')
    context = {
        'form':form,
        'lead':lead,
    }
    return render(request,'leads/lead_update.html',context)

class LeadDeleteView(DeleteView):
    template_name = 'leads/lead_delete.html'
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse("leads:home")

def lead_delete(request,pk):
    lead = Lead.objects.get(id = pk)
    lead.delete()
    return redirect("/leads")
