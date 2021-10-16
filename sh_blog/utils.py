from django.shortcuts import render, get_object_or_404, redirect


class ObjectDetailMixin:
    model = None
    template = None

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        return render(request, self.template, context={self.model.__name__.lower(): obj})


class CreateObjectMixin:
    form = None
    template = None

    def get(self, request):
        obj = self.form
        return render(request, self.template, context={'form': obj})

    def post(self, request):
        bound_obj = self.form(request.POST)

        if bound_obj.is_valid():
            new_obj = bound_obj.save()
            return redirect(new_obj)
        return render(request, self.template, context={'form': bound_obj})


class EditObjectMixin:
    edited_obj = None
    form = None
    template = None

    def get(self, request, slug):
        edited = self.edited_obj.objects.get(slug__iexact=slug)
        bound_form = self.form(instance=edited)
        return render(request, self.template, context={
            'form': bound_form,
            'obj': edited
        })

    def post(self, request, slug):
        edited = self.edited_obj.objects.get(slug__iexact=slug)
        bound_form = self.form(request.POST, instance=edited)
        if bound_form.is_valid():
            updated_world = bound_form.save()
            return redirect(updated_world)
        return render(request, self.template, context={
            'form': bound_form,
            'obj': edited
        })
