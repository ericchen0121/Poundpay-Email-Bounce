import app
import unittest

class TestEmailBounceFunction(unittest.TestCase):
    def setUp(self):
        self.payment_sid = 'PY436d63cab9ad11e081291231400042c7'

    def test_email_bounce(self):
        '''Check to see email bounce callback works'''
        test = app.app.post('/email/bounce', data = {'Message-ID':self.payment_sid})
        self.assertEqual(payment.status, 'ESCROWED')

        
if __name__ == '__main__':
    unittest.main()