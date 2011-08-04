from __future__ import unicode_literals
import pprint
import optparse

import poundpay
from flask import Flask, render_template, request, session

from simplemp import config

app = Flask(__name__)
app.secret_key = config.SECRET_KEY


@app.route('/')
def index():
    default_payment = config.DEFAULT_PAYMENT
    return render_template(
        'create_payment.html',
        iframe_root_uri=config.IFRAME_ROOT_URI,
        payment_details=session.get('payment_details', default_payment),
        )


@app.route('/email/bounce', methods=['POST'])
def email_bounce():
    payment = poundpay.Payment.find(sid=request.form['Message-ID'])
    payment.status = 'ESCROWED'
    assert payment.status == 'ESCROWED'
    # payment.save() # save produces a 400 bad request
    return pprint.pformat(payment.__dict__)


@app.route('/payment', methods=['POST'])
def post_payment():
    payment_details = session['payment_details'] = request.form.to_dict()
    payment = poundpay.Payment(**payment_details).save()
    return payment.sid


@app.route('/payment/escrow', methods=['POST'])
def escrow_payment():
    payment = poundpay.Payment.find(sid=request.form['sid'])
    payment.escrow()
    return pprint.pformat(payment.__dict__)


@app.route('/payment/release', methods=['POST'])
def release_payment():
    payment = poundpay.Payment.find(sid=request.form['sid'])
    payment.release()
    return pprint.pformat(payment.__dict__)


if __name__ == '__main__':
    parser = optparse.OptionParser()
    parser.add_option('--environment', '-e', default='sandbox')
    parser.add_option('--port', '-p', default=3000, type=int)
    options, _args = parser.parse_args()
    poundpay.configure(**config.get_credentials_for_env(options.environment))
    app.run(debug=True, port=options.port)
