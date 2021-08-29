# Install

```shell
git clone https://github.com/Flora-Network/fd-cli.git
```
```shell
cd fd-cli
```
```shell
python3 -m venv venv
```
```shell
source venv/bin/activate
```
```shell
pip install -e . --extra-index-url https://pypi.chia.net/simple/
```


# NFT 7/8 reward recovery


```shell

# Set env var to blockchain path.
export FD_CLI_BC_DB_PATH=$HOME/.flora/mainnet/db/blockchain_v1_mainnet.sqlite

# Set env var to wallet path.
# This must be the wallet that is associated with mnemonic from which NFT plot was created. (Usually your hot wallet)
# Replace <fingerprint> with your wallet fingerprint found at below path or by using "chia wallet show"
export FD_CLI_WT_DB_PATH=$HOME/.flora/mainnet/wallet/db/blockchain_wallet_v1_mainnet_<fingerprint>.sqlite

# Set env var to launcher id of NFT plot. Replace the below ID with output of "Launcher ID:" 
# Launcher ID: can be obtained using "chia plotnft show"
# Execute above command in Chia, as those values are the original NFT contract details, which do not exist in the forks
export LAUNCHER_HASH=aaa0cbae497933a6c029a3819759fe148829dfde0316cb0512ccad23edce6aaa

# Set env var to pool_contract_address. 
# Pool contract address: can be obtained using "chia plotnft show"
# Execute above command in Chia, as those values are the original NFT contract details, which do not exist in the forks
export POOL_CONTRACT_ADDRESS=xch13rht0xz4tpdqfq08e3dk20kewg9cjj3pw0wwjf7vay8whlxn7ppqapeqhz

fd-cli nft-recover \
  -l "$LAUNCHER_HASH" \
  -p "$POOL_CONTRACT_ADDRESS" \
  -nh 127.0.0.1 \
  -np 18755 \
  -ct $HOME/.flora/mainnet/config/ssl/full_node/private_full_node.crt \
  -ck $HOME/.flora/mainnet/config/ssl/full_node/private_full_node.key
  
# All coins that were mined +7 days ago WITH NFT PLOT should be spendable soon via wallet.
```

***


# Powershell script for Windows


## Prerequisites

Git for Windows: [Git - download](https://git-scm.com/download/win)

Python for Windows: [Python - download](https://www.python.org/downloads/)

Microsoft Visual C++ Redistributable [Visual C++ Redistributable](https://support.microsoft.com/en-us/topic/the-latest-supported-visual-c-downloads-2647da03-1eea-4433-9aff-95f26a218cc0)

## Usage
Script can be executed without any parameters. You will be then prompted to provide `LAUNCHER_HASH` and `POOL_CONTRACT_ADDRESS`

Scrip also accepts various parameters. Please remember that you do not have to provide required parameters that have already a default value.
 


| Parameter | Description | Type | Default | Required? |
| --- | --- | --- | --- | --- | 
| `-LAUNCHER_HASH [your_launcher_id]` | Launcher ID of NFT that you want to recover. Can be obtained executing "chia plotnft show" in Chia | `string` | Empty | Yes |
| `-POOL_CONTRACT_ADDRESS [your_pool_contract_address]` | Pool contract address of NFT that you want to recover. Can be obtained executing "chia plotnft show" in Chia | `string` | Empty | Yes |
| `-fingerprint [wallet_fingerprint]` | Wallet fingerprint. If you have only one wallet, you do not need to provide this, as it will be found automatically | `string` | Empty | No |
| `-sleep [hours]` | If provided will run script in a infinite loop, repeating recovery in the provided interval | `Integer` | `0` | No |
| `-nettype [nettype]` | (`mainnet` or `testnet`) Part of the folder path where fork store its data  (please remember that silicoin is using `mainnet` folder) | `string` | `mainnet` | Yes |
| `-blockchains [fork1], [fork2], [fork3]...` | If not provided will run recovery for `flora`. Array of strings, accepts multiple values separated by comma | `string array` | `flora` | Yes |


#### Usage examples

* One time recovery of coins in Flora blockchain:

   `./flora_recovery.ps1 -POOL_CONTRACT_ADDRESS [your_pool_contract_address] -LAUNCHER_HASH [your_launcher_id]`   

* One time recovery of coins in Flora blockchain when multiple wallet are available:

   `./flora_recovery.ps1 -POOL_CONTRACT_ADDRESS [your_pool_contract_address] -LAUNCHER_HASH [your_launcher_id] -fingerprint [wallet_fingerprint]`   

* One time recovery of coins in Flora and Silicoin blockchains:

   `./flora_recovery.ps1 -POOL_CONTRACT_ADDRESS [your_pool_contract_address] -LAUNCHER_HASH [your_launcher_id] -blockchains flora, silicoin`   

* Recovery of coins in Flora and Silicoin blockchains in a loop, executing the recovery every 24 hours:

   `./flora_recovery.ps1 -POOL_CONTRACT_ADDRESS [your_pool_contract_address] -LAUNCHER_HASH [your_launcher_id] -blockchains flora, silicoin -sleep 24`


# Install Español
https://github.com/Flora-Network/fd-cli/blob/master/README-ES.md

# Install Italiano
https://github.com/Flora-Network/fd-cli/blob/master/README-IT.md
