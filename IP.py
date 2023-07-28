import random

def IP_Pool():

    class IPAddress:
        def __init__(self, ip_address, port):
            self.ip_address = ip_address
            self.port = port

    def get_random_data(ip_list):
        random_data = random.choice(ip_list)
        return random_data

    ip_list = [
        # todo IP代理池
        IPAddress("61.145.212.31", "3128"),

    ]

    random_data = get_random_data(ip_list)
    IP = random_data.ip_address+":"+random_data.port
    return IP