import scapy.all as scapy
 
# Function to extract covert data from ICMP Echo Requests
def sniff_icmp_packets(interface):
    # This function listens for ICMP Echo Requests and extracts the payload
    def process_packet(packet):
        if packet.haslayer(scapy.ICMP) and packet[scapy.ICMP].type == 8:  # ICMP Echo Request (type 8)
            payload = packet[scapy.Raw].load  # Extract the raw payload from the packet
            print(f"Extracted covert data: {payload.decode('utf-8', errors='ignore')}")  # Display the payload
 
    # Start sniffing on the specified interface
    scapy.sniff(iface=interface, filter="icmp", prn=process_packet, store=0)
 
# Main function to start sniffing for ICMP packets
def main():
    interface = "eth0"  # Change to the correct interface (e.g., eth0, wlan0, etc.)
    print("Starting ICMP packet sniffer...")
    sniff_icmp_packets(interface)  # Start sniffing for ICMP packets
 
if __name__ == "__main__":
    main()