import os
import pandas as pd
import numpy as np
from scipy.optimize import minimize

CLUSTERED_DATA_DIR = "./data/clustered"
OPTIMIZED_PORTFOLIO_DIR = "./data/optimized"

os.makedirs(OPTIMIZED_PORTFOLIO_DIR, exist_ok=True)


def calculate_portfolio_performance(weights, mean_returns, cov_matrix):
    portfolio_return = np.sum(mean_returns * weights)
    portfolio_std_dev = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
    return portfolio_return, portfolio_std_dev


def optimize_portfolio(mean_returns, cov_matrix, num_clusters, risk_free_rate=0.01):
    def negative_sharpe_ratio(weights):
        portfolio_return, portfolio_std_dev = calculate_portfolio_performance(
            weights, mean_returns, cov_matrix
        )
        sharpe_ratio = (portfolio_return - risk_free_rate) / portfolio_std_dev
        return -sharpe_ratio

    constraints = {"type": "eq", "fun": lambda w: np.sum(w) - 1}

    bounds = tuple((0, 1) for _ in range(num_clusters))

    initial_weights = num_clusters * [1 / num_clusters]

    result = minimize(
        negative_sharpe_ratio,
        initial_weights,
        method="SLSQP",
        bounds=bounds,
        constraints=constraints,
    )

    if result.success:
        return result.x
    else:
        raise ValueError("Optimization failed:", result.message)


def optimize_portfolio_for_file(file_path):
    """Optimize portfolio for a single clustered data file."""
    print(f"Optimizing portfolio for {file_path}...")

    # Load clustered data
    df = pd.read_csv(file_path)

    # Group by cluster and calculate mean returns and covariance matrix
    grouped_df = df.groupby('cluster').mean()
    mean_returns = grouped_df.mean()  # Average return for each cluster
    cov_matrix = grouped_df.cov()    # Covariance matrix for clusters

    # Optimize portfolio based on cluster-level data
    weights = optimize_portfolio(mean_returns, cov_matrix, len(grouped_df))

    # Create a DataFrame for cluster weights
    portfolio_df = pd.DataFrame({
        'Cluster': grouped_df.index,
        'Weight': weights
    })

    return portfolio_df



def main():
    for file_name in os.listdir(CLUSTERED_DATA_DIR):
        clustered_file_path = os.path.join(CLUSTERED_DATA_DIR, file_name)
        try:
            # Optimize portfolio for the current file
            portfolio_df = optimize_portfolio_for_file(clustered_file_path)

            # Save the optimized portfolio to a CSV file
            optimized_file_path = os.path.join(OPTIMIZED_PORTFOLIO_DIR, file_name)
            portfolio_df.to_csv(optimized_file_path, index=False)
            print(f"Optimized portfolio saved to {optimized_file_path}")

        except Exception as e:
            print(f"Error processing {file_name}: {e}")


if __name__ == "__main__":
    main()
