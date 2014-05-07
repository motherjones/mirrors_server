from django.test import TestCase
from scheduler.models import * 
from mirrors.models import *
from datetime import datetime, timedelta
import json

class MakeReservationTestCase(TestCase):
    def setUp(self):
        self.valid_component = {
            'content_type': 'application/x-markdown',
            'schema_name': 'article',
            'slug': 'example',
            'metadata': json.dumps({
                'title': 'Valid component'
            })
        }

    def test_make_reservation(self):
        self.assertTrue(Reservation(slug='example', datetime=datetime.now()))
    def test_make_reservation_invalid_slug(self):
        self.assertFalse(Reservation(slug='foobar', datetime=datetime.now()))
    def test_make_reservation_invalid_date(self):
        teh_past = timedelta(days=-1)
        self.assertFalse(Reservation(slug='example', datetime=teh_past))
    #def test_change_reservation(self):
    #    r = Reservation(slug='example', datetime=timedelta(days=10))
    #    r.datetime = datetime.now()
    #    self.assertTrue(r.save())
    #def test_change_reservation_invalid_slug(self):
    #    r = Reservation(slug='example', datetime=timedelta(days=10))
    #    r.slug = '_____'
    #    self.assertFalse(r.save())
    def test_change_reservation_invalid_date(self):
        r = Reservation(slug='example', datetime=timedelta(days=10))
        r.datetime = timedelta(days=-1)
        self.assertFalse(r.save())
    def test_delete_reservation(self):
        r = Reservation(slug='example', datetime=timedelta(days=10))
        self.assertTrue(r.delete())
    def test_delete_reservation_invalid_slug(self):
        self.fail("pending")

