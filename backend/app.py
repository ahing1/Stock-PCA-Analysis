from flask import Flask, request, jsonify, send_from_directory
from routes.pca import preprocess_bp
import os
from services.preprocess_data import preprocess_file
from services.apply_pca import apply_pca
from services.optimization import optimize_portfolio_for_file
from services.apply_clustering import apply_kmeans


app = Flask(__name__)
app.register_blueprint(preprocess_bp, url_prefix='/api')

DATA_DIR = "./data"
VISUALIZATION_DIR = os.path.join(DATA_DIR, "visualizations")
OPTIMIZED_PORTFOLIO_DIR = os.path.join(DATA_DIR, "optimized_portfolio")
os.makedirs(VISUALIZATION_DIR, exist_ok=True)
os.makedirs(OPTIMIZED_PORTFOLIO_DIR, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No file selected for uploading"}), 400
    
    file_path = os.path.join(DATA_DIR, file.filename)
    file.save(file_path)
    
    processed_file_path = os.path.join(DATA_DIR, 'processed', file.filename)
    preprocess_file(file_path).to_csv(processed_file_path, index=False)
    
    return jsonify({"message": f"File uploaded and processed: {file.filename}"}), 200

@app.route('/run-analysis', methods=['POST'])
def run_analysis():
    data = request.json
    file_name = data.get('file_name')

    if not file_name:
        return jsonify({"error": "File name is required"}), 400

    processed_file_path = os.path.join(DATA_DIR, 'processed', file_name)
    clustered_file_path = os.path.join(DATA_DIR, 'clustered', file_name)
    optimized_file_path = os.path.join(OPTIMIZED_PORTFOLIO_DIR, file_name)

    # Perform PCA and clustering
    pca_df, _ = apply_pca(processed_file_path)
    pca_df.to_csv(clustered_file_path, index=False)
    apply_kmeans(clustered_file_path)

    # Perform portfolio optimization
    portfolio_df = optimize_portfolio_for_file(clustered_file_path)
    portfolio_df.to_csv(optimized_file_path, index=False)

@app.route('/visualizations/<filename>', methods=['GET'])
def get_visualization(filename):
    return send_from_directory(VISUALIZATION_DIR, filename)

if __name__ == "__main__":
    app.run(debug=True)