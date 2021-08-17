# Install Italiano

(Eseguire i seguenti comandi uno ad uno nel terminale):

```shell
# Cloniamo la repository da GitHub.
git clone https://github.com/Flora-Network/fd-cli.git
```
```shell
# Entriamo nella cartella appena clonata.
cd fd-cli
```
```shell
# Attiviamo venv
python3 -m venv venv
```
```shell
source venv/bin/activate
```
```shell
pip install -e . --extra-index-url https://pypi.chia.net/simple/
```


# NFT 7/8 reward recovery Italiano

(Copiamo il testo qui sotto in un editor di testo e modifichiamolo, una volta concluso lo copieremo e incolleremo nel terminale).

```shell

# Impostare il percorso dell'env var con quello della blockchain.
export FD_CLI_BC_DB_PATH=$HOME/.flora/mainnet/db/blockchain_v1_mainnet.sqlite

# Impostare il percorso dell'env var con quello del wallet.
# Deve essere il wallet associato al mnemonico con cui i plot NFT sono stati creati. (Solitamente il tuo portafoglio principale).
# Sostituire <fingerprint> con la fingerprint del proprio wallet ottenibile al seguente percorso oppure tramite comando: "chia wallet show".
export FD_CLI_WT_DB_PATH=$HOME/.flora/mainnet/wallet/db/blockchain_wallet_v1_mainnet_<fingerprint>.sqlite

# Impostare l'env var con il launcher ID dei plot NFT. Sostituire l'ID sottostante con il valore di "Launcher ID:"
# L'ID del launcher è ottenibile tramite comando: "chia plotnft show".
# Eseguire il seguente comando da Chia, poichè i dettagli sono quelli originali del contratto NFT, i quali non esistono nelle forks.
export LAUNCHER_HASH=aaa0cbae497933a6c029a3819759fe148829dfde0316cb0512ccad23edce6aaa

# Impostare l'env var con il pool_contract_address.
# Pool contract address: ottenibile tramite comando: "chia plotnft show".
# Eseguire il seguente comando da Chia, poichè i dettagli sono quelli originali del contratto NFT, i quali non esistono nelle forks.
export POOL_CONTRACT_ADDRESS=xch13rht0xz4tpdqfq08e3dk20kewg9cjj3pw0wwjf7vay8whlxn7ppqapeqhz

# Solitamente questo non è da modificare.
fd-cli nft-recover \
  -l "$LAUNCHER_HASH" \
  -p "$POOL_CONTRACT_ADDRESS" \
  -nh 127.0.0.1 \
  -np 18755 \
  -ct $HOME/.flora/mainnet/config/ssl/full_node/private_full_node.crt \
  -ck $HOME/.flora/mainnet/config/ssl/full_node/private_full_node.key
  
# I coins che sono stati minati più di 7 giorni fa USANDO PLOT NFT dovrebbero essere spendibili a breve nel wallet.  
```
