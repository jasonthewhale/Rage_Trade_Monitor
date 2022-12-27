from web3 import Web3, HTTPProvider
import discord
import asyncio

###############################################################
# discord bot setup
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
channel =client.get_channel('Your channel ID here')
###############################################################



rpc = 'Arbitrum RPC here'
web3 = Web3(HTTPProvider(rpc))

simulatorContract = "0x5c92846A38E75e56ef6935A2B12fF832F1FA80ac"
simulatorAbi = '[{"inputs":[{"internalType":"uint160","name":"sqrtPriceLimitX96","type":"uint160"}],"name":"InvalidSqrtPriceLimit","type":"error"},{"inputs":[],"name":"R","type":"error"},{"inputs":[],"name":"T","type":"error"},{"inputs":[],"name":"ZeroAmount","type":"error"},{"inputs":[{"internalType":"contract IClearingHouse","name":"clearingHouse","type":"address"},{"internalType":"uint32","name":"poolId","type":"uint32"},{"internalType":"int256","name":"amount","type":"int256"},{"internalType":"uint160","name":"sqrtPriceLimitX96","type":"uint160"},{"internalType":"bool","name":"isNotional","type":"bool"}],"name":"simulateSwap","outputs":[{"components":[{"internalType":"int256","name":"amountSpecified","type":"int256"},{"internalType":"int256","name":"vTokenIn","type":"int256"},{"internalType":"int256","name":"vQuoteIn","type":"int256"},{"internalType":"uint256","name":"liquidityFees","type":"uint256"},{"internalType":"uint256","name":"protocolFees","type":"uint256"},{"internalType":"uint160","name":"sqrtPriceX96Start","type":"uint160"},{"internalType":"uint160","name":"sqrtPriceX96End","type":"uint160"}],"internalType":"struct IVPoolWrapper.SwapResult","name":"swapResult","type":"tuple"},{"components":[{"internalType":"uint160","name":"sqrtPriceX96Start","type":"uint160"},{"internalType":"int24","name":"tickStart","type":"int24"},{"internalType":"uint8","name":"feeProtocol","type":"uint8"},{"internalType":"uint128","name":"liquidityStart","type":"uint128"},{"internalType":"int24","name":"tickSpacing","type":"int24"},{"internalType":"uint24","name":"fee","type":"uint24"},{"internalType":"uint256","name":"value1","type":"uint256"},{"internalType":"uint256","name":"value2","type":"uint256"}],"internalType":"struct SimulateSwap.Cache","name":"cache","type":"tuple"},{"components":[{"components":[{"internalType":"uint160","name":"sqrtPriceStartX96","type":"uint160"},{"internalType":"int24","name":"tickNext","type":"int24"},{"internalType":"bool","name":"initialized","type":"bool"},{"internalType":"uint160","name":"sqrtPriceNextX96","type":"uint160"},{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"uint256","name":"feeAmount","type":"uint256"}],"internalType":"struct SimulateSwap.Step","name":"step","type":"tuple"},{"components":[{"internalType":"int256","name":"amountSpecifiedRemaining","type":"int256"},{"internalType":"int256","name":"amountCalculated","type":"int256"},{"internalType":"uint160","name":"sqrtPriceX96","type":"uint160"},{"internalType":"int24","name":"tick","type":"int24"},{"internalType":"uint256","name":"feeGrowthGlobalIncreaseX128","type":"uint256"},{"internalType":"uint128","name":"protocolFee","type":"uint128"},{"internalType":"uint128","name":"liquidity","type":"uint128"}],"internalType":"struct SimulateSwap.State","name":"state","type":"tuple"}],"internalType":"struct SwapSimulator.SwapStepAndState[]","name":"steps","type":"tuple[]"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"contract IUniswapV3Pool","name":"vPool","type":"address"},{"internalType":"uint24","name":"liquidityFeePips","type":"uint24"},{"internalType":"uint24","name":"protocolFeePips","type":"uint24"},{"internalType":"bool","name":"swapVTokenForVQuote","type":"bool"},{"internalType":"int256","name":"amountSpecified","type":"int256"},{"internalType":"uint160","name":"sqrtPriceLimitX96","type":"uint160"}],"name":"simulateSwapOnVPool","outputs":[{"components":[{"internalType":"int256","name":"amountSpecified","type":"int256"},{"internalType":"int256","name":"vTokenIn","type":"int256"},{"internalType":"int256","name":"vQuoteIn","type":"int256"},{"internalType":"uint256","name":"liquidityFees","type":"uint256"},{"internalType":"uint256","name":"protocolFees","type":"uint256"},{"internalType":"uint160","name":"sqrtPriceX96Start","type":"uint160"},{"internalType":"uint160","name":"sqrtPriceX96End","type":"uint160"}],"internalType":"struct IVPoolWrapper.SwapResult","name":"swapResult","type":"tuple"},{"components":[{"internalType":"uint160","name":"sqrtPriceX96Start","type":"uint160"},{"internalType":"int24","name":"tickStart","type":"int24"},{"internalType":"uint8","name":"feeProtocol","type":"uint8"},{"internalType":"uint128","name":"liquidityStart","type":"uint128"},{"internalType":"int24","name":"tickSpacing","type":"int24"},{"internalType":"uint24","name":"fee","type":"uint24"},{"internalType":"uint256","name":"value1","type":"uint256"},{"internalType":"uint256","name":"value2","type":"uint256"}],"internalType":"struct SimulateSwap.Cache","name":"cache","type":"tuple"},{"components":[{"components":[{"internalType":"uint160","name":"sqrtPriceStartX96","type":"uint160"},{"internalType":"int24","name":"tickNext","type":"int24"},{"internalType":"bool","name":"initialized","type":"bool"},{"internalType":"uint160","name":"sqrtPriceNextX96","type":"uint160"},{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"uint256","name":"feeAmount","type":"uint256"}],"internalType":"struct SimulateSwap.Step","name":"step","type":"tuple"},{"components":[{"internalType":"int256","name":"amountSpecifiedRemaining","type":"int256"},{"internalType":"int256","name":"amountCalculated","type":"int256"},{"internalType":"uint160","name":"sqrtPriceX96","type":"uint160"},{"internalType":"int24","name":"tick","type":"int24"},{"internalType":"uint256","name":"feeGrowthGlobalIncreaseX128","type":"uint256"},{"internalType":"uint128","name":"protocolFee","type":"uint128"},{"internalType":"uint128","name":"liquidity","type":"uint128"}],"internalType":"struct SimulateSwap.State","name":"state","type":"tuple"}],"internalType":"struct SwapSimulator.SwapStepAndState[]","name":"steps","type":"tuple[]"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"contract IUniswapV3Pool","name":"vPool","type":"address"},{"internalType":"uint24","name":"liquidityFeePips","type":"uint24"},{"internalType":"uint24","name":"protocolFeePips","type":"uint24"},{"internalType":"bool","name":"swapVTokenForVQuote","type":"bool"},{"internalType":"int256","name":"amountSpecified","type":"int256"},{"internalType":"uint160","name":"sqrtPriceLimitX96","type":"uint160"}],"name":"simulateSwapOnVPoolView","outputs":[{"components":[{"internalType":"int256","name":"amountSpecified","type":"int256"},{"internalType":"int256","name":"vTokenIn","type":"int256"},{"internalType":"int256","name":"vQuoteIn","type":"int256"},{"internalType":"uint256","name":"liquidityFees","type":"uint256"},{"internalType":"uint256","name":"protocolFees","type":"uint256"},{"internalType":"uint160","name":"sqrtPriceX96Start","type":"uint160"},{"internalType":"uint160","name":"sqrtPriceX96End","type":"uint160"}],"internalType":"struct IVPoolWrapper.SwapResult","name":"swapResult","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"contract IClearingHouse","name":"clearingHouse","type":"address"},{"internalType":"uint32","name":"poolId","type":"uint32"},{"internalType":"int256","name":"amount","type":"int256"},{"internalType":"uint160","name":"sqrtPriceLimitX96","type":"uint160"},{"internalType":"bool","name":"isNotional","type":"bool"}],"name":"simulateSwapView","outputs":[{"components":[{"internalType":"int256","name":"amountSpecified","type":"int256"},{"internalType":"int256","name":"vTokenIn","type":"int256"},{"internalType":"int256","name":"vQuoteIn","type":"int256"},{"internalType":"uint256","name":"liquidityFees","type":"uint256"},{"internalType":"uint256","name":"protocolFees","type":"uint256"},{"internalType":"uint160","name":"sqrtPriceX96Start","type":"uint160"},{"internalType":"uint160","name":"sqrtPriceX96End","type":"uint160"}],"internalType":"struct IVPoolWrapper.SwapResult","name":"swapResult","type":"tuple"}],"stateMutability":"view","type":"function"}]'
simulate = web3.eth.contract(address = simulatorContract, abi = simulatorAbi)

