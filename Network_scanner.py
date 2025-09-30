import socket

def scan_network(ip_base, start, end, port=80, timeout=0.5):
    print(f"Scanning {ip_base}.{start}-{end} on port {port}...")
    for i in range(start, end + 1):
        ip = f"{ip_base}.{i}"
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        try:
            s.connect((ip, port))
            print(f"[+] {ip}:{port} is OPEN")
        except (socket.timeout, ConnectionRefusedError, OSError):
            pass
        finally:
            s.close()

if __name__ == "__main__":
    # Example: scan 192.168.1.1-192.168.1.254 on port 80
    scan_network("192.168.1", 1, 254, port=80)