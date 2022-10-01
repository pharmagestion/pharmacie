from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.

class UsersManagerTest(TestCase):

    def setUp(self):
        self.account    = get_user_model()
        self.pharmacist =  self.account.objects.create_user('pharmacist', 'pharma224@224', user_type='pharmacist')
        self.admin      =  self.account.objects.create_user('admin', 'admin224@224', user_type='admin')
        self.vigile     =  self.account.objects.create_user('vigile', 'vigile224@224', user_type='vigile')
        self.superuser  = self.account.objects.create_superuser('superuser', '621481439')
        
    
    def test_create_user(self):
        pharmacist = self.pharmacist
        self.assertEqual('pharmacist', pharmacist.username)
        self.assertEqual('pharmacist', pharmacist.user_type)
        self.assertTrue(isinstance(pharmacist, get_user_model()))
        self.assertTrue(pharmacist.is_active == True)
        self.assertTrue(pharmacist.is_staff == False)
        self.assertTrue(pharmacist.is_superuser == False)

        # test for an admin
        admin = self.admin
        self.assertEqual('admin', admin.username)
        self.assertEqual('admin', admin.user_type)
        self.assertTrue(isinstance(admin, get_user_model()))
        self.assertTrue(pharmacist.is_active == True)
        self.assertTrue(pharmacist.is_staff == False)
        self.assertTrue(pharmacist.is_superuser == False)

        # test for a vigile
        vigile = self.vigile
        self.assertEqual('vigile', vigile.username)
        self.assertEqual('vigile', vigile.user_type)
        self.assertTrue(isinstance(admin, get_user_model()))
        self.assertTrue(vigile.is_active == False)
        self.assertTrue(vigile.is_staff == False)
        self.assertTrue(vigile.is_superuser == False)

    
    def test_create_superuser(self):
        superuser = self.superuser
        self.assertEqual('superuser', superuser.username)
        self.assertTrue(superuser.is_active == True)
        self.assertTrue(superuser.is_superuser == True)
        self.assertTrue(superuser.is_staff == True)
    

class UsersViewTest(TestCase):
    pass