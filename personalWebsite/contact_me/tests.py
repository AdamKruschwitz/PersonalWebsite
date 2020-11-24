from django.test import TestCase
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .forms import ContactMeForm


class ContactMeFormUnitTests(TestCase):
    def test_no_input(self):
        """
        If no Subject, From, or Body is included, do not send message and
        return a special error.
        """

        form = ContactMeForm({
            'from_email': "",
            'subject': "",
            'body': "",
        })

        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'from_email': "From Address Required",
            'subject': "Subject Required",
            'body': "Body Required",
        })


    def test_no_from_input(self):
        """
        If no From is included, do not send message and return an error
        """

        form = ContactMeForm({
            'from_email': "",
            'subject': "Subject",
            'body': "Body",
        })

        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'from_email': "From Address Required"
        })


    def test_no_body_input(self):
        """
        If no body is included, do not send message and return an error
        """

        form = ContactMeForm({
            'from_email': "from@test.com",
            'subject': "Subject",
            'body': ""
        })

        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'body': "Body Required",
        })


    def test_no_subject_input(self):
        """
        If no subject is included, do not send message and return an error
        """

        form = ContactMeForm({
            'from_email': "from@test.com",
            'subject': "",
            'body': "Body",
        })

        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'subject': "Subject Required"
        })


    def test_all_fields_input(self):
        """
        If all fields are included and the from email is valid, send the message
        """

        form = ContactMeForm({
            'from_email': "from@test.com",
            'subject': "Subject",
            'body': "Body",
        })

        self.assertTrue(form.is_valid())

    def test_invalid_from_email(self):
        """
        If all fields are included and the from email is invalid, do not send
        the message and send an error message
        """

        form = ContactMeForm({
            'from_email': "from.com",
            'subject': "Subject",
            'body': "Body",
        })

        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'from_email': "Valid email required"
        })


class ContactMeViewIntegrationTests(TestCase):

    def test_get(self):
        """
        When request is a GET, get the contact form
        """
        response = self.client.get(reverse('contact_me:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Contact Me")

    def test_post_valid(self):
        """
        When request is a POST and all valid info is included, send a message
        """
        response = self.client.post(
            reverse('contact_me:contact'),
            data = {
                'from_email': "from@test.com",
                'subject': "Subject",
                'body': "Body"
            }
        )
        self.assertEqual(response.status_code, 302) #Found status code
        self.assertEqual(response["Location"], reverse('contact_me:success'))
        self.assertContains(response, "Message sent successfully!")

    def test_post_missing_from(self):
        """
        When request is a POST and from info is missing, return an error and
        redirect to contact me page
        """
        response = self.client.post(
            reverse('contact_me:contact'),
            data = {
                'from_email': "",
                'subject': "Subject",
                'body': "Body"
            }
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "From Required")

    def test_post_missing_subject(self):
        """
        When request is a POST and subject info is missing, return an error and
        redirect to contact me page
        """
        response = self.client.post(
            reverse('contact_me:contact'),
            data = {
                'from_email': "from@test.com",
                'subject': "",
                'body': "Body"
            }
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Subject Required")

    def test_post_missing_body(self):
        """
        When request is a POST and body info is missing, return an error and
        redirect to contact me page
        """
        response = self.client.post(
            reverse('contact_me:contact'),
            data = {
                'from_email': "from@test.com",
                'subject': "Subject",
                'body': ""
            }
        )

        self.assertEqual(response.status_code, 200)
        self.assertContins(response, "Body Required")

    def test_post_invalid_from_email(self):
        """
        When request is a POST and from email is invalid, return an error and
        redirect to contact me page
        """
        response = self.client.post(
            reverse('contact_me:contact'),
            data = {
                'from_email': "from.com",
                'subject': "Subject",
                'body': "Body"
            }
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Valid email required")
