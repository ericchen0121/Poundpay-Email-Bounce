import app
import unittest

class TestEmailBounceFunction(unittest.TestCase):
    def setUp(self):
        self.payment_sid = 'PY436d63cab9ad11e081291231400042c7'
        self.app = app.app.test_client()

    def test_email_bounce(self):
        '''Check to see email bounce callback works'''
        #import ipdb; ipdb.set_trace();
        rv = self.app.post('/email/bounce', data={'Message-ID':str('PY436d63cab9ad11e081291231400042c7')}, follow_redirects=True)
        #print rv #debug test
        assert 'ESCROWED' in rv.data

        
if __name__ == '__main__':
    unittest.main()