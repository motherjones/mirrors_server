from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse
from scheduler.models import Reservation
from mirrors.models import Component
from datetime import datetime, timedelta
import json


class ReservationRequestTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.teh_future = (timedelta(days=10) + datetime.utcnow())
        self.valid_component = Component(
            content_type='application/x-markdown',
            schema_name='article',
            slug='example'
        ).save()

    def test_make_reservation(self):
        response = self.client.post(reverse('reservation-list'),
                                    {'slug': 'example',
                                     'datetime': datetime.now().isoformat()})
        self.assertEqual(response.status_code, 201)

    def test_make_reservation_invalid_slug(self):
        date = datetime.now().isoformat()
        response = self.client.post(reverse('reservation-list'), {
            'slug': 'nope!!!',
            'datetime': date
        })
        self.assertEqual(response.status_code, 400)

    def test_make_reservation_invalid_date(self):
        date = datetime(1990, 1, 1).isoformat()
        response = self.client.post(reverse('reservation-list'), {
            'slug': 'example',
            'datetime': date
        })
        self.assertEqual(response.status_code, 400)

    def test_change_reservation(self):
        r = Reservation(slug='example', datetime=self.teh_future)
        r.save()
        url = reverse('reservation-detail', args=[r.id])
        data = {
            'slug': 'example',
            'datetime': datetime.now().isoformat(),
        }
        # /me flips table
        response = self.client.patch(url, json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_change_reservation_with_single_field(self):
        r = Reservation(slug='example', datetime=self.teh_future)
        r.save()
        response = self.client.patch('/scheduler/%s' % r.id, {
            'datetime': datetime.now().isoformat(),
        })
        self.assertEqual(response.status_code, 200)

    def test_change_reservation_invalid_slug(self):
        r = Reservation(slug='example', datetime=self.teh_future)
        r.save()
        response = self.client.patch('/scheduler/%s' % r.id, {
            'slug': 'notexample',
            'datetime': datetime.now().isoformat(),
            'reservation': r.id
        })
        self.assertEqual(response.status_code, 400)

    def test_change_reservation_invalid_date(self):
        r = Reservation(slug='example', datetime=self.teh_future)
        r.save()
        past_time = (timedelta(days=-10) + datetime.now()).isoformat()
        response = self.client.patch('/scheduler/%s' % r.id, {
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
