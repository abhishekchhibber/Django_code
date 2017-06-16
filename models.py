## Fintech Segment

class fin_Segment(models.Model):
	segment = models.CharField(max_length=100)
	class Meta:
	        ordering = ('segment',)
	def __str__(self):
		return self.segment



## Fintech Country

class fin_Country(models.Model):
	country = models.CharField(max_length=100)
	continent = models.CharField(max_length=100)

	class Meta:
	        ordering = ('country',)


	def __str__(self):
		return self.country+" : "+self.continent


## Fintech Organization

class fin_Organization(models.Model):
	orgnization_name = models.CharField(max_length=250)
	orgnization_segment = models.ManyToManyField(fin_Segment, blank=True)
	orgnization_country = models.ManyToManyField(fin_Country)

	class Meta:
	        ordering = ('orgnization_name',)

	def __str__(self):
		return self.orgnization_name
