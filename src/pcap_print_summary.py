from scapy.all import rdpcap

file_path = './network_sec_monitoring2.pcap'

packets = rdpcap(file_path)

for each in packets:
    print(each.summary())



