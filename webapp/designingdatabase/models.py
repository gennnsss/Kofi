from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=50, null=True )
    phone = models.IntegerField(blank=True)
    email = models.EmailField(max_length=50, blank=True)
    date_created = models.DateField(auto_now_add=True)

    def _str_(self):
        return self.name

class Product(models.Model):
    category = models.CharField(max_length=30, null=True)
    flavor = models.CharField(max_length=30, null=True)
    size = models.CharField(max_length=30, blank=True)
    amount = models.IntegerField(null=True)
    addons = models.TextField(max_length=30, null=True)
    description = models.TextField(null=True)


    def __str__(self):
        return self.category       

class Group(models.Model):
     name = models.CharField(max_length=50, null=True)    
     description = models.TextField(null=True)
     started_date = models.DateField(null=True)
     
     def _str_(self):
        return self.name

class Order(models.Model):
    name = models.CharField(max_length=50, null=True)
    size = models.CharField(max_length=30, blank=True)
    amount = models.IntegerField(null=True)
    group = models.ManyToManyField(Group, related_name='orders')

    def _str_(self):
        return self.name

class Return(models.Model):
     category = models.CharField(max_length=30, null=True)
     size = models.CharField(max_length=30, blank=True)
     flavor = models.CharField(max_length=30, null=True)
     amount = models.IntegerField(blank=True)
     reason =  models.TextField(null=True)
     date = models.DateField(auto_now_add=True)
     time = models.TimeField(auto_now_add=True)
     group = models.ManyToManyField(Group, related_name='returns')


     def _str_(self):
        return self.date


class Review(models.Model):      
      Feedback = models.TextField(null=True)
      
      def _str_(self):
        return self.Feedback


class Payment(models.Model):
    payment = models.PositiveIntegerField(null=True)
    name = models.CharField(max_length=50, null=True )
    phone = models.IntegerField(blank=True)
    amount = models.IntegerField(blank=True) 
    date_created = models.DateTimeField(auto_now_add=True)

def _str_(self):
        return self.payment
