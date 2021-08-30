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

(Copiamo il testo seguente in un editor di testo e modifichiamolo, una volta finito lo copieremo e incolleremo nel terminale per eseguirlo).

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

# Script Powershell su Windows


## Prerequisiti:

Git per Windows: [Scarica - Git](https://git-scm.com/download/win)

Python per Windows: [Scarica - Python](https://www.python.org/downloads/)

Microsoft Visual C++ Redistributable [Visual C++ Redistributable](https://support.microsoft.com/en-us/topic/the-latest-supported-visual-c-downloads-2647da03-1eea-4433-9aff-95f26a218cc0)

## Utilizzo:
Lo script è eseguibile anche senza parametri. Ti saranno chiesti al momento il `LAUNCHER_HASH` e il `POOL_CONTRACT_ADDRESS`.

Sono comunque disponibili diversi parametri. Ricorda che non tutti sono necessari poichè con già valori predefiniti. 


| Argomento | Descrizione | Tipo | Default | Necessario? |
| --- | --- | --- | --- | --- | 
| `-LAUNCHER_HASH [your_launcher_id]` | Launcher ID o NFT che vuoi recuperare. Ottenibile tramite comando "chia plotnft show" su Chia. | `stringa` | Vuoto | Si |
| `-POOL_CONTRACT_ADDRESS [your_pool_contract_address]` | Pool contract address dell'NFT che vuoi recuperare. Ottenibile tramite comando "chia plotnft show" su Chia. | `stringa` | Vuoto | Si |
| `-fingerprint [wallet_fingerprint]` | Wallet fingerprint. Se hai solamente un portafoglio/Wallet, il parametro non è necessario e sarà automaticamente usato quello esistente. | `stringa` | Vuoto | No |
| `-sleep [hours]` | Se specificato eseguirà lo script in un ciclo/loop infinito, ripetendo la recovery in base all'intervallo specificato. | `Intero` | `0` | No |
| `-nettype [nettype]` | (`mainnet` o `testnet`) Parte del percorso per la cartella della fork in cui sono salvati i dati (ricorda che silicon utilizza la cartella `mainnet`). | `stringa` | `mainnet` | Si |
| `-blockchains [fork1], [fork2], [fork3]...` | Se non precedentemente specificato la recovery sarà effettuata su `flora`. Elenco di stringhe, accetta più valori saparati da virgola. | `Elenco di stringhe` | `flora` | Si |


#### Esempi di utilizzo:

* Recupero delle monete dalla Blockchain Flora:

   `./flora_recovery.ps1 -POOL_CONTRACT_ADDRESS [tuo_pool_contract_address] -LAUNCHER_HASH [tuo_launcher_id]`   

* Recupero delle monete dalla Blockchain Flora con più portafogli/Wallet:

   `./flora_recovery.ps1 -POOL_CONTRACT_ADDRESS [tuo_pool_contract_address] -LAUNCHER_HASH [tuo_launcher_id] -fingerprint [wallet_fingerprint]`   

* Recupero delle monete dalle Blockchain Flora e Silicon:

   `./flora_recovery.ps1 -POOL_CONTRACT_ADDRESS [tuo_pool_contract_address] -LAUNCHER_HASH [tuo_launcher_id] -blockchains flora, silicoin`   

* Recupero delle monete dalle Blockchain Flora e Silicon in loop/ciclo, esegue la recovery ogni 24 ore:

   `./flora_recovery.ps1 -POOL_CONTRACT_ADDRESS [tuo_pool_contract_address] -LAUNCHER_HASH [tuo_launcher_id] -blockchains flora, silicoin -sleep 24`
