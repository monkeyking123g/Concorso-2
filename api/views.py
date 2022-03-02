from django import views
from django.conf import settings
from datetime import datetime, timedelta
from rest_framework import exceptions
from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import generics, viewsets, parsers, views, permissions
from rest_framework.response import Response


from . import serializer
from . import models
from base.classes import MixedSerializer
from base.permission import IsAuthor




class UserView(viewsets.ModelViewSet):
    parser_calsses = (parsers.MultiPartParser,)
    serializer_class = serializer.UserSerializer
    #permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
       
        return self.request.user
    
    def get_object(self):
        return self.get_queryset()

class PrizeView(generics.ListAPIView):
    queryset = models.Prize.objects.all()
  
    serializer_class = serializer.PrizeSerializer
   
class ConcorsoView(MixedSerializer, viewsets.ModelViewSet):
    serializer_class = serializer.ConcorsoSerializer
    serializer_classes_by_action = {
        'list' :serializer.ConcorsoListSerializer
    }
    def get_queryset(self):
        return models.Concorso.objects.all()
    
class WinerView(viewsets.ModelViewSet):
    serializer_class = serializer.WinerSerializer

    def get_queryset(self):
        return models.Winer.objects.all()

class PlayView(views.APIView):
    # defult= off ,  if on  alone is Author play 
    #permission_classes = [IsAuthor]

    def time(self):
        """ Tempo per una vincita """
        un_day = 60 * 24
        x =  un_day / 35
        times =  timezone.now() + timedelta(minutes=x)
       
        return times                                                                          

    
    TIME = timezone.now()  - timedelta(minutes=15) # defolt time 

    def set_play(self, concorso):
        # if win, concorso prize -1
        concorso.prize.perday -= 1
        concorso.prize.save()

    def random(self):
        import random
        randoms = random.randint(1, 10) 
        if randoms == 5:
            return True
        else:
            return False
    
    def user_vin(self, concorso):
        # if user win, max_win -1
        concorso.max_win += 1
        concorso.save()
       
    def get(self, request, pk):
        try:
            now = timezone.now() 
            concorso = get_object_or_404(models.Concorso, id=pk, user = request.user)
            if concorso.code != None:
                if concorso.end > now:
                    if concorso.prize.perday <= 0:
                        return Response(f'finiti concorsi {concorso.prize.perday}')
                    chance = concorso.prize.perday # chance for winner 
                    for b in concorso.user.all():
                        if b == request.user:
                            if b.max_win < 3:
                                win = self.random() # chance for winner
                                b.win.winner = win # True or False
                                b.win.save()
                         
                                if b.win.winner == True and now >  PlayView.TIME:
                                    b.win.prize = concorso.prize
                                    b.win.save()
                                    PlayView.TIME = self.time()
                                    self.set_play(concorso)
                                    self.user_vin(b)
                                    context = {'winner': b.win.winner,'prize': b.win.prize} 
                                    return Response(f'congratulation {context}--{PlayView.TIME}', status=200)
                                else:
                                    b.win.prize = None
                                    b.win.save()
                                    context = {'winner': b.win.winner,'prize': b.win.prize,}
                                    return Response(f'Not win {context}--{PlayView.TIME}', status=200)
                            else:
                                return Response(f'Your maxwin > 3 : " {request.user}"  :)', status=200) 
                            
                else:
                    return Response(f'Contest in not active  code: "{concorso.code}"', status=422)
            else:
                return Response(f'Contest code missing { concorso.code }', status=400)

        except TypeError:
            return Response("Richiesta non autenticata", status=401)
        

        
        
                                                                                   



