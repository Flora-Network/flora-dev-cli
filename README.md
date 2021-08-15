# Install

```shell

git clone https://github.com/Flora-Network/fd-cli.git

python3 -m venv venv
source venv/bin/activate
```

# NFT 7/8 reward recovery

```shell

# Set env var to blockchain path.
export FD_CLI_BC_DB_PATH=/root/.flora/mainnet/db/blockchain_v1_mainnet.sqlite
# Set env var to wallet path.
# This must be wallet that is associated with mnemonic from which NFT plot was created.
export FD_CLI_WT_DB_PATH=/root/.flora/mainnet/wallet/db/blockchain_wallet_v1_mainnet_<fingerprint>.sqlite

# Set env var to launcher id of NFT plot.
export LAUNCHER_HASH=aaa0cbae497933a6c029a3819759fe148829dfde0316cb0512ccad23edce6aaa
# Set env var to pool_contract_puzzle_hash. 
# This Bench32 decoded address of NFT plot, the one with comment "USE ONLY FOR PLOTTING".
export CONTRACT_HASH=eeeeb79855585a0481e7cc5b653ed9720b894a2173dce927cce90eebfcd3f000

fd-cli nft-recover \
  -l "$LAUNCHER_HASH" \
  -c "$CONTRACT_HASH" \
  -nh 127.0.0.1 \
  -np 18755 \
  -ct /root/.flora/mainnet/config/ssl/full_node/private_full_node.crt \
  -ck /root/.flora/mainnet/config/ssl/full_node/private_full_node.key
  
# All coins that were mined +7 days ago WITH NFT PLOT should be spendable soon via wallet.
```