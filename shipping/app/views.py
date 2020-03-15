import easypost

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import authentication, permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import AddressForm, ParcelForm
from .models import Shipment

easypost.api_key = "EZTKfeed06fda19846b79db859f6aef43efaRpw3K7Ok4a0sy9BWyennrw" #NOT PRODUCTION KEY

class ShipmentView(APIView):
	renderer_classes = [TemplateHTMLRenderer]
	template_name = 'submit.html'
	authentication_classes = [SessionAuthentication, BasicAuthentication]
	permission_classes = [IsAuthenticated]

	def post(self, request):
		from_form = AddressForm(request.data, prefix='from_form')
		to_form = AddressForm(request.data, prefix='to_form')
		parcel_form = ParcelForm(request.data, prefix='parcel_form')

		if from_form.is_valid() and to_form.is_valid() and parcel_form.is_valid():
			fromAddress = easypost.Address.create(
				company=from_form.cleaned_data['company'],
				street1=from_form.cleaned_data['street_1'],
				street2=from_form.cleaned_data['street_2'],
				city=from_form.cleaned_data['city'],
				state=from_form.cleaned_data['state'],
				zip=from_form.cleaned_data['zip_code']
			)
			
			toAddress = easypost.Address.create(
				company=to_form.cleaned_data['company'],
				street1=to_form.cleaned_data['street_1'],
				street2=to_form.cleaned_data['street_2'],
				city=to_form.cleaned_data['city'],
				state=to_form.cleaned_data['state'],
				zip=to_form.cleaned_data['zip_code']
			)

			parcel = easypost.Parcel.create(
 				length=parcel_form.cleaned_data['length'],
				width=parcel_form.cleaned_data['width'],
				height=parcel_form.cleaned_data['height'],
				weight=parcel_form.cleaned_data['weight']
			)

			shipment = easypost.Shipment.create(
				to_address=toAddress,
				from_address=fromAddress,
				parcel=parcel
			)

			shipment.buy(rate=shipment.lowest_rate(carriers=['USPS'], services=['First']))

			s = Shipment.objects.create(label_url=shipment.postage_label.label_url, tracking_number=shipment.tracking_code, owner=request.user)
			s.save()

			return redirect('app:shipment_view')

	def get(self, request):
		shipments = request.user.shipment_set.all()
		from_form = AddressForm(prefix='from_form')
		to_form = AddressForm(prefix="to_form")
		parcel_form = ParcelForm(prefix='parcel_form')
		return Response({'from_form': from_form, 'to_form': to_form, 'parcel_form': parcel_form, 'shipments': shipments}, None, 'submit.html')
