import os
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import numpy as np

PROCESSED_DATA_DIR = "./data/processed"
PCA_DATA_DIR = "./data/pca_transformed"

os.makedirs(PCA_DATA_DIR, exist_ok=True)

def apply_pca(file_path, n_components=None):
    print(f"Applying PCA to {file_path}...")
    df = pd.read_csv(file_path)
    numeric_cols = df.select_dtypes(include=["number"]).columns
    data = df[numeric_cols]
    
    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(data)
    
    pca = PCA(n_components=3)
    pca_data = pca.fit_transform(data_scaled)
    
    pca_columns = [f"PC{i+1}" for i in range(pca_data.shape[1])]
    pca_df = pd.DataFrame(pca_data, columns=pca_columns)
    
    return pca_df, pca.explained_variance_ratio_

def main():
    for file_name in os.listdir(PROCESSED_DATA_DIR):
        processed_file_path = os.path.join(PROCESSED_DATA_DIR, file_name)
        
        if os.path.isfile(processed_file_path):
            pca_df, explained_variance_ratio = apply_pca(processed_file_path, n_components=None)
            
            pca_file_path = os.path.join(PCA_DATA_DIR, file_name)
            pca_df.to_csv(pca_file_path, index=False)
            print(f"Explained variance ratio: {explained_variance_ratio}")
            
            cumulative_variance = np.cumsum(explained_variance_ratio)
            print("Cumulative Variance: ", cumulative_variance) 

if __name__ == "__main__":
    main()