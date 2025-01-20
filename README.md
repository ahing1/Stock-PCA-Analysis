# Stock Market Analysis and Portfolio Optimization

## **Overview**

This project analyzes stock market data using **dimensionality reduction** (PCA), **clustering** (K-Means), and **portfolio optimization** (Markowitz's Efficient Frontier). It enables users to upload stock data, perform analysis, and view insightful visualizations.

The application includes:
- Dimensionality reduction with PCA to identify key factors influencing stock price movements.
- Clustering stocks with similar behavior using K-Means.
- Portfolio optimization for diversification and risk management.
- Interactive visualizations to display clusters, principal components, and optimized portfolios.

---

## **Features**

1. **Upload Stock Data**:
   - Users can upload CSV files containing stock market data.

2. **Run Analysis**:
   - The backend processes data with:
     - PCA for dimensionality reduction.
     - K-Means clustering for grouping stocks.
     - Portfolio optimization for selecting diversified investments.

3. **Visualizations**:
   - 2D/3D visualizations of PCA clusters.
   - Bar charts for optimized portfolio weights.

4. **Technologies**:
   - **Frontend**: React, Tailwind CSS
   - **Backend**: Flask, Python
   - **Data Processing**: Pandas, NumPy, Scikit-learn, Matplotlib
   - **Deployment**: Docker, Google Cloud Run

---

## **System Architecture**

1. **Frontend**:
   - Provides a user interface for file upload, triggering analysis, and viewing results.

2. **Backend**:
   - Processes stock data and performs analysis.
   - Generates visualizations and optimized portfolios.

3. **Google Cloud Run**:
   - Hosts the backend and frontend as separate services.

---

## **Getting Started**

### Prerequisites
- **Node.js** (v18+)
- **Python** (v3.9+)
- **Docker** (v20+)
- **Google Cloud SDK** (for deployment)

---

### **Local Setup**

#### Backend
1. Navigate to the `backend` folder:
   ```bash
   cd backend

2. Create virutal environment
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies
    pip install -r requirements.txt

4. Run the backend
    python app.py

#### Frontend
1. Navigate to the `frontend` folder:
    cd frontend

2. Install dependencies
    npm install

3. Start dev server
    npm start

#### Deployment
1. Run docker-compose
    docker-compose build

2. Push images
    docker-compose push

3. Deploy backend using this command or deploy through console
    gcloud run deploy stock-backend \
    --image gcr.io/<PROJECT-ID>/stock-backend \
    --platform managed \
    --region us-central1 \
    --allow-unauthenticated

4. Deploy frontend using this command or deploy through console
    gcloud run deploy stock-frontend \
    --image gcr.io/<PROJECT-ID>/stock-frontend \
    --platform managed \
    --region us-central1 \
    --allow-unauthenticated
