from flask import Flask
from routes.pca import preprocess_bp

app = Flask(__name__)
app.register_blueprint(preprocess_bp, url_prefix='/api')
