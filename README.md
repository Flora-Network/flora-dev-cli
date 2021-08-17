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

# Install Español
https://github.com/Flora-Network/fd-cli/blob/master/README-ES.md
