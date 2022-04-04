# Crypto Watch Data Pull

This project pulls data from the crypto watch api and stores the data in a sql database. Currently Postresql and MySQL 
is supported but a database class has been created to allow the ability to connect to different databases. 

# Exchanges

This is the first version that is only pulling data from Kraken but will be working 
to add other exchanges and pairs. Next version will allow the ability to see volume
from all exchanges.

# Pairs

The project now includes more crypto pairs from Kraken and there are plans to expand further.
The goal is to eventually build a dashboard that will give high level insight on how the pairs
are performing. The following pairs have been added:

* Bitcoin
* Ethereum
* Litecoin
* Solana
* Ada/Cardano
* Ripple
* Avalanche
* Polkadot
* Dogecoin
* Terra Luna
* Graph
* Polygon Matic
* Chainlink
* Shiba Inu
* Audius

To add more pairs edit the CryptoPairs ENUM class in the crypto/cryptodata.py file. 

# Project Setup

There is a requirements.txt file located in the src directory. Run the below command
to set the project up. Virtualenv is not required you can use venv if you prefer.


```
virtualenv -p python3.6 <project-name>
cd <project-name>
source bin/activate
git clone https://github.com/coffeeincodeout/crypto-data.git
cd src 
pip install -r requirements.txt
```