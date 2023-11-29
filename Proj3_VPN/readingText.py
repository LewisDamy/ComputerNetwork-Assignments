import re
import subprocess

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

# Define regex patterns
capacity_pattern = re.compile(r'(Uplink|Downlink) capacity: (\d+\.\d+) Mbps.*?Accuracy: (\w+).*?bytes transferred: (\d+\.\d+) MB.*?Flow count: (\d+)', re.DOTALL)
latency_pattern = re.compile(r'(Idle Latency|Responsiveness):\n\s*(\d+) RPM \(([\d.]+) milliseconds\).*?Transport: (\d+) RPM \(([\d.]+) (milliseconds|seconds)\).*?Security: (\d+) RPM \(([\d.]+) (milliseconds|seconds)\).*?HTTP: (\d+) RPM \(([\d.]+) (milliseconds|seconds)\).*?HTTP loaded: (\d+) RPM \(([\d.]+) (milliseconds|seconds)\).*?Accuracy: (\w+)', re.DOTALL)
protocol_pattern = re.compile(r"HTTP-protocol: (\w+)")

# Search for capacity information
capacity_info = re.findall(capacity_pattern, cmd_output)
capacity_data = []
for direction, capacity, accuracy, bytes_transferred, flow_count in capacity_info:
    capacity_data.append({
        "Direction": direction,
        "Capacity": float(capacity),
        "Accuracy": accuracy,
        "Bytes_Transferred": float(bytes_transferred),
        "Flow_Count": int(flow_count)
    })

# Search for latency information
latency_info = re.findall(latency_pattern, cmd_output)
latency_data = []
for type_, rpm1, time1, rpm2, time2, _, rpm3, time3, _, rpm4, time4, _, rpm5, time5, _ , accuracy in latency_info:
    latency_data.append({
        "Type": type_,
        # "RPM_1": int(rpm1),
        "Time_1": float(time1),
        # "RPM_2": int(rpm2),
        "Time_2": float(time2),
        # "RPM_3": int(rpm3),
        "Time_3": float(time3),
        # "RPM_4": int(rpm4),
        "Time_4": float(time4),
        # "RPM_5": int(rpm5),
        "Time_5": float(time5),
        "Accuracy": accuracy
    })
    
# Define regex patterns for extracting protocol-related information
protocol_pattern = re.compile(r'HTTP-protocol:\s+(\w+)')
test_endpoint_pattern = re.compile(r'Test Endpoint:\s+(.+)')
interface_pattern = re.compile(r'Interface:\s+(\w+)')
start_end_pattern = re.compile(r'(Start|End):\s+([\d\-:. ]+)')

# Extract Protocol Info
protocol_match = re.search(protocol_pattern, cmd_output)
http_protocol = protocol_match.group(1) if protocol_match else None

# Extract Test Endpoint
test_endpoint_match = re.search(test_endpoint_pattern, cmd_output)
test_endpoint = test_endpoint_match.group(1) if test_endpoint_match else None

# Extract Interface
interface_match = re.search(interface_pattern, cmd_output)
interface = interface_match.group(1) if interface_match else None

# Extract Start and End Time
start_end_matches = re.findall(start_end_pattern, cmd_output)
start_time, end_time = None, None
for key, value in start_end_matches:
    if key == 'Start':
        start_time = value
    elif key == 'End':
        end_time = value


###### PRINT SECTION ######

# Display extracted data
print("Capacity Data:")
for item in capacity_data:
    print(item)

print("\nLatency Data:")
for item in latency_data:
    print(item)

print('\nProtocol Data:')
print(f"HTTP Protocol: {http_protocol}")
print(f"Test Endpoint: {test_endpoint}")
print(f"Interface: {interface}")
print(f"Start Time: {start_time}")
print(f"End Time: {end_time}")
