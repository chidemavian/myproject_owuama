# Create your views here.
from django.shortcuts import render_to_response
from myproject.geo.forms import *
from myproject.geo.models import *
from decimal import *
import math
from django.http import  Http404, HttpResponseRedirect, HttpResponse
import locale
locale.setlocale(locale.LC_ALL,'')

def indexes(request):
        return render_to_response('owuama.html')

def geotech(request):
        return render_to_response('geo/success.html')

def bch(request):
	if request.method =='POST':
		form=bearingcapacity(request.POST)
		if form.is_valid():
			nc = form.cleaned_data['nc']
			nq= form.cleaned_data['nq']
			nr = form.cleaned_data['nr']
			foundation= form.cleaned_data['foundation']
			cohession = form.cleaned_data['cohesion']
			off1= form.cleaned_data['off1']
			r1=form.cleaned_data['r1']
			r2=form.cleaned_data['r2']
			off1=(off1)
			off2= form.cleaned_data['off2']
			b = form.cleaned_data['b']
			d= form.cleaned_data['d']
			if foundation == '----':
				return HttpResponseRedirect('/login/')
			if foundation=='Strip':
				alpha =1.0
				beta = 0.5
			elif foundation == 'Square':
				alpha = 1.3
				beta=0.4
			elif foundation == 'Circular':
				alpha = 1.3
				beta=0.3

			b1=b
			b2=b+off1
			b3=b+(2*off1)
			b4=b+(3*off1)
			b5=b+(4*off1)
			myb=[b1,b2,b3,b4,b5]

			d1=d
			d2=d+off2
			d3=d+(2*off2)
			d4=d+(3*off2)
			d5=d+(4*off2)
			myd=[d1,d2,d3,d4,d5]

			tblgeo.objects.all().delete()
			for d in myd:
				A =Decimal(alpha)*cohession*nc
				B = d* r1*nq
				for j in myb:
					C = Decimal(beta)*j*r2*nr
					qu = Decimal(A+B+C)
					tblgeo(nc=nc,nq=nq,nr=nr,cohession=cohession,qu=str(round(qu,2)),d=d,b=j,r1=r1,r2=r2).save()
				# qu=locale.format("%.2f",qu,grouping=True),d=d,b=j,r1=r1,r2=r2).save()
					

			data=tblgeo.objects.filter(cohession=cohession)

			return  render_to_response('geo/bc_results.html',{'f':myd,'b':data,'g':myb})
		else:
			return HttpResponseRedirect('/geo/bearingcapacity/')

	else:
		form=bearingcapacity()
	return render_to_response('geo/bc.html',{'form':form})




def ech(request):
	if request.method =='POST':
		form = endbearingcapacity(request.POST)
		if form.is_valid():
			nc = form.cleaned_data['nc']
			nq= form.cleaned_data['nq']
			nr = form.cleaned_data['nr']
			cohession = form.cleaned_data['cohesion']
			off1= form.cleaned_data['off1']
			r1=form.cleaned_data['r1']
			off2= form.cleaned_data['off2']
			b = form.cleaned_data['b']
			d= form.cleaned_data['d']

			b1=b
			b2=b+off1
			b3=b+(2*off1)
			b4=b+(3*off1)
			b5=b+(4*off1)
			myb=[b1,b2,b3,b4,b5]

			d1=d
			d2=d+off2
			d3=d+(2*off2)
			d4=d+(3*off2)
			d5=d+(4*off2)
			myd=[d1,d2,d3,d4,d5]
			tblendbearing.objects.all().delete()
			for d in myd:
				A =cohession*nc
				B = d* r1*nq
				for j in myb:
					C =Decimal(0.4)*j*r1*nr
					qu = Decimal(A+B+C)                                                           
					tblendbearing(nc=nc,nq=nq,nr=nr,cohession=cohession,qu=str(round(qu,2)),d=d,b=j,r1=r1).save()


			data=tblendbearing.objects.filter(cohession=cohession)

			return  render_to_response('geo/ebc_results.html',{'f':myd,'b':data,'g':myb})

		else:
			return HttpResponseRedirect('/geo/endbearingcapacity/')
	


	else:
		form=endbearingcapacity()
		return render_to_response('geo/ebc.html',{'form':form})

def sc(request):
	if request.method =='POST':
		form = skincapacity(request.POST)
		if form.is_valid():
			unit = form.cleaned_data['unit']
			friction= form.cleaned_data['friction']
			adhession = form.cleaned_data['adhession']
			frictionangle = form.cleaned_data['frictionangle']
			off2= form.cleaned_data['off2']
			d= form.cleaned_data['d']

			d1=d
			d2=d+off2
			d3=d+(2*off2)
			d4=d+(3*off2)
			d5=d+(4*off2)
			myd=[d1,d2,d3,d4,d5]
			tblskincapacity.objects.all().delete()

			d=  Decimal(math.tan(frictionangle))

			A= unit * Decimal(math.tan(friction))

			B= unit * Decimal(math.sin(frictionangle)) * Decimal(math.tan(friction))

			C=adhession

			D = A + C -B

			for jd in myd:
				qs = D*jd
				tblskincapacity(unit=unit,friction=friction,adhession=adhession,frictionangle=frictionangle,qs=str(round(qs,2)),d=jd).save()


			data=tblskincapacity.objects.filter(friction=friction)

			return  render_to_response('geo/sc_result.html',{'f':D,'b':data})



		else:
			return HttpResponseRedirect('/geo/skincapacity/')
			
	else:
		form=skincapacity()
		return render_to_response('geo/sc.html',{'form':form})




def s(request):
	if request.method =='POST':
		form = settlement(request.POST)
		if form.is_valid():
			compression=form.cleaned_data['compression']
			void=form.cleaned_data['void']
			unit=form.cleaned_data['unit']
			thick =form.cleaned_data['thick']
			off1 = form.cleaned_data['off1']
			off2 =form.cleaned_data['off2']
			d = form.cleaned_data['d']
			pressure= form.cleaned_data['pressure']

			b=pressure
			b1=b
			b2=b+off2
			b3=b+(2*off2)
			b4=b+(3*off2)
			b5=b+(4*off2)
			myb=[b1,b2,b3,b4,b5]

			d1=d
			d2=d+off1
			d3=d+(2*off1)
			d4=d+(3*off1)
			d5=d+(4*off1)
			myd=[d1,d2,d3,d4,d5]

			tblsettlement.objects.all().delete()
	
			
			for df in myd:
				for bf in myb:
					A = (compression * thick) / (1+void)
					B = (unit * df) + bf
					C = B / (unit*df)
					s = A * Decimal(math.log10(C))

					tblsettlement(thick=thick,off2=off2,off1=off1,pressure=bf, compression=compression,void=void,unit=unit,qs=str(round(s,2)),d=df).save()


			data=tblsettlement.objects.filter(compression=compression)

			return  render_to_response('geo/s_result.html',{'b':data})

			
		else:
			return HttpResponseRedirect('/geo/settlement/')

	else:
		form=settlement()
		return render_to_response('geo/s.html',{'form':form})


