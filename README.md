# NetStat Lite CLI

A lightweight network analyzer for Linux that reads directly from `/proc/net/tcp` and `/proc/net/udp` to display network connections and listening ports into it

## Features

- **Lightweight**: No external dependencies, reads directly from Linux proc filesystem
- **Fast**: Minimal overhead compared to traditional netstat
- **Flexible**: Filter by protocol, connection state, and port ranges
- **Simple**: Clean, easy-to-read output format

## Requirements

- Linux operating system
- Python 3.x
- Root access (for some network information)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Arnazz10/netstat-lite.git
cd netstat-lite
```

2. Make the script executable:
```bash
chmod +x netstat-lite.py
```

## Usage

### Basic Usage

Show all TCP and UDP connections:
```bash
./netstat-lite.py
```

### Filter by Protocol

Show only TCP connections:
```bash
./netstat-lite.py --proto tcp
```

Show only UDP connections:
```bash
./netstat-lite.py --proto udp
```

### Filter by Connection State

Show only established connections:
```bash
./netstat-lite.py --established
```

Show only listening ports:
```bash
./netstat-lite.py --listening
```

### Filter by Port Range

Show connections on ports above 1000:
```bash
./netstat-lite.py --min-port 1000
```

### Combined Filters

Show only established TCP connections on ports above 1024:
```bash
./netstat-lite.py --proto tcp --established --min-port 1024
```

Show listening UDP ports above 5000:
```bash
./netstat-lite.py --proto udp --listening --min-port 5000
```

## Output Format

The output displays:
- Protocol (tcp/udp)
- Port number
- Connection state (ESTABLISHED, LISTEN, etc.)

Example output:
```
tcp  port  80  LISTEN
tcp  port 443  LISTEN
tcp  port 8080  ESTABLISHED
udp  port  53  LISTEN
```

## Command Line Options

| Option | Description |
|--------|-------------|
| `--proto {tcp,udp}` | Filter by protocol |
| `--established` | Show only established connections |
| `--listening` | Show only listening ports |
| `--min-port PORT` | Show only ports above specified number |
| `-h, --help` | Show help message |

## How It Works

NetStat Lite reads directly from the Linux proc filesystem:
- `/proc/net/tcp` - TCP connection information
- `/proc/net/udp` - UDP connection information

This approach provides:
- **Performance**: Direct file reading without system calls
- **Reliability**: Uses the same data source as the kernel
- **Simplicity**: No complex parsing or external dependencies

## Comparison with Traditional netstat

| Feature | NetStat Lite | Traditional netstat |
|---------|-------------|-------------------|
| Dependencies | None | Multiple system libraries |
| Speed | Fast | Slower due to system calls |
| Memory usage | Minimal | Higher |
| Features | Basic filtering | Advanced features |
| Portability | Linux only | Cross-platform |

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).

## Author

Created by [Arnazz10](https://github.com/Arnazz10)

## Acknowledgments

- Inspired by the traditional `netstat` command
- Uses Linux proc filesystem for network information

