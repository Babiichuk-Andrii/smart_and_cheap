from django import forms

from .models import *


class WorldForm(forms.ModelForm):
    class Meta:
        model = World
        fields = ['title', 'description']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'})
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['world', 'title', 'description']

        widgets = {
            'world': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'})
        }


class CategoryRoomsForm(forms.ModelForm):
    class Meta:
        model = CategoryRooms
        fields = ['category', 'title', 'type_of_room', 'description']

        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'type_of_room': forms.Select(),
            'description': forms.TextInput(attrs={'class': 'form-control'})
        }


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['room', 'title', 'body']

        widgets = {
            'room': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'})
        }


class TopicRoomsForm(forms.ModelForm):
    class Meta:
        model = TopicRooms
        fields = ['topic', 'title', 'type_of_room', 'description']

        widgets = {
            'topic': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'type_of_room': forms.Select(),
            'description': forms.TextInput(attrs={'class': 'form-control'})
        }


class RoomsProjectsForm(forms.ModelForm):
    class Meta:
        model = RoomsProjects
        fields = ['room', 'title', 'type_of_project', 'description', 'body']

        widgets = {
            'room': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'type_of_project': forms.Select(),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'})
        }
