from flask import Flask
from flask_restful import Api

from controllers.ssl_certificates_chain import SSLCertificatesChain

app = Flask(__name__)
api = Api(app)

api.add_resource(SSLCertificatesChain, "/v2/sslCertificatesChain")

if __name__ == "__main__":
    app.run()
