# Install Español

(Estas lineas las pegamos una a una en la cmd):

```shell
#Clonamos el repo de Github
git clone https://github.com/Flora-Network/fd-cli.git
```
```shell
#Entramos a la carpeta creada
cd fd-cli
```
```shell
#Activamos venv
python3 -m venv venv
```
```shell
source venv/bin/activate
```
```shell
pip install -e . --extra-index-url https://pypi.chia.net/simple/
```


# NFT 7/8 reward recovery Español

```shell
#Establecemos la ruta a la database de la fork
export FD_CLI_BC_DB_PATH=$HOME/.flora/mainnet/db/blockchain_v1_mainnet.sqlite
# Establecer la ruta de la database de la billetera.
# Esta debe ser la billetera asociada con la clave "mnemonic" a partir de la que se creó el plot NFT. (Usualmente, tu billetera caliente)
# Reemplace <huella digital> con la huella digital de su billetera, esta la puedes encontrar usando "chia wallet show" o dando click en "Llaves" si tienes instalada la interfaz grafica.
export FD_CLI_WT_DB_PATH=$HOME/.flora/mainnet/wallet/db/blockchain_wallet_v1_mainnet_<fingerprint>.sqlite
# Establecer el "Launcher ID del plot NFT. Reemplaza la ID del ejemplo con tu propia "Launcher ID:"
# Launcher ID: se puede obtener usando "chia plotnft show"
# Ejecuta el comando anterior en Chia, ya que ese valor es un detalle del contrato NFT original, que no existe en las forks.
export LAUNCHER_HASH=aaa0cbae497933a6c029a3819759fe148829dfde0316cb0512ccad23edce6aaa
# Establecer el pool_contract_address. Reemplaza el pool_contract_address del ejemplo con tu propi "pool_contract_address"
# Pool_contract_address: se obtiene usando "chia plotnft show"
# Ejecuta el comando anterior en Chia, ya que ese valor es un detalle del contrato NFT original, que no existe en las forks.
export POOL_CONTRACT_ADDRESS=xch13rht0xz4tpdqfq08e3dk20kewg9cjj3pw0wwjf7vay8whlxn7ppqapeqhz
#Generalmente no tocamos nada de aquí abajo:
fd-cli nft-recover \
  -l "$LAUNCHER_HASH" \
  -p "$POOL_CONTRACT_ADDRESS" \
  -nh 127.0.0.1 \
  -np 18755 \
  -ct $HOME/.flora/mainnet/config/ssl/full_node/private_full_node.crt \
  -ck $HOME/.flora/mainnet/config/ssl/full_node/private_full_node.key
  
# Todas las coins minadas hace más de 7 días con plots NFT deberían aparecer en la wallet pronto.
```
