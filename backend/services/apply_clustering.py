import os
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

PCA_DATA_DIR = "./data/pca_transformed"
CLUSTERING_DATA_DIR = "./data/clustered"

os.makedirs(CLUSTERING_DATA_DIR, exist_ok=True)

def apply_kmeans(file_path, n_clusters=3):
    df = pd.read_csv(file_path)
    numeric_cols = df.select_dtypes(include=["number"]).columns
    data = df[numeric_cols]

    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    cluster_labels = kmeans.fit_predict(data)
    print(f"Cluster Labels: {cluster_labels}")

    silhouette_avg = silhouette_score(data, cluster_labels)
    print(f"Silhouette Score: {silhouette_avg:.3f}")

    df["cluster"] = cluster_labels

    return df, kmeans


def main():
    for file_name in os.listdir(PCA_DATA_DIR):
        pca_file_path = os.path.join(PCA_DATA_DIR, file_name)
        clustered_df, kmeans_model = apply_kmeans(pca_file_path, n_clusters=3)
        clustered_file_path = os.path.join(CLUSTERING_DATA_DIR, file_name)
        clustered_df.to_csv(clustered_file_path, index=False)


if __name__ == "__main__":
    main()
