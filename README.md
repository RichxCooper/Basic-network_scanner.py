# Network Scanner

## Testing

To test the network scanner:

1. Make sure you have Python 3.7 or newer installed.
2. Open a terminal in this project directory.
3. (Optional) Edit `network_scanner_main.py` to set the IP range and ports you want to scan.
4. Run the script:
  ```powershell
  C:/Users/1coop/OneDrive/Desktop/Network_scanner.py/.venv/Scripts/python.exe network_scanner_main.py
  ```
5. Review the output to see which hosts are online and which ports are open.

**Note:** You may need to run the script with administrator privileges for some network operations, and ensure your firewall allows outbound ping and port scan traffic.

### Testing Outside Your Network

To test the scanner on external or public networks:

- Change the IP range in `network_scanner_main.py` to target public IPs or remote networks you have permission to scan.
- Ensure you have legal authorization to scan those networks. Scanning external networks without permission is illegal and unethical.
- Run the script from a machine with internet access and no firewall or network policy blocking outbound scans.

**Warning:** Always respect privacy and network security laws. Only scan networks you own or have explicit permission to test.

## Features
- Pings a range of IP addresses to find active hosts
- Scans common ports (22, 80, 443, 3389) on each online host
- Easy to customize IP range and ports

## Usage
1. Edit the script to set your desired IP range and ports.
2. Run the script:
   ```powershell
   C:/Users/1coop/OneDrive/Desktop/Network_scanner.py/.venv/Scripts/python.exe network_scanner_main.py
   ```
3. View results in the terminal.

## Requirements
- Python 3.7+
- No external dependencies (uses built-in libraries)

## Customization
- Change `base_ip`, `start`, and `end` in the script to scan a different IP range.
- Modify the `ports` list to scan different ports.

## Example Output
```
Scanning IPs 192.168.1.1 to 192.168.1.10...
Host 192.168.1.1 is offline.
Host 192.168.1.2 is online.
  Open ports: [22, 80]
...
```

## License
MIT
