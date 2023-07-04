from django import forms
from django.core.mail import EmailMessage, BadHeaderError
from django.http import HttpResponse


class ContactForm(forms.Form):
    title = forms.CharField(max_length=50)
    contact = forms.CharField(widget=forms.Textarea(), max_length=1000)
    nickname = forms.CharField(max_length=50)
    email = forms.EmailField()
    myself = forms.BooleanField(required=False)

    def send_mail_function(self):
        subject = self.cleaned_data['title']
        message = self.cleaned_data['contact'] + f'\n====================\nお問合せ者氏名：{self.cleaned_data["nickname"]}' + \
            f'\nEmail：{self.cleaned_data["email"]}\n===================='
        from_email = ""
        user_email = ""
        if self.cleaned_data['myself']:
            user_email = self.cleaned_data['email']
        recipient_list = [
            user_email
        ]
        bcc = [
            "aikawa.shota24@gmail.com"
        ]
        msg = EmailMessage(subject, message, from_email, recipient_list, bcc)
        try:
            msg.send()
        except BadHeaderError:
            return HttpResponse("無効なヘッダが検出されました。")
