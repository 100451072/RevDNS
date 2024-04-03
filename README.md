# RevDNS: Reverse DNS Lookup Tool

## Overview
`RevDNS` is a command-line tool written in Python that performs reverse DNS lookups, translating IP addresses into domain names. This tool can process single IP addresses, CIDR ranges, or lists of IP addresses provided in a text file. `RevDNS` is designed to assist network administrators, security professionals, and researchers in identifying the domain names associated with given IP addresses, facilitating network analysis and security audits.

## Features
- **Single IP Lookup:** Perform a reverse DNS lookup on a single IP address.
- **CIDR Range Processing:** Input a CIDR range to perform reverse DNS lookups on all IPs within that range.
- **File Processing:** Read a list of IP addresses or CIDR ranges from a file, performing batch reverse DNS lookups.
- **Interactive Mode:** Run without arguments for an interactive prompt that accepts IP addresses or CIDR ranges one at a time.
