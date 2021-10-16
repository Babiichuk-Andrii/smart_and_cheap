from django.urls import path


from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index_url'),
    path('world/<str:slug>/', WorldDetailsView.as_view(), name='world_detail_url'),
    path('world/<str:slug>/edit_world/', EditWorldView.as_view(), name='edit_world_url'),
    path('category/<str:slug>/', CategoryDetailView.as_view(), name='category_detail_url'),
    path('category/<str:slug>/edit_category/', EditCategoryView.as_view(), name='edit_category_url'),
    path('room/<str:slug>/', CategoryRoomDetailView.as_view(), name='category_room_detail_url'),
    path('room/<str:slug>/edit_room/', EditCategoryRoomsView.as_view(), name='edit_category_room_url'),
    path('topic/<str:slug>/', TopicDetailsView.as_view(), name='topic_details_url'),
    path('topic/<str:slug>/edit_topic/', EditTopicView.as_view(), name='edit_topic_url'),
    path('topic_room/<str:slug>/', TopicRoomDetailView.as_view(), name='topic_room_detail_url'),
    path('topic_room/<str:slug>/edit_room/', EditTopicRoomsView.as_view(), name='edit_topic_room_url'),
    path('projects/<str:slug>/', ProjectDetailView.as_view(), name='project_url'),
    path('projects/<str:slug>/edit_project/', EditProjectView.as_view(), name='edit_project_url'),
    path('create_world/', CreateWorldView.as_view(), name='create_world_url'),
    path('create_category/', CreateCategoryView.as_view(), name='create_category_url'),
    path('create_category_rooms/', CreateCategoryRoomsView.as_view(), name='create_category_rooms_url'),
    path('create_topic/', CreateTopicView.as_view(), name='create_topic_url'),
    path('create_topic_rooms/', CreateTopicRoomsView.as_view(), name='create_topic_rooms_url'),
    path('create_rooms_projects/', CreateRoomsProjectsView.as_view(), name='create_rooms_projects_url')
]
