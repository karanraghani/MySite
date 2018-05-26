from django.shortcuts import render, redirect
from portfolio.models import message
from portfolio.forms import contact_form
from django.template.loader import get_template
from django.core.mail import EmailMessage, send_mail

def home_page(request):
	return render(request, 'portfolio/index.html', {})

#def resume(request):

def projects(request):
	return render(request, 'portfolio/projects.html', {})

def contact_me(request):
	form = contact_form
	if request.method == 'POST':
		form = contact_form(request.POST)
		if form.is_valid():
			name = request.POST.get('name','')
			email = request.POST.get('email','')
			website = request.POST.get('website','')
			text = request.POST.get('text','')

			template = get_template('portfolio/email_template.txt')
			context = {
				'name': name,
				'email': email,
				'website': website,
				'text': text,
			}
			content = template.render(context)
			print (name,email,content)
			print ('email sending')
			'''
			email = EmailMessage(
				"New Message from Submission",
				content,
				"karanraghani.me",
				['karanraghani14@gmail.com'],
			)
			email.send()
			
			'''
			send_mail(
				"New Message from Submission",
				content,
				"karanraghani.me",
				['karanraghani14@gmail.com'],
				fail_silently=False
				)
			print('email send')
			# send an email to me with the message
			return redirect(home_page)

		
	return render(request, 'portfolio/contact_me.html', {'form': form, 'form_error':form.errors, })