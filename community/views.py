from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse

from django.db.models import Q

from django.views.generic import TemplateView, DetailView, CreateView, ListView
from django.views.generic.edit import UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect

from .models import *
from .forms import *


# Create your views here.


class CommunityCreateView(LoginRequiredMixin, CreateView):
    model = Community
    fields = ["topic", "title", "description", "tags"]
    success_url = reverse_lazy("home")
    template_name = "community.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CommunityListView(ListView):
    queryset = Community.objects.order_by('-date_created')
    model = Community
    template_name = 'community_list.html'
    paginate_by = 4


class CommunityDetailView(DetailView):
    model = Community
    template_name = 'community_detail.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        likes_connected = get_object_or_404(Community, id=self.kwargs['pk'])
        liked = False
        if likes_connected.likes.filter(id=self.request.user.id).exists():
            liked = True
        data['number_of_likes'] = likes_connected.posts_liked()
        data['post_is_liked'] = liked

        dicussions_connected = Discussion.objects.filter(
            community=self.get_object())
        data['dicussions'] = dicussions_connected
        if self.request.user.is_authenticated:
            data['dicussion_form'] = DiscussionForm(instance=self.request.user)

        return data

    def post(self, request, *args, **kwargs):
        new_discussion = Discussion(content=request.POST.get('content'),
                                    user=self.request.user,
                                    community=self.get_object())
        new_discussion.save()
        return self.get(self, request, *args, **kwargs)


class CommunityUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Community
    fields = ["topic", "title", "description", "tags"]
    template_name = 'community_edit.html'

    def get_success_url(self):
        return reverse_lazy("home")

    def test_func(self):
        community = self.get_object()
        return self.request.user == community.user


class CommunityDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Community
    template_name = 'community_delete.html'
    success_url = reverse_lazy("home")

    def test_func(self):
        community = self.get_object()
        return self.request.user == community.user


def CommunityLike(request, pk):
    post = get_object_or_404(Community, id=request.POST.get('community_id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return HttpResponseRedirect(reverse('community:community_detail', args=[str(pk)]))


