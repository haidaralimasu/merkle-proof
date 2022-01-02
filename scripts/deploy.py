from scripts.helpful_scripts import get_account
from brownie import NFT, config, network
import os


def deploy_nft():
    account = get_account()

    # verfiying smart contract
    publish_source = config["networks"][network.show_active()]["verify"]

    print('deploying NFT contract ...')
    nft = NFT.deploy(
        'Merkle Test',
        'AP',
        'https://gateway.pinata.cloud/ipfs/QmXaMRgYKTLVNuU4hr3AkkeWv73Lz7i2oN2rui6wNAg4ob/',
        {"from": account},
        publish_source=publish_source
    )

    print(f'nft is deployed at {nft.address}')

    os.remove('address.txt')
    f = open('address.txt', 'a')
    f.write(f'nft deployed at {nft.address}')
    f.close()


def main():
    deploy_nft()
