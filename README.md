# WSCrypto

## Installation
Python 3

1) go to the project root folder;

2) create virtual environment `vitrualenv venv -p python3`;

3) activate virtual environment `source venv/bin/activate`(for linux) `venv\Scripts\activate`(for Windows);

4) install libraries `pip install -r requirements.txt`;


## Usage
```
python wscrypto.py <marketCurrency> <tradeCurrency> <timeToWorkInSeconds> <targetFileName>

Options:
marketCurrency - currency code, for example: USD
tradeCurrency - currency code, for example: BTC
timeToWorkInSeconds - program duration(seconds)
targetFileName - The path to the resulting file
```


## Example
```
$ python wscrypto.py BTC USDT 360 btcusdt.txt
```