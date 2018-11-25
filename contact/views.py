from django.shortcuts import render, redirect
from . import forms
from django.core.mail import send_mail

# Create your views here.
def contactform(request):
  if request.method == 'POST':
    form = forms.ContactForm(request.POST)
    if form.is_valid():
      instance = form.save(commit=False)
      instance.save()
      return redirect('contact:contactform')
  else:
    form = forms.ContactForm()
  return render(request, 'contact/contact.html', {'form':form})
