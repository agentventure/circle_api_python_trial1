from config import wallets_api

wallet_id = "46709485-a176-5cb4-bc28-f2c8d7400685"

# Basic access
response = wallets_api.list_wallet_balance(wallet_id)
balances = response.data.token_balances

# Loop through all balances
for balance in balances:
    amount = balance.amount
    symbol = balance.token.symbol
    blockchain = balance.token.blockchain
    decimals = balance.token.decimals
    
# Access specific balance properties
if balances:
    first_balance = balances[0]
    raw_amount = first_balance.amount  # "9"
    token_symbol = first_balance.token.symbol  # "USDC"
    token_decimals = first_balance.token.decimals  # 6
    
    # Convert to human-readable format
    readable_amount = float(raw_amount) / (10 ** token_decimals)
    print(f"Balance: {readable_amount} {token_symbol}")  # "Balance: 9.0 USDC"