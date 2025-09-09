# generate_data.py
import pandas as pd
import numpy as np

# --- Parameters ---
start_date = "2022-01-01"
end_date = "2024-12-31"
base_volume = 100        # Avg containers per day at the start
trend_slope = 0.1        # Gradual increase in volume over time
yearly_seasonality_amp = 50  # Amplitude of yearly peak/trough
weekly_seasonality_map = {  # Monday=0, Sunday=6
    0: 20,   # Peak on Monday
    1: 15,
    2: 5,
    3: -10,  # Mid-week dip
    4: 10,
    5: -20,  # Weekend low
    6: -15,
}
noise_level = 15         # Random daily fluctuations

# --- Generate Data ---
dates = pd.to_datetime(pd.date_range(start=start_date, end=end_date, freq='D'))
num_days = len(dates)

# 1. Trend component
trend = np.arange(num_days) * trend_slope

# 2. Yearly seasonality (using a sine wave)
yearly_seasonality = yearly_seasonality_amp * \
    np.sin(2 * np.pi * (dates.dayofyear / 365.25 - 0.25))

# 3. Weekly seasonality
weekly_seasonality = dates.dayofweek.map(weekly_seasonality_map)

# 4. Noise
noise = np.random.normal(0, noise_level, num_days)

# --- Combine components ---
# Ensure volume is non-negative
volume = base_volume + trend + yearly_seasonality + weekly_seasonality + noise
volume = np.maximum(0, volume).astype(int)

# --- Create DataFrame ---
df = pd.DataFrame({'date': dates, 'volume': volume})
df.to_csv('warehouse_daily_volume.csv', index=False)

print("Synthetic data generated and saved to warehouse_daily_volume.csv")
