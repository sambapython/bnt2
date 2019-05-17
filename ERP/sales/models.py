from django.db import models

# Create your models here.
# create table customer(name varchar(250), address varchar(250), 
#gender varchar(1), cell int)
def gender_validation(value):
	if len(value)>2:
		raise Exception("exepcting only two digits")
	#if value not in ["M","F"]:
	#	raise Exception("Expeting only: M,F")


class Customer(models.Model):
	genders=[("M","MALE"),('F', 'FEMALE')]
	name = models.CharField(max_length=250)
	address = models.CharField(max_length=400, blank=True, null=True)
	gender = models.CharField(choices=genders, max_length=2, validators=(gender_validation,))
	cell = models.IntegerField(unique=True)
	email = models.EmailField(max_length=300, default="", null=True)

	def get_record(self):
		data = self.__dict__
		data.pop("_state",None)
		return data
		
class Sample(models.Model):
	id1 = models.IntegerField(primary_key=True)
	name=models.CharField(max_length=250)

