from django.shortcuts import render, redirect
from .models import Book
from .forms import ContactForm
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied


class IndexView(generic.ListView):
    model = Book
    template_name = 'app/index.html'

    def get_queryset(self):
        return Book.objects.all().order_by('-updated_datetime')


class DetailView(generic.DetailView):
    model = Book
    template_name = 'app/detail.html'


class CreateView(LoginRequiredMixin, generic.CreateView):
    model = Book
    fields = ['title', 'writer', 'ndc', 'tag', 'summary', 'review', 'rating']
    template_name = 'app/new.html'

    def form_valid(self, form):
        form.instance.poster = self.request.user
        return super(CreateView, self).form_valid(form)


class EditView(LoginRequiredMixin, generic.UpdateView):
    model = Book
    fields = ['title', 'writer', 'ndc', 'tag', 'summary', 'review', 'rating']
    template_name = 'app/edit.html'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.poster != self.request.user:
            try:
                raise PermissionDenied()
            except PermissionDenied:
                print('You do not have permission to edit.')
                return render(request, 'app/rejection.html')
        return super(EditView, self).dispatch(request, *args, **kwargs)


class DeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Book
    template_name = 'app/delete_confirm.html'
    success_url = reverse_lazy('app:index')

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.poster != self.request.user:
            try:
                raise PermissionDenied()
            except PermissionDenied:
                print('You do not have permission to delete.')
                return render(request, 'app/rejection.html')
        return super(DeleteView, self).dispatch(request, *args, **kwargs)


"""
class ContactView(generic.edit.FormView):
    template_name = 'app/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('app:contact_success')

    def form_valid(self, form):
        print("form_valid関数は実行されています。")
        form.send_mail_function()
        return super().form_valid(form)

    def __init__(self, *args, **kwargs):
        ContactForm.base_fields["email"].initial = self.request.user.email
        ContactForm.base_fields["nickname"].initial = self.request.user.username
        super().__init__(*args, **kwargs)
"""

"""
    def get_context_data(self, **kwargs):
        # 既存のget_context_dataをコール
        context = super().get_context_data(**kwargs)
        # 追加したいコンテキスト情報(取得したコンテキスト情報のキーのリストを設定)
        context["email"] = self.request.user.email
        context["nickname"] = self.request.user.username
        context.update()
        # コンテキスト情報のキーを追加
        return context
"""

"""
    def get_context_data(self):
        if self.request.user.is_authenticated:
            email = self.request.user.email
            nickname = self.request.user.username
        else:
            email = ""
            nickname = ""
        form_data = {'email': email, 'nickname': nickname}
        return ContactForm(form_data)
"""


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send_mail_function()
            return redirect('app:contact_success')
    else:
        initial_data = ""
        if request.user.is_authenticated:
            user_info = request.user
            initial_data = {
                'nickname': user_info.username,
                'email': user_info.email,
                'myself': True
            }
        form = ContactForm(
            initial=initial_data,
        )

    return render(request, 'app/contact.html', {'form': form})


class ContactResultView(generic.TemplateView):
    template_name = 'app/contact_result.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['success'] = "お問い合わせは正常に送信されました。"
        return context


def about(request):
    return render(request, 'app/about.html')


def how_to_use(request):
    return render(request, 'app/how_to_use.html')
