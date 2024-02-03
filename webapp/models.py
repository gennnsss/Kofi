from django.db import models

class Customer(models.Model):
    pen_name = models.CharField(max_length=50, null=True )
    name = models.CharField(max_length=50, null=True )
    email = models.EmailField(max_length=50, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    
    def _str_(self):
        return self.name

class Product(models.Model):
    Category = models.CharField(max_length=30, null=True)
    Size = models.CharField(max_length=30, blank=True)
    Price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    Quantity = models.PositiveIntegerField(null=True)
    Addons = models.TextField(null=True)

    def __str__(self):
        return self.Category       


class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    ]

    customer_name = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    Product = models.ManyToManyField(Product, related_name='Product')


    def __str__(self):
        return f"Orders #{self.id} - {self.customer_name}"
    
    
class Return(models.Model):
     customer_name = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
     order_list = models.ManyToManyField(Product)
     reason =  models.TextField(null=True)
     
     def _str_(self):
        return self.customer_name

class Payment(models.Model):
    customer_name = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    ordered_list = models.ManyToManyField(Product, related_name='product')
    ordered_date = models.DateField(null=True)

def _str_(self):
        return self.Payment

class Review(models.Model):
      Feedback = models.TextField(null=True)
      
      def _str_(self):
        return self.Feedback