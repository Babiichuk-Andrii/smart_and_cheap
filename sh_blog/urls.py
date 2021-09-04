from django.urls import path


from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index_url'),
    path('world/<str:slug>/', WorldDetailsView.as_view(), name='world_detail_url'),
    path('category/<str:slug>/', CategoryDetailView.as_view(), name='category_detail_url'),
    path('room/<str:slug>/', CategoryRoomDetailView.as_view(), name='category_room_detail_url'),
    path('topic/<str:slug>/', TopicDetailsView.as_view(), name='topic_details_url'),
    path('topic_room/<str:slug>/', TopicRoomDetailView.as_view(), name='topic_room_detail_url'),
    path('projects/<str:slug>/', ProjectDetailView.as_view(), name='project_url'),
    path('create_world/', CreateWorldView.as_view(), name='create_world_url')
]
