from indy import did,wallet,crypto
from PDS import agent
import pytest
import asyncio
import json
import base64


user = {
    'wallet_config': json.dumps({'id': 'user_wallet',"storage_config":{"path":"tests/indy_wallets"}}),
    'wallet_credentials': json.dumps({'key': 'user_wallet_key'}),
    'seed': '000000000000000000000000000User1', #used only for testing
    'msk' : 'msk_key',
    'did' : '4qk3Ab43ufPQVif4GAzLUW'
}

server = {
    'wallet_config': json.dumps({'id': 'as_wallet',"storage_config":{"path":"tests/indy_wallets"}}),
    'wallet_credentials': json.dumps({'key': 'server_wallet_key'}),
    'seed': '0000000000000000000000000Server1', #used only for testing
    'msk' : 'msk_key'
}


@pytest.mark.asyncio
async def test_valid_did():
    challenge = '9843787448916803398229937674313'
    wallet_handle = await wallet.open_wallet(user['wallet_config'], user['wallet_credentials'])
    verkey = await did.key_for_local_did(wallet_handle, user['did'])
    signature = await crypto.crypto_sign(wallet_handle, verkey, challenge.encode())
    signature64 = base64.b64encode(signature)
    code = await agent.verify_did(user['did'], challenge, signature64, server['wallet_config'], server['wallet_credentials'], True)
    assert (code == 200)
    await wallet.close_wallet(wallet_handle)