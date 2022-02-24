
from django.db import models

class Prize(models.Model):
    """ Model Prize
    """
    code = models.CharField(max_length=200)
    perday = models.IntegerField(default=0)
    name = models.CharField(max_length=300)

    def __str__(self) -> str:
        return f'{self.code}'


class Winer(models.Model):
    """ Model for winner"""
    winner = models.BooleanField(default=False)
    prize = models.ForeignKey(Prize, on_delete=models.SET_NULL, related_name='winner', blank=True, null= True)

    def __str__(self) -> str:
        return f'{self.winner}, {self.prize}'


class User(models.Model):
    """ Model for user  """
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=150, unique=True)
    max_win = models.IntegerField(default=0)
    win = models.ForeignKey(Winer,on_delete=models.SET_NULL, blank=True, null=True)

    @property
    def is_authenticated(self):
        """ Return True  if user authenticated"""
        return True

    def __str__(self) -> str:
        return self.email 
 
class Concorso(models.Model):
    """Model for concorso"""
    user = models.ManyToManyField(User, related_name='concors')
    code = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=200, null=True)
    start = models.DateTimeField(auto_now_add=True)
    end = models.DateTimeField()
    prize = models.ForeignKey(Prize, on_delete=models.SET_NULL, related_name='prizes', null=True, blank=True)
   


 

    
