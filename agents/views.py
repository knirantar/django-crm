from django.shortcuts import render,reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from leads.models import Agent
from .forms import AgentModelForm
# Create your views here.

class AgentListView(LoginRequiredMixin,generic.ListView):
    template_name = 'agents/agents_list.html'
    def get_queryset(self):
        oraganization = self.request.user.userprofile
        return Agent.objects.filter(oraganization = oraganization)

class AgentCreateView(LoginRequiredMixin,generic.CreateView):
    template_name = 'agents/agent_create.html'
    form_class = AgentModelForm

    def get_success_url(self):
        return reverse("agents:agents-list")

    def form_valid(self,form):
        agent = form.save(commit = False)
        #commit so that it dont commit to database
        agent.oraganization = self.request.user.userprofile
        #give agent organization as it is empty -- pass userprofile as organization 
        agent.save()
        return super(AgentCreateView,self).form_valid(form)

class AgentDetailView(LoginRequiredMixin,generic.DetailView):
    template_name = 'agents/agent_detail.html'
    queryset = Agent.objects.all()
    context_object_name = 'agent'

    def get_queryset(self):
        oraganization = self.request.user.userprofile
        return Agent.objects.filter(oraganization = oraganization)

class AgentUpdateView(LoginRequiredMixin,generic.UpdateView):
    template_name = 'agents/agent_update.html'
    form_class = AgentModelForm
    context_object_name = 'agent'

    def get_success_url(self):
        return reverse("agents:agents-list")

    def get_queryset(self):
        oraganization = self.request.user.userprofile
        return Agent.objects.filter(oraganization = oraganization)

class AgentDeleteView(LoginRequiredMixin,generic.DeleteView):
    template_name = 'agents/agent_delete.html'
    form_class = AgentModelForm
    context_object_name = 'agent'

    def get_success_url(self):
        return reverse("agents:agents-list")

    def get_queryset(self):
        oraganization = self.request.user.userprofile
        return Agent.objects.filter(oraganization = oraganization)