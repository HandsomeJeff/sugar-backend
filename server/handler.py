from web3.auto import w3

# w3 = Web3.HTTPProvider()

def prove(msg, signature: str):
    msg = "0x1476abb745d423bf09273f1afd887d951181d25adc66c4834a70491911b7f750"
    signature = "0xe6ca9bba58c88611fad66a6ce8f996908195593807c4b38bd528d2cff09d4eb33e5bfbbf4d3e39b1a2fd816a7680c19ebebaf3a141b239934ad43cb33fcec8ce1c"
    addr = w3.eth.account.recoverHash(msg, signature)
    print(addr)


prove("", "")
