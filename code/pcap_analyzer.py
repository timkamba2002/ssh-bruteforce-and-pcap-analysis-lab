from scapy.all import rdpcap  # Import Scapy utility to read pcap files

# Path to your pcap file
file_path = './network_sec_monitoring2.pcap'

def count_packets_by_protocol(pcap_path):
    """
    Read a pcap file and count:
      - total packets
      - number of TCP, UDP, ICMP, and ARP packets
    """
    # Load all packets from the pcap file into memory as a PacketList
    packets = rdpcap(pcap_path)

    # Total number of packets in the pcap
    total_packets = len(packets)

    # Initialize counters for each protocol of interest
    tcp_count = 0
    udp_count = 0
    icmp_count = 0
    arp_count = 0

    # Iterate over each packet and check which protocol layers it has
    for pkt in packets:
        # Check by layer name using strings so we don't need to import classes
        if pkt.haslayer("ARP"):
            arp_count += 1
        if pkt.haslayer("TCP"):
            tcp_count += 1
        if pkt.haslayer("UDP"):
            udp_count += 1
        if pkt.haslayer("ICMP"):
            icmp_count += 1

    # Return counts as a dictionary for easy access
    return {
        "total": total_packets,
        "tcp": tcp_count,
        "udp": udp_count,
        "icmp": icmp_count,
        "arp": arp_count,
    }

if __name__ == "__main__":
    # Call the function with the given pcap file path
    counts = count_packets_by_protocol(file_path)

    # Print results in a readable format
    print(f"Total packets: {counts['total']}")
    print(f"TCP packets:   {counts['tcp']}")
    print(f"UDP packets:   {counts['udp']}")
    print(f"ICMP packets:  {counts['icmp']}")
    print(f"ARP packets:   {counts['arp']}")
