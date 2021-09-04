from django.shortcuts import render, redirect
from django.views import View


from .models import *
from .utils import ObjectDetailMixin
from .forms import WorldForm

# Create your views here.


class IndexView(View):
    def get(self, request):
        worlds = World.objects.all()
        return render(request, 'sh_blog/index.html', context={'worlds': worlds})


class WorldDetailsView(ObjectDetailMixin, View):

    model = World
    template = 'sh_blog/world_detail.html'


class CategoryDetailView(ObjectDetailMixin, View):

    model = Category
    template = 'sh_blog/category_detail.html'


class CategoryRoomDetailView(ObjectDetailMixin, View):

    model = CategoryRooms
    template = 'sh_blog/category_room_detail.html'


class TopicDetailsView(ObjectDetailMixin, View):

    model = Topic
    template = 'sh_blog/topic_details.html'


class TopicRoomDetailView(ObjectDetailMixin, View):

    model = TopicRooms
    template = 'sh_blog/topic_room_details.html'


class ProjectDetailView(ObjectDetailMixin, View):

    model = RoomsProjects
    template = 'sh_blog/project_details.html'


class CreateWorldView(View):
    def get(self, request):
        world_form = WorldForm()
        return render(request, 'sh_blog/create_world.html', context={'world_form': world_form})

    def post(self, request):
        bound_world_form = WorldForm(request.POST)

        if bound_world_form.is_valid():
            new_world = bound_world_form.save()
            return redirect(new_world)
        return render(request, 'sh_blog/create_world.html', context={'world_form': bound_world_form})


class CreateCategory(View):
    pass
