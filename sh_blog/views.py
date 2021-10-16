from django.shortcuts import render, redirect
from django.views import View


from .models import *
from .utils import ObjectDetailMixin, CreateObjectMixin, EditObjectMixin
from .forms import WorldForm, CategoryForm, CategoryRoomsForm, TopicForm, TopicRoomsForm, RoomsProjectsForm

# Create your views here.


class IndexView(View):
    def get(self, request):
        worlds = World.objects.all()
        return render(request, 'sh_blog/index.html', context={'worlds': worlds})


class WorldDetailsView(ObjectDetailMixin, View):

    model = World
    template = 'sh_blog/world_detail.html'


class CreateWorldView(CreateObjectMixin, View):
    form = WorldForm
    template = 'sh_blog/create_world.html'


class EditWorldView(EditObjectMixin, View):
    edited_obj = World
    form = WorldForm
    template = 'sh_blog/edit_world.html'


class CategoryDetailView(ObjectDetailMixin, View):

    model = Category
    template = 'sh_blog/category_detail.html'


class CreateCategoryView(CreateObjectMixin, View):
    form = CategoryForm
    template = 'sh_blog/create_category.html'


class EditCategoryView(EditObjectMixin, View):
    edited_obj = Category
    form = CategoryForm
    template = 'sh_blog/edit_category.html'


class CategoryRoomDetailView(ObjectDetailMixin, View):
    model = CategoryRooms
    template = 'sh_blog/category_room_detail.html'


class CreateCategoryRoomsView(CreateObjectMixin, View):
    form = CategoryRoomsForm
    template = 'sh_blog/create_category_rooms.html'


class EditCategoryRoomsView(EditObjectMixin, View):
    edited_obj = CategoryRooms
    form = CategoryRoomsForm
    template = 'sh_blog/edit_category_rooms.html'


class TopicDetailsView(ObjectDetailMixin, View):

    model = Topic
    template = 'sh_blog/topic_details.html'


class CreateTopicView(CreateObjectMixin, View):
    form = TopicForm
    template = 'sh_blog/create_topic.html'


class EditTopicView(EditObjectMixin, View):
    edited_obj = Topic
    form = TopicForm
    template = 'sh_blog/edit_topic.html'


class TopicRoomDetailView(ObjectDetailMixin, View):

    model = TopicRooms
    template = 'sh_blog/topic_room_details.html'


class CreateTopicRoomsView(CreateObjectMixin, View):
    form = TopicRoomsForm
    template = 'sh_blog/create_topic_rooms.html'


class EditTopicRoomsView(EditObjectMixin, View):
    edited_obj = TopicRooms
    form = TopicRoomsForm
    template = 'sh_blog/edit_topic_rooms.html'


class ProjectDetailView(ObjectDetailMixin, View):

    model = RoomsProjects
    template = 'sh_blog/project_details.html'


class CreateRoomsProjectsView(CreateObjectMixin, View):
    form = RoomsProjectsForm
    template = 'sh_blog/create_rooms_projects.html'


class EditProjectView(EditObjectMixin, View):
    edited_obj = RoomsProjects
    form = RoomsProjectsForm
    template = 'sh_blog/edit_project.html'
