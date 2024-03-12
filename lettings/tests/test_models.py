from django.test import TestCase
from lettings.models import Letting, Address


class LettingModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        address = Address.objects.create(number='8', street="rue", city="stchamand",
        state="avignon", zip_code="84000", country_iso_code="country")
        Letting.objects.create(title='Big', address=address)

    def test_title_label(self):
        letting = Letting.objects.get(id=1)
        field_label = letting._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_title_type(self):
        title_type = Letting._meta.get_field("title").get_internal_type()
        self.assertEqual(title_type, 'CharField')

    def test_title_value(self):
        letting = Letting.objects.get(id=1)
        self.assertEqual(letting.title, 'Big')

    def test_address_label(self):
        letting = Letting.objects.get(id=1)
        field_label = letting._meta.get_field('address').verbose_name
        self.assertEqual(field_label, "address")

    def test_address_value(self):
        letting = Letting.objects.get(id=1)
        address = Address.objects.get(id=1)
        self.assertEqual(letting.address, address)

    def test_address_type(self):
        address_type = Letting._meta.get_field("address").get_internal_type()
        self.assertEqual(address_type, 'OneToOneField')


class AddressModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        address = Address.objects.create(number=8, street="rue",
        city="stchamand", state="avignon", zip_code="84000", country_iso_code="country")
        Letting.objects.create(title='Big', address=address)

    def test_number_label(self):
        address = Address.objects.get(id=1)
        field_label = address._meta.get_field('number').verbose_name
        self.assertEqual(field_label, 'number')

    def test_number_value(self):
        address = Address.objects.get(id=1)
        self.assertEqual(address.number, 8)

    def test_number_type(self):
        number_type = Address._meta.get_field("number").get_internal_type()
        self.assertEqual(number_type, 'PositiveIntegerField')

    def test_street_label(self):
        address = Address.objects.get(id=1)
        field_label = address._meta.get_field('street').verbose_name
        self.assertEqual(field_label, 'street')

    def test_street_value(self):
        address = Address.objects.get(id=1)
        self.assertEqual(address.street, "rue")

    def test_street_type(self):
        street_type = Address._meta.get_field("street").get_internal_type()
        self.assertEqual(street_type, 'CharField')

    def test_city_label(self):
        address = Address.objects.get(id=1)
        field_label = address._meta.get_field('city').verbose_name
        self.assertEqual(field_label, 'city')

    def test_city_value(self):
        address = Address.objects.get(id=1)
        self.assertEqual(address.city, 'stchamand')

    def test_city_type(self):
        city_type = Address._meta.get_field("city").get_internal_type()
        self.assertEqual(city_type, 'CharField')

    def test_state_label(self):
        address = Address.objects.get(id=1)
        field_label = address._meta.get_field('state').verbose_name
        self.assertEqual(field_label, 'state')

    def test_state_value(self):
        address = Address.objects.get(id=1)
        self.assertEqual(address.state, 'avignon')

    def test_state_type(self):
        state_type = Address._meta.get_field("state").get_internal_type()
        self.assertEqual(state_type, 'CharField')

    def test_zip_code_label(self):
        address = Address.objects.get(id=1)
        field_label = address._meta.get_field('zip_code').verbose_name
        self.assertEqual(field_label, 'zip code')

    def test_zip_code_value(self):
        address = Address.objects.get(id=1)
        self.assertEqual(address.zip_code, 84000)

    def test_zip_code_type(self):
        zip_code_type = Address._meta.get_field("zip_code").get_internal_type()
        self.assertEqual(zip_code_type, 'PositiveIntegerField')

    def test_country_iso_code_label(self):
        address = Address.objects.get(id=1)
        field_label = address._meta.get_field('country_iso_code').verbose_name
        self.assertEqual(field_label, 'country iso code')

    def test_country_iso_code_value(self):
        address = Address.objects.get(id=1)
        self.assertEqual(address.country_iso_code, 'country')

    def test_country_iso_code_type(self):
        country_iso_code_type = Address._meta.get_field("country_iso_code").get_internal_type()
        self.assertEqual(country_iso_code_type, 'CharField')