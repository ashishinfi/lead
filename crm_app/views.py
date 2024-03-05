from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from .models import Product  # Make sure to import your Product model correctly


from django.http import HttpResponse
from django.template import loader
from rest_framework import viewsets
from .models import Customer,Lead,Opportunity,Interaction,Product,Sale,Contact
from .serializers import (
    CustomerSerializer,
    LeadSerializer,
    OpportunitySerializer,
    InteractionSerializer,
    ProductSerializer,
    SaleSerializer,
    ContactSerializer,
)



# Create your views here.
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

class OpportunityViewSet(viewsets.ModelViewSet):
    queryset = Opportunity.objects.all()
    serializer_class = OpportunitySerializer

class InteractionViewSet(viewsets.ModelViewSet):
    queryset = Interaction.objects.all()
    serializer_class = InteractionSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def general(request):
    return render(request, 'general.html')

def leads(request):
    return render(request, 'leads.html')

def opportunity(request):
    return render(request, 'opportunity.html')

def interaction(request):
    return render(request, 'interaction.html')

def product(request):
    return render(request, 'product.html')

def sales(request):
    return render(request, 'sales.html')

def contacts(request):
    return render(request, 'contacts.html')

def simple(request):
    return render(request, 'simple.html')

def leadstable(request):
    return render(request, 'leadstable.html')

def opportunitytable(request):
    return render(request, 'opportunitytable.html')

def interactiontable(request):
    return render(request, 'interactiontable.html')

def producttable(request):
    return render(request, 'producttable.html')

def salestable(request):
    return render(request, 'salestable.html')

def contacttable(request):
    return render(request, 'contacttable.html')
    
# Views for Form Submission

def save_data(request):
    if request.method == 'POST' and request.is_ajax():
        name = request.POST.get('name')
        price = request.POST.get('price')

        # Save data to your model
        new_data = Product.objects.create(name=name, price=price)

        # Return response
        return JsonResponse({'id': new_data.id, 'name': new_data.name, 'price': new_data.price})

    return JsonResponse({'error': 'Invalid request'})


def leads_data(request):
    if request.method=='POST' and request.is_ajax():
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        status=request.POST.get('status')

         # Save data to your model
        new_data = Product.objects.create(first_name=first_name, last_name=last_name, email=email, phone=phone , status=status)


        # Return response
        return JsonResponse({'id': new_data.id, 'name': new_data.first_name, 'price': new_data.last_name, 'email': new_data.email, 'phone': new_data.phone, 'status': new_data.status})

    return JsonResponse({'error': 'Invalid request'})

def opp_data(request):
    if request.method == 'POST' and request.is_ajax():
        amount = request.POST.get('amount')
        stage = request.POST.get('stage')
        close_date=request.POST.get('close_date')
        customer=request.POST.get('customer')


 # Save data to your model
        new_data = Product.objects.create(amount=amount,stage=stage,close_date=close_date,customer=customer)

        # Return response
        return JsonResponse({'id': new_data.id, 'amount': new_data.amount, 'stage': new_data.stage, 'close_date':new_data.close_date, 'customer':new_data.customer})

    return JsonResponse({'error': 'Invalid request'})

def sales_data(request):
    if request.method=='POST'and request.is_ajax():
         quantity = request.POST.get('quantity')
         total_amount = request.POST.get('total_amount')
         sale_date=request.POST.get('sale_date')
         customer=request.POST.get('customer')
         product=request.POST.get('product')

         new_data = Product.objects.create(quantity=quantity, total_amount=total_amount, sale_date=sale_date, customer=customer , product=product)
         # Return response

         return JsonResponse({'id': new_data.id, 'quantity': new_data.quantity, 'total_amount': new_data.total_amount, 'sale_date': new_data.sale_date, 'customer': new_data.customer, 'product': new_data.product})


def interaction_data(request):
    if request.method=='POST'and request.is_ajax():
        interaction_type=request.POST.get('interaction_type')
        date=request.POST.get('date')
        notes=request.POST.get('notes')
        customer=request.POST.get('customer')

        new_data = Product.objects.create(interaction_type=interaction_type, date=date, notes=notes, customer=customer )

        return JsonResponse({'id': new_data.id, 'interaction_type': new_data.interaction_type, 'date': new_data.date, 'notes': new_data.notes, 'customer': new_data.customer})
    



def customer_data(request):
    if request.method=='POST' and request.is_ajax():
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        address=request.POST.get('address')

        new_data=Product.objects.create(first_name=first_name,last_name=last_name,email=email,phone=phone,address=address)

        return JsonResponse({'id': new_data.id, 'firstname':new_data.first_name, 'last_name':new_data.last_name,'email':new_data.email, 'phone':new_data.phone, 'address':new_data.address})
    
@api_view(['POST'])
def contact_data(request):
    # Extract data directly from request.data assuming JSON body
    
    Name = request.data.get('Name', None)
    Email = request.data.get('Email',None)
    Mobile_Number = request.data.get('tel',None)
    Website_Url = request.data.get('Website_Url',None)
    Page_Url = request.data.get('Page_Url',None)
    Date = request.data.get('_date',None)
    Time = request.data.get('_time',None)
    Lead_ID = request.data.get('_serial_number',None)
    Referral_information_field = request.data.get('referral_Information_field',None)
    Visitor_came_from = request.data.get('Visitor_came_from',None)
    utm_source = request.data.get('utm_source',None)
    utm_medium = request.data.get('utm_medium',None)
    utm_campaign = request.data.get('utm_campaign'),None
    Last_visited_pages = request.data.get('CF7VPUT_VISITED_Details',None)

    # Create a new Product object with the extracted data
    newdata = Product.objects.create(
        Name=Name,
        Email=Email, 
        Mobile_Number=Mobile_Number, 
        Website_Url=Website_Url, 
        Page_Url=Page_Url, 
        Date=Date, 
        Time=Time, 
        Lead_ID=Lead_ID,
        Referral_information_field=Referral_information_field,
        Visitor_came_from=Visitor_came_from,
        utm_source=utm_source,
        utm_medium=utm_medium,
        utm_campaign=utm_campaign,
        Last_visited_pages=Last_visited_pages
    )

    # Return the created Product object data as JSON
    return JsonResponse({
        'id': newdata.id, 
        'Name': newdata.Name,
        'Email': newdata.Email, 
        'Mobilenumber': newdata.Mobile_Number, 
        'Website_url': newdata.Website_Url, 
        'Pageurl': newdata.Page_Url, 
        'Date': newdata.Date, 
        'Time': newdata.Time,
        'Lead_ID': newdata.Lead_ID,
        'Referral_information_field': newdata.Referral_information_field,
        'Visitor_came_from': newdata.Visitor_came_from,
        'utm_source': newdata.utm_source,
        'utm_medium': newdata.utm_medium,
        'utm_campaign': newdata.utm_campaign,
        'Last_visited_pages': newdata.Last_visited_pages 
    })