chainlinkOracleContract = "0x639Fe6ab55C921f74e7fac1ee960C0B6293ba612"
oracleAbi = '[{"inputs":[{"internalType":"address","name":"_aggregator","type":"address"},{"internalType":"address","name":"_accessController","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"int256","name":"current","type":"int256"},{"indexed":true,"internalType":"uint256","name":"roundId","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"updatedAt","type":"uint256"}],"name":"AnswerUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"roundId","type":"uint256"},{"indexed":true,"internalType":"address","name":"startedBy","type":"address"},{"indexed":false,"internalType":"uint256","name":"startedAt","type":"uint256"}],"name":"NewRound","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"}],"name":"OwnershipTransferRequested","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"inputs":[],"name":"acceptOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"accessController","outputs":[{"internalType":"contract AccessControllerInterface","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"aggregator","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_aggregator","type":"address"}],"name":"confirmAggregator","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"description","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_roundId","type":"uint256"}],"name":"getAnswer","outputs":[{"internalType":"int256","name":"","type":"int256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint80","name":"_roundId","type":"uint80"}],"name":"getRoundData","outputs":[{"internalType":"uint80","name":"roundId","type":"uint80"},{"internalType":"int256","name":"answer","type":"int256"},{"internalType":"uint256","name":"startedAt","type":"uint256"},{"internalType":"uint256","name":"updatedAt","type":"uint256"},{"internalType":"uint80","name":"answeredInRound","type":"uint80"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_roundId","type":"uint256"}],"name":"getTimestamp","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"latestAnswer","outputs":[{"internalType":"int256","name":"","type":"int256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"latestRound","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"latestRoundData","outputs":[{"internalType":"uint80","name":"roundId","type":"uint80"},{"internalType":"int256","name":"answer","type":"int256"},{"internalType":"uint256","name":"startedAt","type":"uint256"},{"internalType":"uint256","name":"updatedAt","type":"uint256"},{"internalType":"uint80","name":"answeredInRound","type":"uint80"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"latestTimestamp","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address payable","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"","type":"uint16"}],"name":"phaseAggregators","outputs":[{"internalType":"contract AggregatorV2V3Interface","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"phaseId","outputs":[{"internalType":"uint16","name":"","type":"uint16"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_aggregator","type":"address"}],"name":"proposeAggregator","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"proposedAggregator","outputs":[{"internalType":"contract AggregatorV2V3Interface","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint80","name":"_roundId","type":"uint80"}],"name":"proposedGetRoundData","outputs":[{"internalType":"uint80","name":"roundId","type":"uint80"},{"internalType":"int256","name":"answer","type":"int256"},{"internalType":"uint256","name":"startedAt","type":"uint256"},{"internalType":"uint256","name":"updatedAt","type":"uint256"},{"internalType":"uint80","name":"answeredInRound","type":"uint80"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"proposedLatestRoundData","outputs":[{"internalType":"uint80","name":"roundId","type":"uint80"},{"internalType":"int256","name":"answer","type":"int256"},{"internalType":"uint256","name":"startedAt","type":"uint256"},{"internalType":"uint256","name":"updatedAt","type":"uint256"},{"internalType":"uint80","name":"answeredInRound","type":"uint80"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_accessController","type":"address"}],"name":"setController","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_to","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"version","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"}]'
priceFeed = web3.eth.contract(address = chainlinkOracleContract, abi = oracleAbi)

