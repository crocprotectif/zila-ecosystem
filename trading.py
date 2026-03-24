from web3 import Web3
import config
from wallet import get_pk

w3 = Web3(Web3.HTTPProvider(config.RPC_URL))

def send_matic(user, to, amount):
    pk = get_pk(user)
    address = user[1]

    tx = {
        'nonce': w3.eth.get_transaction_count(address),
        'to': Web3.to_checksum_address(to),
        'value': w3.to_wei(amount, 'ether'),
        'gas': 21000,
        'gasPrice': w3.to_wei('50','gwei')
    }

    signed = w3.eth.account.sign_transaction(tx, pk)
    return w3.eth.send_raw_transaction(signed.rawTransaction).hex()
