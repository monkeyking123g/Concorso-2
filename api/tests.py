from django.contrib.auth import get_user_model
from django.http import response
from django.utils import timezone
from rest_framework.test import APIRequestFactory

factory = APIRequestFactory()
request = factory.post('/notes/', {'title': 'new idea'})

from django.test import Client, TestCase

from django.urls import reverse

from .models import Concorso, Prize, User, Winer

class UserTests(TestCase):

    def setUp(self):

        self.prize = Prize.objects.create(
             code = 'Test code',
             perday = 29,
             name = 'test name', 
        )

        self.winer = Winer.objects.create(
             winner = False,
             prize = self.prize,
        )

        self.user = User.objects.create(
            name = 'A good title',
            email = 'dima@gmail.com',
            max_win = 12,
            win = self.winer,   
        )
        self.concorso = Concorso.objects.create(
            code = 'C0001',
            name = 'Concorso',
            start = timezone.now(),
            end = timezone.now(),
            prize = self.prize,   
        )

    
    def test_prize_content(self):
        self.assertEqual(f'{self.prize.code}', 'Test code')
        self.assertEqual(self.prize.perday, 29)
        self.assertEqual(f'{self.prize.name}', 'test name')
    
    def test_winer_content(self):
        self.assertEqual(self.winer.winner, False)
        self.assertEqual(self.winer.prize, self.prize)
       

    def test_user_content(self):

        self.assertEqual(f'{self.user.name}', 'A good title')
        self.assertEqual(f'{self.user.email}', 'dima@gmail.com'),
        self.assertEqual(self.user.max_win, 12)
        self.assertEqual(self.user.win, self.winer)
    
    def test_concorso_content(self):
        self.assertEqual(f'{self.concorso.code}', 'C0001'),
        self.assertEqual(f'{self.concorso.name}', 'Concorso')
        self.assertEqual(self.concorso.start, self.concorso.start)
        self.assertEqual(self.concorso.end, self.concorso.end)
        self.assertEqual(self.concorso.prize, self.prize)
    
    def test_post_detail_view(self):
        response = self.client.get('/play/1/')
        self.assertEqual(response.status_code, 401)
    
    def test_concorso_detail_view(self):
        responses = self.client.get('/concorso/1/')
        response = self.client.get('/concorso/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(responses.status_code, 405)
    
    def test_winer_detail_view(self):
        responses = self.client.get('/winer/1/')
        response = self.client.get('/winer/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(responses.status_code, 405)
    
    def test_user_detail_view(self):
        response = self.client.get('/user/')
        self.assertEqual(response.status_code, 403)
    
    def test_prize_detail_view(self):
        responses = self.client.get('/peize/12/')
        response = self.client.get('/prize/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(responses.status_code, 404)
    
    def test_google_detail_view(self):
        response = self.client.get('/google/')
        self.assertEqual(response.status_code, 405)
    
    def test_post_winer_questions(self):
       
        response = self.client.post(reverse('winer'),{
            'winner' : True,
            'prize': '',
        })
        self.assertEqual(response.status_code, 201)
    
    def test_post_winer_questions(self):
     
        response = self.client.post(reverse('winer'),{
            'winner' : True,
            'prize': '',
        })
        self.assertEqual(response.status_code, 201)
    
    def test_post_concorso_questions(self):
        response = self.client.post(reverse('concorso'),{
            'user' : self.user,
            'code' : 'C0001',
            'name' :'Concorso',
            'start' : timezone.now(),
            'end'  : timezone.now(),
            'prize' : self.prize,
        })
        self.assertEqual(response.status_code, 400)
      
      
      
        
      
   


