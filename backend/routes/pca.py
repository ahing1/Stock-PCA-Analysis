from flask import Blueprint, jsonify
import os
from services.preprocess_data import main as preprocess_main

preprocess_bp = Blueprint('preprocess', __name__)

@preprocess_bp.route('/preprocess', methods=['POST'])
def preprocess_data():
    """Endpoint to trigger data preprocessing."""
    preprocess_main()
    return jsonify({"message": "Data preprocessing completed successfully."}), 200
