import json
from django.test import TestCase
from django.test.client import Client
from scheduler.models import Reservation
from datetime import datetime, timedelta


class ReservationRequestTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.teh_future = (timedelta(days=10) + datetime.now())
        self.valid_component = {
            'content_type': 'application/x-markdown',
            'schema_name': 'article',
            'slug': 'example',
            'metadata': json.dumps({
                'title': 'Valid component'
            })
        }

    def test_make_reservation(self):
        response = self.client.post('/scheduler',
                                    {'slug': 'example',
                                     'datetime': datetime.now().isoformat()})
        self.assertEqual(response.status_code, 200)

    def test_make_reservation_invalid_slug(self):
        date = datetime.now().isoformat()
        response = self.client.post('/scheduler',
                                    {
                                        'slug': 'nope!!!',
                                        'datetime': date
                                    })
        self.assertEqual(response.status_code, 400)

    def test_make_reservation_invalid_date(self):
        date = datetime(1990, 1, 1).isoformat()
        response = self.client.post('/scheduler',
                                    {
                                        'slug': 'example',
                                        'datetime': date
                                    })
        self.assertEqual(response.status_code, 400)

    def test_change_reservation(self):
        r = Reservation(slug='example', datetime=self.teh_future)
        r.save()
        response = self.client.patch(
            '/scheduler/%s' % r.id,
             {
                'slug': 'example',
                'datetime': datetime.now().isoformat(),
                'reservation': r.id
             })
        self.assertEqual(response.status_code, 200)

    def test_change_reservation_invalid_slug(self):
        r = Reservation(slug='example', datetime=self.teh_future)
        r.save()
        response = self.client.patch('/scheduler/%s' % r.id,
                                    {
                                        'slug': 'notexample',
                                        'datetime': datetime.now().isoformat(),
                                        'reservation': r.id
                                    })
        self.assertEqual(response.status_code, 400)

    def test_change_reservation_invalid_date(self):
        r = Reservation(slug='example', datetime=self.teh_future)
        r.save()
        past_time = (timedelta(days=-10) + datetime.now()).isoformat()
        response = self.client.patch('/scheduler/%s' % r.id,
                {
                    'slug': 'example',
                    'datetime': past_time,
                    'reservation': r.id
                })
        self.assertEqual(response.status_code, 400)

    def test_delete_reservation(self):
        r = Reservation(slug='example', datetime=self.teh_future)
        r.save()
        response = self.client.delete('/scheduler/%s' % r.id)
        self.assertEqual(response.status_code, 204)

    def test_delete_reservation_invalid_slug(self):
        response = self.client.delete('/scheduler/squoodlydoo')
        self.assertEqual(response.status_code, 400)
