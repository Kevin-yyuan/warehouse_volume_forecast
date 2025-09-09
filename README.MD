# 📦 Warehouse Volume Time-Series Forecast

This project provides a 4-week forecast of weekly container volume for a warehouse. It uses a time-series model to predict future demand, turning a complex data science model into a simple, interactive web application for operational planning.

## 🚀 Live Demo

You can access the live, interactive application here:
**[➡️ View the Deployed Streamlit App](https://warehouse-volume-forecast.streamlit.app/)**

## 🎯 Project Goal

The primary goal is to assist a warehouse manager with operational planning by building a time-series model that accurately forecasts the total weekly container volume for the next four weeks. This allows for better resource allocation, staffing decisions, and inventory management.

## ✨ Key Features

- **Interactive Forecasts:** Users can generate a new 4-week forecast with the click of a button.
- **Data Visualization:** The app displays historical data, time-series decomposition (trend, seasonality), and the final forecast plot.
- **Uncertainty Intervals:** The forecast includes prediction intervals (`yhat_lower`, `yhat_upper`) to visualize the range of likely outcomes, providing a more realistic view of the future.
- **Clear Data Presentation:** Forecasted values for the next four weeks are shown in a clean, easy-to-read table.

## 🛠️ Key Skills Demonstrated

- **Time-Series Analysis:** Handling date-time data, resampling from daily to weekly frequency, and decomposing a time-series to identify trends and seasonality.
- **Forecasting Models:** Implementing and training a predictive model using Facebook's **Prophet** library.
- **Data Application Development:** Building and deploying a user-friendly, interactive web application using **Streamlit**.
- **Data Visualization:** Creating informative plots with `matplotlib`, `seaborn`, and `plotly` to communicate data insights and model results effectively.
- **Project Workflow:** Demonstrating an end-to-end data science workflow from data generation and analysis to model deployment.

## 📂 Project Structure

├── 🐍 app.py # The Python script for the Streamlit web application.
├── 📓 warehouse_volume_forecast.ipynb # Jupyter Notebook with detailed EDA and model evaluation.
├── 📊 warehouse_daily_volume.csv # The synthetic dataset used for training.
├── 📄 requirements.txt # A list of Python libraries required to run the project.
└── 📜 README.md # This file.

## 💻 How to Run Locally

To run this application on your own machine, follow these steps:

1.  **Clone the repository:**

    ```bash
    git clone [https://github.com/](https://github.com/Kevin-yyuan/warehouse_volume_forecast.git)
    cd warehouse_volume_forecast
    ```

2.  **Create and activate a virtual environment (recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Streamlit app:**
    ```bash
    streamlit run app.py
    ```
    Your web browser will open with the application running locally.

## 📊 Data

The data used for this project is synthetic, generated to simulate three years of daily warehouse container volume. It was created with realistic components:

- **A base volume** with a slight positive **trend** over time.
- **Yearly seasonality** (e.g., higher volume during peak seasons).
- **Weekly seasonality** (e.g., higher volume on Mondays, lower on weekends).
- **Random noise** to mimic real-world unpredictability.
