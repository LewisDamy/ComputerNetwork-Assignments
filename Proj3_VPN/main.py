import subprocess
import re
import json
from datetime import datetime
import logging


print("[1] Network name search - check network name")
# Execute command to get Wi-Fi network name
network_name = subprocess.check_output(["/usr/sbin/networksetup", "-getairportnetwork", "en0"], universal_newlines=True)
network_name_pattern = re.compile(r"Current Wi-Fi Network:\s(.+)")
network_name_match = re.search(network_name_pattern, network_name)


if network_name_match:
    wifi_name = network_name_match.group(1).strip()
    print(f"[1] Network name search - has been found: {wifi_name}")
else:
    wifi_name = "Unknown"
    print(f"[1] Network name search - has NOT been found!!")


print(f"[2] Speed test - start execution")
# Execute the command and capture the output
cmd_output = subprocess.check_output(["networkQuality", "-v"], universal_newlines=True)

print(f"[2] Speed test - searching for data return")
# Define regex patterns to extract information
capacity_pattern = re.compile(r"Uplink capacity: ([\d.]+) Mbps.*Downlink capacity: ([\d.]+) Mbps", re.MULTILINE | re.DOTALL)
latency_pattern = r'(\d+)\s*RPM\s*\(([\d\.]+)\s*milliseconds\)'
latency_section_pattern = r'(\w+\s*Latency):'
protocol_pattern = re.compile(r"HTTP-protocol: (\w+)")

# Search for capacity, latency, and protocol information in the output
capacity_match = re.search(capacity_pattern, cmd_output)
sections = re.findall(latency_section_pattern, cmd_output)
protocol_match = re.search(protocol_pattern, cmd_output)

# Structure to store the extracted data
latency_data = {}

# Loop through each section and extract the data
for section in sections:
    # Create a list to store data for this section
    latency_data[section] = []

    # Find the part of the data that corresponds to this section
    section_data = re.search(f'{section}:(.*?)Accuracy:', cmd_output, re.DOTALL).group(1)

    # Find all latencies in this section
    matches = re.findall(latency_pattern, section_data)

    # Add the found latencies to the list for this section
    for match in matches:
        rpm, milliseconds = match
        latency_data[section].append({
            'RPM': int(rpm),
            'Milliseconds': float(milliseconds)
        })

# Print the structured data
for section, values in latency_data.items():
    print(f"{section}:")
    for value in values:
        print(f"  RPM: {value['RPM']}, Milliseconds: {value['Milliseconds']}")





print(f"[2] Speed test - saving data into variable")


# Extract and save information into variables
if capacity_match:
    uplink_capacity, downlink_capacity = capacity_match.groups()

if protocol_match:
    http_protocol = protocol_match.group(1)

# Display extracted information
print("Uplink Capacity:", uplink_capacity)
print("Downlink Capacity:", downlink_capacity)
# print("Responsiveness:", responsiveness)
# print("RPM:", rpm)
# print("Latency (milliseconds):", milliseconds)
# print("HTTP Protocol:", http_protocol)

# data = {}


# Extract and save information into variables
# data = {
    # "Capacity": {
    #     "Uplink_capacity": capacity_match.group(1),
    #     "Downlink_capacity": capacity_match.group(2)
    # },
#     "Latency": {
#         "Responsiveness": {
#             "Accuracy": latency_match.group(1),
#             "RPM": int(latency_match.group(2)),
#             "Milliseconds": float(latency_match.group(3))
#         }
#     },
#     "Protocol_info": {
#         "HTTP_protocol": protocol_match.group(1)
#     }
# }

# print(data)

# print(f"[2] Speed test - creating json file for data")
# # Generate a unique filename using current timestamp
# timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
# filename = f"extracted_network_data_{wifi_name}_{timestamp}.json"

# # Save the extracted data into a JSON file
# with open(filename, 'w') as file:
#     json.dump(data, file, indent=4)
#     print(f"[2] Speed test - file has been save")
