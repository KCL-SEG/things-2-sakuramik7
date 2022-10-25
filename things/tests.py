from django.test import TestCase
from django import forms
from things.forms import ThingForm

# Create your tests here.
class TestThingForm(TestCase):
    def setUp(self):
        self.form_input = {'name' : 'Jane', 'description': 'Object which peels potatos', 'quantity': 3}

    def test_form_contains_required_fields(self):
        form = ThingForm()
        self.assertIn('name', form.fields)
        self.assertIn('description', form.fields)
        self.assertIn('quantity', form.fields)
        description_widget = forms.fields['description'].widgets
        self.assertTrue(isinstance(description_widget, forms.Textarea))

    def test_form_accepts_valid_input(self):
        form = ThingForm(data=self.form_input)
        self.assertTrue(form.is_valid())

    def test_form_rejects_empty_name(self):
        self.form_input['name'] = ''
        form = ThingForm(data=self.form_input)
        self.assertFalse(form.is_valid())

    def test_form_rejects_low_quantity(self):
        self.form_input['quantity'] = -3
        form = ThingForm(data=self.form_input)
        self.assertFalse(form.is_valid())

    def test_form_rejects_high_quantity(self):
        self.form_input['quantity'] = 333
        form = ThingForm(data=self.form_input)
        self.assertFalse(form.is_valid())

    def test_form_has_description_field(self):
        form = ThingForm()
        self.assertIn('description', form.fields.keys())
        field = form.fields['description']
        self.assertTrue(isinstance(field.widget, forms.Textarea))

    # def tes_form_description_widget(self):
    #     form = ThingForm()
    #     description_widget = forms.fields['description'].widget
    #     self.assertTrue(isinstance(description_widget, forms.Textarea))
