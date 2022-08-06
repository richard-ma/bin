def get_ip():
    internal_ip = get_internal_ip()
    external_ip = get_external_ip()

    print("Internal IP: %s" % internal_ip)
    print("External IP: %s" % external_ip)


def get_internal_ip():
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 80))
    ip = s.getsockname()[0]
    s.close()
    return ip


def get_external_ip():
    import requests
    ip = requests.get('http://ifconfig.me/ip/', timeout=1).text.strip()
    return ip


if __name__ == "__main__":
    get_ip()
