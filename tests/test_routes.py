from app import app
from unittest import TestCase

app.config['TESTING'] = True
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar'] 

class ConverterRoutesTestCase(TestCase):
    def test_index(self):
        """Tests if index route is followed correctly"""
        with app.test_client() as client:
            res = client.get('/')
            html = res.get_data(as_text = True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<h1>Forex Converter</h1>', html)

    def test_post_with_valid_info(self):
        """ Test to see if when post route is followed, passed in data makes it to the html as intended """
        with app.test_client() as client:
            res = client.post('/', data={'curr-from': 'MXN', 'curr-to': 'MXN', 'amt':'20'})
            html = res.get_data(as_text = True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('$20.00', html)

    def test_post_with_invalid_info(self):
        """ Test to see if redirect code is received when invalid currency code is passed """
        with app.test_client() as client:
            res = client.post('/', data={'curr-from': 'ABC', 'curr-to': 'MXN', 'amt':'20'})

            self.assertEqual(res.status_code, 302)
        
    def test_invalid_code_redirect_with_flash(self):
        """ Test to see if redirect is followed to correct page when invalid currency code is passed """
        with app.test_client() as client:
            res = client.post('/', data={'curr-from': 'ABC', 'curr-to': 'MXN', 'amt':'20'}, follow_redirects= True)

            html = res.get_data(as_text = True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('currency code is not valid', html) #proper flash msg displayed

    def test_invalid_amt_redirect_with_flash(self):
        """ Test to see if redirect is followed to correct page when invalid amount is passed """
        with app.test_client() as client:
            res = client.post('/', data={'curr-from': 'USD', 'curr-to': 'MXN', 'amt':'ten'}, follow_redirects= True)

            html = res.get_data(as_text = True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('enter a valid currency amount', html) #proper flash msg displayed

    def test_missing_info_redirect_with_flash(self):
        """ Test to see if redirect is followed to correct page when form is missing information"""
        with app.test_client() as client:
            res = client.post('/', data={'curr-from': 'None', 'curr-to': 'MXN', 'amt':'ten'}, follow_redirects= True)

            html = res.get_data(as_text = True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('currency code is not valid', html) #proper flash msg displayed