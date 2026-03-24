import json,time
from web3 import Web3
import config
from wallet import get_pk

w3 = Web3(Web3.HTTPProvider(config.RPC_URL))

router = w3.eth.contract(
    address=Web3.to_checksum_address(config.ROUTER),
    abi=json.load(open("abi_router.json"))
)

def buy(user, token, amount):
    pk = get_pk(user)
    address = user[1]

    fee = amount * config.FEE_PERCENT / 100
    final_amount = amount - fee

    path = [Web3.to_checksum_address(config.WETH),
            Web3.to_checksum_address(token)]

    tx = router.functions.swapExactETHForTokens(
        0, path, address, int(time.time())+60
    ).build_transaction({
        'from': address,
        'value': w3.to_wei(final_amount,'ether'),
        'gas':300000,
        'gasPrice': w3.to_wei('80','gwei'),
        'nonce': w3.eth.get_transaction_count(address)
    })

    signed = w3.eth.account.sign_transaction(tx, pk)
    return w3.eth.send_raw_transaction(signed.rawTransaction).hex()
