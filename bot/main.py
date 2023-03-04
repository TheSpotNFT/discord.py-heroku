import discord
import os
from discord.ext import commands
from web3 import Web3
from web3.contract import ContractEvent
from discord.ext import tasks

# Connect to the Ethereum network using Infura with coorect
w3 = Web3(Web3.HTTPProvider('https://avalanche-mainnet.infura.io/v3/c95c3ea588814fed8c05a6f112c05a23'))

# Define contract address and ABI
contract_address = '0x26DaEb5eDa7bBb8b12d05764502d832feEDA45Ea'
contract_abi = [{"inputs":[{"internalType":"address","name":"feeWallet","type":"address"},{"internalType":"string","name":"baseURI","type":"string"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"account","type":"address"},{"indexed":True,"internalType":"address","name":"operator","type":"address"},{"indexed":False,"internalType":"bool","name":"approved","type":"bool"}],"name":"ApprovalForAll","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":True,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"operator","type":"address"},{"indexed":True,"internalType":"address","name":"from","type":"address"},{"indexed":True,"internalType":"address","name":"to","type":"address"},{"indexed":False,"internalType":"uint256[]","name":"ids","type":"uint256[]"},{"indexed":False,"internalType":"uint256[]","name":"values","type":"uint256[]"}],"name":"TransferBatch","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"operator","type":"address"},{"indexed":True,"internalType":"address","name":"from","type":"address"},{"indexed":True,"internalType":"address","name":"to","type":"address"},{"indexed":False,"internalType":"uint256","name":"id","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"value","type":"uint256"}],"name":"TransferSingle","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"string","name":"value","type":"string"},{"indexed":True,"internalType":"uint256","name":"id","type":"uint256"}],"name":"URI","type":"event"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"_exists","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"_mintFee","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"bool","name":"value","type":"bool"}],"name":"addToGudVibes","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"uint256","name":"id","type":"uint256"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address[]","name":"accounts","type":"address[]"},{"internalType":"uint256[]","name":"ids","type":"uint256[]"}],"name":"balanceOfBatch","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"getGudVibes","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"address","name":"operator","type":"address"}],"name":"isApprovedForAll","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"address","name":"owner","type":"address"}],"name":"isTokenOwner","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"mint","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"mintToOwner","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256[]","name":"ids","type":"uint256[]"},{"internalType":"uint256[]","name":"amounts","type":"uint256[]"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"safeBatchTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"operator","type":"address"},{"internalType":"bool","name":"approved","type":"bool"}],"name":"setApprovalForAll","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"baseURI_","type":"string"}],"name":"setBaseURI","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"mintFee","type":"uint256"}],"name":"setMintFee","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"uri","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"}]
contract = w3.eth.contract(address=contract_address, abi=contract_abi)
channel_id = 1081427953713430538  # replace with the ID of your Discord channel

#this is a test bot
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

# create a filter for the `mint` event
event_filter = contract.events.mint.createFilter(fromBlock='latest')

# loop indefinitely, listening for new events
while True:
    # wait for the filter to match a new event
    events = event_filter.get_new_entries()
    
# Define Discord bot client
client = discord.Client(intents=intents)

bot = commands.Bot(command_prefix='!', intents=intents)

# Define event listener function
async def handle_event(event):
    # Get Discord channel object for the desired channel
    args = event['args']
    channel = client.get_channel(1081427953713430538)

    # Send message to Discord channel
    message = f"A mint has taken place on the smart contract! TxHash: {event['transactionHash'].hex()}"
    await channel.send(message)

# Set up Discord bot event listener
@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

    # Subscribe to smart contract events
    contract_event_filter = contract.events.mint.createFilter(fromBlock='latest')
    while True:
        for event in contract_event_filter.get_new_entries():
            handle_event(event)

# Define the Transfer event
Transfer: ContractEvent = contract.events.Transfer()

# Define a task that listens for new minted tokens
@tasks.loop(seconds=10)
async def check_for_mint():
    latest_block = web3.eth.getBlock('latest')
    events = Transfer.getLogs(fromBlock=latest_block['number'] - 10, toBlock=latest_block['number'])
    for event in events:
        if event['args']['from'] == '0x0000000000000000000000000000000000000000':
            minter = event['args']['to']
            await client.get_channel(channel_id).send(f'{minter} got some Vibes!')

# Start the task
check_for_mint.start()
            
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}({bot.user.id})')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

if __name__ == '__main__':
    bot.run(os.getenv('DISCORD_TOKEN'))