def getIndexPrice(_amount):
    clearingHouse = "0x4521916972A76D5BFA65Fb539Cf7a0C2592050Ac"
    poolId = 2721558366
    if _amount > 0:
        amount = web3.toWei(_amount, 'ether')
    else:
        _amount = - _amount
        amount = -web3.toWei(_amount, 'ether')
    sqrtPriceLimitX96 = 0
    isNotional = False
    swapResult = simulate.functions.simulateSwapView(
        clearingHouse,
        poolId,
        amount,
        sqrtPriceLimitX96,
        isNotional).call()
    return abs(swapResult[2] / 1e6)

def getChainlinkPrice():
    oracleResults = priceFeed.functions.latestRoundData().call()
    return oracleResults[1] / 1e8

def isShortProfitable():
    if getIndexPrice(-1) - getChainlinkPrice() >= 2:
        return True
    return False

def isLongProfitable():
    if getChainlinkPrice() - getIndexPrice(1) >= 2:
        return True
    return False

def isTimeToDecreasePosition():
    if getChainlinkPrice() - getIndexPrice(1) >= 0:
        return True
    return False

##########################################################################################
# discord bot login and connected to rage call
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

        # if message.content.startswith('$hello'):
        #     await message.channel.send('Hello!')
        
    if message.content.startswith('rage'):
        while 1:
            await message.add_reaction('🚀')
            longOneEther = getIndexPrice(1)
            shortOneEther = getIndexPrice(-1)
            ethOraclePrice = getChainlinkPrice()
            await message.channel.send(f'longOneEther is {longOneEther}, shortOneEther is {shortOneEther}, ChainlinkPrice is {ethOraclePrice}')
            if isLongProfitable():
                await message.channel.send('long 1 ether is profitbale, do it ASAP!!!')
                await message.channel.send('🐮')
            else:
                await message.channel.send('chill, no long opportunity')
            if isShortProfitable():
                await message.channel.send('short 1 ether is profitbale, do it ASAP!!!')
                await message.channel.send('🐮')
            else:
                await message.channel.send('chill, no short opportunity')
            if isTimeToDecreasePosition():
                await message.channel.send('time to decrease position degen!!!')
                await message.channel.send('🐮')
            else:
                await message.channel.send('chill, not yet to take profit')
            await asyncio.sleep(300)

client.run('Your discord bot key here')

##################################################################################################
