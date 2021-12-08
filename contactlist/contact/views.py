from django.shortcuts import render,redirect

from .models import Contact
# Create your views here.

def index(request):
  contacts = Contact.objects.all()
  search_input= request.GET.get('search_area')
  if search_input:
    contacts.Contacts.ojects.filter(full__name__icontans=search_input)
  else:
      contacts.Contacts.objects.all()
      search_input =''
  return render(request,'index.html', {'contacts': contacts, 'search_input': search_input})
    
    
    
def addContact(request):
  if request.method == 'POST':
    new_contact = Contact(
      full_name = request.POST['fullname'],
      relationship =request.POST['relationship'],
      email =request.POST['email'],
      phone_number =request.POST['phone-number'],
      address =request.POST['address'],
    )
    new_contact.save()
    return redirect('/')
  return render(request, 'new.html')


def contactProfile(request,pk):
    contacts = Contact.objects.get(id=pk)
    return render(request, 'contact-profile.html', {'contact': contact})
    
def editContact(request,pk):
  contacts = Contact.objects.get(id=pk)
  
  if request.method == 'POST':
    contact.full_name = request.POST['full_name'],
    contact.relationship= request.POST['relationship'],
    contact.email = request.POST['email'],
    contact.phone_number = request.POST['phone_number'],
    contact.address = request.POST['address'],
    
    contact.save()
    return redirect('/profile/' +str(contact.id))
  return render(request,'edit.html', {'contact': contact})


def deleteContact(request,pk):
    contacts = Contact.objects.get(id=pk)
    if request.method == 'POST':
      contact.delete()
      return render('/')
    return render(request, 'delete.html', {'contact': contact})