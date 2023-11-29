import matplotlib.pyplot as plt

# Data
categories = ['Sem VPN', 'VPN (USA)', 'VPN (SOUTH AFRICA)', 'VPN (JAPAN)']
upload = [29.11, 20.94, 17.83, 9.85]
download = [131.97, 266.56, 253.68, 160.36]
latency = [26.5, 151.62, 286.82, 472.39]

# Creating subplots
fig, axs = plt.subplots(3)

# Plotting upload speed
upload_bars = axs[0].bar(categories, upload, color='#8C9C84', width=0.5)
axs[0].set_title('Upload Speed (Mbps)')
for bar in upload_bars:
    axs[0].annotate(f'{bar.get_height():.2f}', (bar.get_x() + bar.get_width() / 2, bar.get_height()), ha='center', va='bottom')

# Plotting download speed
download_bars = axs[1].bar(categories, download, color='#D8C176', width=0.5)
axs[1].set_title('Download Speed (Mbps)')
for bar in download_bars:
    axs[1].annotate(f'{bar.get_height():.2f}', (bar.get_x() + bar.get_width() / 2, bar.get_height()), ha='center', va='bottom')

# Plotting latency
latency_bars = axs[2].bar(categories, latency, color='#CF755B', width=0.5)
axs[2].set_title('Latency (ms)')
for bar in latency_bars:
    axs[2].annotate(f'{bar.get_height():.2f}', (bar.get_x() + bar.get_width() / 2, bar.get_height()), ha='center', va='bottom')

# Adjust layout
plt.tight_layout()
plt.show()
