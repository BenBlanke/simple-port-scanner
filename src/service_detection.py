def detect_service(port):
    known_services = {
        20: "FTP (Data)",
        21: "FTP",
        22: "SSH",
        23: "Telnet",
        25: "SMTP",
        53: "DNS",
        80: "HTTP",
        110: "POP3",
        143: "IMAP",
        443: "HTTPS",
        445: "Microsoft-DS",
        3389: "RDP"
    }
    return known_services.get(port, "Unknown service")