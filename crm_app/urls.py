from . import views
from rest_framework import routers
from django.urls import include, path
from .views import index
from .views import home,save_data,leads_data,opp_data,sales_data,interaction_data,customer_data,contact_data
from .views import general, leads, opportunity,interaction,product,sales,contacts,simple,leadstable,opportunitytable
from .views import interactiontable,producttable,salestable,contacttable

from .views import (
    CustomerViewSet,
    LeadViewSet,
    OpportunityViewSet,
    InteractionViewSet,
    ProductViewSet,
    SaleViewSet,
    ContactViewSet,
    
)

router = routers.DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'leads', LeadViewSet)
router.register(r'opportunities', OpportunityViewSet)
router.register(r'interactions', InteractionViewSet)
router.register(r'products', ProductViewSet)
router.register(r'sales', SaleViewSet)
router.register(r'contacts', ContactViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    path('index/', index, name='index'),
    path('home/', home, name='home'),
    path('general/', general, name='general'),
    path('leads/', leads, name='leads'),
    path('opportunity/', opportunity, name='opportunity'),
    path('interaction/', interaction, name='interaction'),
    path('product/', product, name='product'),
    path('sales/', sales, name='sales'),
    path('contacts/', contacts, name='contacts'),
    path('simple/', simple, name='simple'),
    path('leadstable/', leadstable, name='leadstable'),
    path('opportunitytable/', opportunitytable, name='oportunitytable'),
    path('interactiontable/', interactiontable, name='interactiontable'),
    path('producttable/', producttable, name='producttable'),
    path('salestable/', salestable, name='salestable'),
    path('contacttable/', contacttable, name='contacttable'),
    path('save-data/', save_data, name='save_data'),
    path('leads_data/', leads_data, name='leads_data'),
    path('opp_data/', opp_data, name='opp_data'),
    path('sales_data/', sales_data, name='sales_data'),
    path('interaction_data/', interaction_data, name='interaction_data'),
    path('customer_data/', customer_data, name='customer_data'),
    path('contact_data/', contact_data, name='contact_data'),
]

