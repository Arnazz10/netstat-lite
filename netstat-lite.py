#!/usr/bin/env python3
import os
import argparse

def parse_proc_net(file, proto):
    conns = []
    with open(file, "r") as f:
        next(f)  # skip header
        for line in f:
            parts = line.split()
            local = parts[1]
            state = parts[3]
            inode = parts[]

            ip_hex, port_hex = local.split(":")
            port = int(port_hex, 16)
            state_map = {
                "01": "ESTABLISHED",
                "0A": "LISTEN",
            }
            conns.append({
                "proto": proto,
                "port": port,
                "state": state_map.get(state, state),
                "inode": inode
            })
    return conns

def main():
    parser = argparse.ArgumentParser(description="NetStat Lite CLI")
    parser.add_argument("--proto", choices=["tcp", "udp"], help="Filter by protocol")
    parser.add_argument("--established", action="store_true", help="Only show established")
    parser.add_argument("--listening", action="store_true", help="Only show listening ports")
    parser.add_argument("--min-port", type=int, default=0, help="Only ports above this number")
    args = parser.parse_args()

    all_conns = []
    all_conns += parse_proc_net("/proc/net/tcp", "tcp")
    all_conns += parse_proc_net("/proc/net/udp", "udp")

    for c in all_conns:
        if args.proto and c["proto"] != args.proto:
            continue
        if args.established and c["state"] != "ESTABLISHED":
            continue
        if args.listening and c["state"] != "LISTEN":
            continue
        if c["port"] < args.min_port:
            continue
        print(f"{c['proto']:>3}  port {c['port']:5}  {c['state']}")

if __name__ == "__main__":
    main()
