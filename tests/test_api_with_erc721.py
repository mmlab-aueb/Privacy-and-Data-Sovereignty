import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../PDS/')

from web3 import Web3
import pytest
import requests
import json
import asyncio
import base64
import datetime
import time

@pytest.fixture(autouse=True, scope="module")
def server():
    import subprocess
    import time
    global w3, account, ERC721Contract_instance
    p3 = subprocess.Popen(['ganache-cli', '-m', 'myth like bonus scare over problem client lizard pioneer submit female collect']) #use this mnemonic to much the contract address in configuration
    time.sleep(10)
    p1 = subprocess.Popen(['python3', 'PDS/pds.py'])
    time.sleep(5) #Otherwise the server is not ready when tests start
    w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:8545"))
    with open('conf/contract/build/ERC721Metadata.bin', 'r') as myfile:
        binfile = myfile.read()
    with open('conf/contract/build/ERC721Metadata.abi', 'r') as myfile:
        abi = myfile.read()
    account = w3.eth.accounts[0]
    ERC721Contract = w3.eth.contract(abi=abi, bytecode=binfile)
    tx_hash = ERC721Contract.constructor("Sofie Access Token", "SAT").transact({'from': account})
    tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    address = tx_receipt.contractAddress
    ERC721Contract_instance = w3.eth.contract(abi = abi, address = address)

    yield
    p1.kill()
    p3.kill()


def test_valid_auth_code_erc721():
    global w3, account, ERC721Contract_instance
    nbf = time.mktime(datetime.datetime(2020, 4, 1, 00, 00).timetuple())
    exp = time.mktime(datetime.datetime(2020, 4, 1, 23, 59).timetuple()) 
    payload = {'grant-type':'auth_code', 'grant':'shared_secret_key', 'metadata':json.dumps({'aud': 'sofie-iot.eu','nbf':nbf, 'exp': exp}), 'erc-721':'True'}
    response  = requests.post("http://localhost:9001/gettoken", data = payload).text
    response =json.loads(response)

    token_id = int('c0097d06511a91ffd05912862dca06f5bd428886dd3b9534d863947a1aa3e5c4', base=16)
    erc721_token = ERC721Contract_instance.functions.getTokenURI(token_id).call()
    token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiJzb2ZpZS1pb3QuZXUiLCJleHAiOjE1ODU3NzQ3NDAuMCwibmJmIjoxNTg1Njg4NDAwLjB9.tmnmUIZLd7E8flr8vM_ldosO2yJzHw2vCloJ9AVkLP7fXGexmp9_TlitU2YxttHKHrs-WvbjAZafYj72OLYmEr4Cgm27U-XieuvXBxHDp8uJCd2x_D4lKCDgOYM3YMVIjmVqL2kCk4F1g_pqFy6FBsjhInF1_23GETujzqyD5Jf1p_gCCiZUE8xMjRPPYEpeA7gs1MFPlwMFWM42ao2lzW6y0dSyWHopqrdzoSX_mK8qKO1rS-bx0KJWNia5spZhsgDYnfcsf59fgxkus96Dv5smK15XbWpyY-OJ7Hm6w4GbF6JdObmFYJIbzL-rRTdGeJ1pbbmnCF9Adqkcmca2rg"

    assert(response['code'] == 200 and erc721_token == token) 
