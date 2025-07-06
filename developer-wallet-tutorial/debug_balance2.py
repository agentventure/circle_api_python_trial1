from config import wallets_api

wallet_id = "46709485-a176-5cb4-bc28-f2c8d7400685"

def get_wallet_balance_detailed(wallet_id):
    """Get detailed wallet balance with proper error handling"""
    try:
        # Make the API call
        response = wallets_api.list_wallet_balance(wallet_id)
        
        # Access the balance data
        balance_data = response.data
        token_balances = balance_data.token_balances
        
        print(f"💰 Wallet Balance Details:")
        print(f"📍 Wallet ID: {wallet_id}")
        print(f"🔢 Total Token Types: {len(token_balances)}")
        print("=" * 50)
        
        if token_balances:
            for i, balance in enumerate(token_balances, 1):
                # Access balance properties
                amount = balance.amount
                token = balance.token
                
                # Display formatted balance
                print(f"{i}. {token.symbol} ({token.name})")
                print(f"   Amount: {amount}")
                print(f"   Blockchain: {token.blockchain}")
                print(f"   Decimals: {token.decimals}")
                print(f"   Token Address: {token.token_address}")
                print(f"   Is Native: {token.is_native}")
                print(f"   Last Updated: {balance.update_date}")
                print()
                
                # Calculate human-readable amount
                # For USDC with 6 decimals, amount is already in human-readable format
                # Only divide by 10^decimals if amount is in wei/smallest unit format
                if token.decimals > 0 and float(amount) >= (10 ** token.decimals):
                    human_readable = float(amount) / (10 ** token.decimals)
                else:
                    human_readable = float(amount)
                print(f"   💡 Human Readable: {human_readable} {token.symbol}")
                print("   " + "-" * 40)
                
        else:
            print("   No balances found")
            
        return token_balances
        
    except Exception as e:
        print(f"❌ Error getting wallet balance: {e}")
        return None

# Usage example
if __name__ == "__main__":
    # Use the wallet ID defined at the top of the file
    balances = get_wallet_balance_detailed(wallet_id)
    
    # Access specific balance data
    if balances:
        first_balance = balances[0]
        print(f"\n🎯 First Balance: {first_balance.amount} {first_balance.token.symbol}")
        print(f"🏦 Blockchain: {first_balance.token.blockchain}")



# Access pattern: 
# response.data.token_balances[index].amount
# response.data.token_balances[index].token.symbol
# response.data.token_balances[index].token.blockchain
# response.data.token_balances[index].token.decimals
# response.data.token_balances[index].token.token_address
# response.data.token_balances[index].token.is_native
# response.data.token_balances[index].update_date

