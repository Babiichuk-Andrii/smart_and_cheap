from django import forms
from django.core.exceptions import ValidationError

from .models import *


class WorldForm(forms.ModelForm):
    class Meta:
        model = World
        fields = ['title', 'description', 'slug']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'})
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if World.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError('{} - уже занято.'.format(new_slug))
        return new_slug


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['world', 'title', 'description', 'slug']

        widgets = {
            'world': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'})
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if Category.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError('{} - уже занято.'.format(new_slug))
        return new_slug


class CategoryRoomsForm(forms.ModelForm):
    class Meta:
        model = CategoryRooms
        fields = ['category', 'title', 'type_of_room', 'description', 'slug']

        widgets = {
            'category': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'type_of_room': forms.BooleanField(),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'})
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if Category.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError('{} - уже занято.'.format(new_slug))
        return new_slug


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['room', 'title', 'body', 'slug']

        widgets ={
            'room': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'})
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if Topic.objects.filter(slug__iexact=new_slug).count():
            return ValidationError('{} - уже занятою'.format(new_slug))
        return new_slug


class TopicRoomsForm(forms.ModelForm):
    class Meta:
        model = TopicRooms
        fields = ['topic', 'title', 'type_of_room', 'description', 'slug']

        widgets = {
            'topic': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'title' : forms.TextInput(attrs={'class': 'form-control'}),
            'type_of_room': forms.BooleanField(),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'})
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if TopicRooms.objects.filter(slug__iexact=new_slug).count():
            return ValidationError('{} - уже занято.'.format(new_slug))
        return new_slug


class RoomsProjectsForm(forms.ModelForm):
    class Meta:
        model = RoomsProjects
        fields = ['room', 'title', 'type_of_project', 'description', 'body', 'slug']

        widgets = {
            'room': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'type_of_project': forms.BooleanField(),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'})
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if RoomsProjects.objects.filter(slug__iexact=new_slug).count():
            return ValidationError('{} - уже занято.'.format(new_slug))
        return new_slug
