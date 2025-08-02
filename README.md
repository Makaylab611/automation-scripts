# Automation Scripts

This directory contains example automation scripts that showcase how to automate routine operational tasks across a fleet of servers.  The goal of these scripts is to illustrate best practices for monitoring, scheduling and alerting using both **Python** and **AutoSys**.

### Contents

- **server_maintenance.py** – A Python utility that periodically checks CPU and memory utilisation on one or more servers and writes the metrics to a log file.  When resource thresholds are exceeded, the script can be extended to send email notifications to the operations team.  This demonstrates how you might use Python for system automation and proactive monitoring.
- **batch_scheduler.jil** – A sample [AutoSys JIL](https://en.wikipedia.org/wiki/AutoSys) job definition that runs the server maintenance script on a schedule.  The job is configured to execute nightly, capture output to a log, and retry on failure.  This illustrates the syntax and structure of JIL for defining batch jobs.

These examples are simplified for demonstration purposes, but they provide a starting point for building out real‑world automation solutions.
