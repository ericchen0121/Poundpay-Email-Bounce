import app
import unittest

class TestEmailBounceFunction(unittest.TestCase):
    def setUp(self):
        self.payment_sid = 'PY436d63cab9ad11e081291231400042c7'
        self.app = app.app.test_client()

    def test_email_bounce(self):
        '''Check to see email bounce callback works'''
        rv = self.app.post('/email/bounce', data={
            'Message-ID':self.payment_sid
        }, follow_redirects=True)
        #print rv.data #debug
        assert 'ESCROWED' in rv.data

        
if __name__ == '__main__':
    unittest.main()