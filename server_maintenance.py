#!/usr/bin/env python3
"""
server_maintenance.py
----------------------

This script simulates monitoring CPU and memory usage across a list of servers.  In a
production environment you would likely use a library such as psutil or connect via
SSH to each host and gather real metrics.  For demonstration purposes, this script
generates random utilisation values and writes them to a timestamped log file.

Usage::

    python3 server_maintenance.py

The script will iterate over the defined list of servers, collect metrics and
append them to ``maintenance.log`` in the current directory.  If CPU or
memory utilisation exceed the configured thresholds, a warning message will be
printed.  This behaviour could be extended to send email alerts or trigger
notifications via Slack or other systems.
"""

import datetime
import json
import os
import random
from typing import Dict, List

# List of servers to monitor.  In practice this might be read from a
# configuration file or discovered dynamically.
SERVERS: List[str] = [
    "server01.example.com",
    "server02.example.com",
    "server03.example.com",
]

# Thresholds for alerting (percent)
CPU_THRESHOLD: int = 80
MEM_THRESHOLD: int = 75


def collect_metrics(server: str) -> Dict[str, float]:
    """Generate fake CPU and memory utilisation for a given server.

    In a real implementation you might run a remote command like `top` or use a
    monitoring API to retrieve these metrics.  Here we simply return random
    percentages to simulate utilisation.

    Args:
        server: Hostname of the server being monitored.

    Returns:
        Dictionary containing CPU and memory utilisation percentages.
    """
    cpu = random.uniform(10, 95)
    mem = random.uniform(10, 95)
    return {"cpu": round(cpu, 2), "memory": round(mem, 2)}


def write_log(entry: Dict[str, object], log_file: str = "maintenance.log") -> None:
    """Append a JSON entry to the log file.

    Each line in the log contains a JSON object with timestamp, server name and
    metrics.  JSON lines make it easy to parse logs programmatically later.

    Args:
        entry: Data to write (must be JSON serialisable).
        log_file: Path to the log file.
    """
    with open(log_file, "a") as f:
        f.write(json.dumps(entry) + "\n")


def main() -> None:
    timestamp = datetime.datetime.utcnow().isoformat() + "Z"
    for server in SERVERS:
        metrics = collect_metrics(server)
        log_entry = {
            "timestamp": timestamp,
            "server": server,
            "cpu": metrics["cpu"],
            "memory": metrics["memory"],
        }
        write_log(log_entry)

        # Simple alerting to demonstrate threshold logic
        if metrics["cpu"] > CPU_THRESHOLD:
            print(
                f"WARNING: {server} CPU usage {metrics['cpu']}% exceeds {CPU_THRESHOLD}% threshold"
            )
        if metrics["memory"] > MEM_THRESHOLD:
            print(
                f"WARNING: {server} memory usage {metrics['memory']}% exceeds {MEM_THRESHOLD}% threshold"
            )


if __name__ == "__main__":
    main()
