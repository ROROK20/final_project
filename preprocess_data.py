import pandas as pd
import matplotlib.pyplot as plt
import os

# Configuration
csv_file_path = 'stock_data.csv'  # Replace with your CSV file name
output_folder = 'processed_images'  # Folder to save images
window_size = 30  # Number of days for each image

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Load data
data = pd.read_csv('/home/nvidia/final_project/stock_data.csv')

# Ensure the date column is in datetime format
data['Date'] = pd.to_datetime(data['Date'])
data.sort_values('Date', inplace=True)

# Create images
for i in range(len(data) - window_size):
    subset = data.iloc[i:i + window_size]
    plt.figure(figsize=(10, 6))
    
    # Plot stock price
    plt.plot(subset['Date'], subset['Close'], color='blue')
    plt.title('Stock Trend from {} to {}'.format(
        subset['Date'].iloc[0].strftime('%Y-%m-%d'),
        subset['Date'].iloc[-1].strftime('%Y-%m-%d'))
    )
    plt.xlabel('Date')
    plt.ylabel('Closing Price')
    plt.xticks(rotation=45)
    
    # Save as grayscale image
    image_path = os.path.join(output_folder, 'trend_{}.png'.format(i))
    plt.savefig(image_path, format='png', bbox_inches='tight', dpi=100, cmap='gray')
    plt.close()

print('Images saved to {}'.format(output_folder))
