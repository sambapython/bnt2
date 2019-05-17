from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from sales.models import Customer

# Create your views here.
class CustomerView(APIView):
	def post(self, request, format=None):
		# insrted details
		data = request.data
		print("data:::::",data)
		'''
		cust = Customer(name=data["name"],
			address=data["address"],
			gender=data["gender"],
			cell=data["cell"],
			email=data["email"],)
		'''
		try:
		    cust=Customer(**data)
		    cust.save()
		    msg="customer created successfully"
		    sta = status.HTTP_200_OK
		except Exception as err:
			msg= str(err)
			sta = status.HTTP_400_BAD_REQUEST

		return Response(msg, status=sta)
	def get(self, request, format=None):
		records = Customer.objects.all()
		data = [rec.get_record() for rec in records]
		return Response(data)
	def put(self, request, pk, format=None):
		return Response("customer updated successfully")
	def delete(self, request, pk, format=None):
		try:
			rec = Customer.objects.get(id=pk)
			record_details = rec.delete()
			msg = f"{pk} deleted successfully"
			sta = status.HTTP_200_OK
		except Exception as err:
			msg = str(err)
			sta = status.HTTP_400_BAD_REQUEST
		return Response(msg, status=sta)

def home_view1(request):
	return render(request, "home.html")
def home_view(request):
	resp = """
	<!DOCTYPE html>
<html lang="en">
<head>
  <title>Bootstrap Example</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.0/jquery.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
</head>
<body style="height:1500px">

<nav class="navbar navbar-expand-sm bg-dark navbar-dark fixed-top">
  <a class="navbar-brand" href="#">Logo</a>
  <ul class="navbar-nav">
    <li class="nav-item">
      <a class="nav-link" href="#">Link</a>
    </li>
    <li class="nav-item">
      <a class="nav-link" href="#">Link</a>
    </li>
  </ul>
</nav>

<div class="container-fluid" style="margin-top:80px">
  <h3>Top Fixed Navbar</h3>
  <p>A fixed navigation bar stays visible in a fixed position (top or bottom) independent of the page scroll.</p>
  <h1>Scroll this page to see the effect</h1>
</div>

</body>
</html>
	"""
	return HttpResponse(resp)
def fun(request):
	
	return HttpResponse("<h1>available: 30 GB, used:40 GB</h1>")
