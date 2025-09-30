# Network Scanner

This Python script scans a range of IP addresses to check which hosts are online and then scans for open ports on each online host.

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
