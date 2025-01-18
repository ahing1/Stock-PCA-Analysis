import os
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

CLUSTERED_DATA_DIR = "./data/clustered"
OPTIMIZED_DATA_DIR = "./data/optimized"
VISUALIZATION_DIR = "./data/visualization"

os.makedirs(VISUALIZATION_DIR, exist_ok=True)

def plot_clusters(file_path):
    print(f"Plotting clusters for {file_path}")
    
    data = pd.read_csv(file_path)
    plt.figure(figsize=(8, 6))
    for cluster in data['cluster'].unique():
        cluster_data = data[data['cluster'] == cluster]
        plt.scatter(cluster_data['PC1'], cluster_data['PC2'], label=f'Cluster {cluster}')
    plt.title('2D Cluster Visualization (PC1 vs PC2)')
    plt.xlabel('PC1')
    plt.ylabel('PC2')
    plt.legend()
    plt.grid()
    plot_path = os.path.join(VISUALIZATION_DIR, f"{os.path.basename(file_path).split('.')[0]}_2D.png")
    plt.savefig(plot_path)
    plt.close()
    
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    for cluster in data['cluster'].unique():
        cluster_data = data[data['cluster'] == cluster]
        ax.scatter(cluster_data['PC1'], cluster_data['PC2'], cluster_data['PC3'], label=f'Cluster {cluster}')
    ax.set_title('3D Cluster Visualization')
    ax.set_xlabel('PC1')
    ax.set_ylabel('PC2')
    ax.set_zlabel('PC3')
    ax.legend()
    plot_path = os.path.join(VISUALIZATION_DIR, f"{os.path.basename(file_path).split('.')[0]}_3D.png")
    plt.savefig(plot_path)
    plt.close()

def plot_portfolio(file_path):
    print(f"Plotting portfolio for {file_path}")
    
    data = pd.read_csv(file_path)
    plt.figure(figsize=(8, 6))
    plt.bar(data['Cluster'], data['Weight'], color='skyblue')
    plt.title('Optimized Portfolio Weights by Cluster')
    plt.xlabel('Cluster')
    plt.ylabel('Weight')
    plt.grid(axis='y')
    plot_path = os.path.join(VISUALIZATION_DIR, f"{os.path.basename(file_path).split('.')[0]}_Portfolio.png")
    plt.savefig(plot_path)
    plt.close()
    
def main():
    for file_name in os.listdir(CLUSTERED_DATA_DIR):
        clustered_file_path = os.path.join(CLUSTERED_DATA_DIR, file_name)
        try:
            plot_clusters(os.path.join(CLUSTERED_DATA_DIR, file_name))
        except Exception as e:
            print(f"Error plotting clusters for {clustered_file_path}: {e}")
    
    for file_name in os.listdir(OPTIMIZED_DATA_DIR):
        optimized_file_path = os.path.join(OPTIMIZED_DATA_DIR, file_name)
        try:
            plot_portfolio(os.path.join(OPTIMIZED_DATA_DIR, file_name))
        except Exception as e:
            print(f"Error plotting portfolio for {optimized_file_path}: {e}")

if __name__ == "__main__":
    main()