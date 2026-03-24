from web3 import Web3
from security import encrypt, decrypt
from database import save_user

def create_wallet(user_id):
    acct = Web3().eth.account.create()

    address = acct.address
    pk = encrypt(acct.key.hex())

    save_user(user_id, address, pk)
    return address

def get_pk(user):
    return decrypt(user[2])
