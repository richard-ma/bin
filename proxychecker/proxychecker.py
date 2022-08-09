import requests
import random


class IPGetter:
    def __init__(self):
        self.getter_sites_file = "getter_sites"
        self.getter_sites = list()

        # Load verify sites from file
        with open(self.getter_sites_file, 'r') as f:
            for line in f.readlines():
                self.getter_sites.append(line)
        if len(self.getter_sites) == 0:
            raise Exception("%s is empty." % self.getter_sites_file)

    def get(self, proxy=None):
        if proxy is not None:
            proxies = {
                "%s" % proxy[0]: "%s://%s:%s" % (proxy[0], proxy[1], proxy[2])
            }
        else:
            proxies = None
        print(proxies)
        site = random.choice(self.getter_sites)
        ip = requests.get(site, timeout=5, proxies=proxies).text.strip()
        return ip


class ProxyChecker:
    def __init__(self):
        pass

    def check(self):
        pass


if __name__ == "__main__":
    proxy = [
        "http",
        "192.99.14.132",
        "80",
    ]

    ip =IPGetter().get()
    print(ip)
    ip = IPGetter().get(proxy=proxy)
    print(ip)
