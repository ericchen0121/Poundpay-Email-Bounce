IFRAME_ROOT_URI = 'https://www-sandbox.poundpay.com'


DEVELOPER = dict(
    credentials=dict(
        developer_sid='',
        auth_token=(''),
        api_url='http://localhost:8000',
        ),
    IFRAME_ROOT_URI='http://localhost:5000',
    )

# Eric Chen's developer sid and auth token for sandbox
SANDBOX = dict(
    credentials=dict(
        developer_sid='DVe8f08faeb8b611e090b81231400042c7',
        auth_token=('6d05ec6f6125f00c782263e25586429c85294093a3bad7b899b6b17e6fb1e61e'),
        api_url='https://api-sandbox.poundpay.com',
        ),
    IFRAME_ROOT_URI='https://www-sandbox.poundpay.com',
)


DEFAULT_PAYMENT = dict(
    amount='12311',
    payer_fee_amount='123',
    recipient_fee_amount='123',
    payer_email_address='eric@poundpay.com',
    recipient_email_address='e.ric@poundpay.com',
    description='this is a sample description',
    developer_identifier='',
    )


SECRET_KEY = b'super secret key'


def get_credentials_for_env(environment):
    global IFRAME_ROOT_URI
    configurations = {
        'DEVELOPER': DEVELOPER,
        'SANDBOX': SANDBOX,
        }
    environment = environment.upper()
    configuration = configurations[environment]
    IFRAME_ROOT_URI = configuration['IFRAME_ROOT_URI']
    return configuration['credentials']
