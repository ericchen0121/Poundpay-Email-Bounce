import os
import app
import unittest


def email_bounce(self, MessageID):
    return self.app.post('/email/bounce', data=dict(
        Message-ID=MessageID
    )) #follow_redirects=True)


# testing functions


def email_bounce(self, ''):
    """Check to see email bounce callback works"""
    test = self.app.email_bounce('PY436d63cab9ad11e081291231400042c7')
    # Do something to check if this works... assert 'blah' for data.test

if __name__ == '__main__':
    unittest.main()