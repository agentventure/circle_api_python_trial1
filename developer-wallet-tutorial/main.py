from steps import create_wallet_set, create_wallet, get_wallet_balance, create_transaction
import os

def main():
    print("🚀 Starting Circle Developer-Controlled Wallets Quickstart...")
    
    # Step 1: Create a wallet set
    print("\n📦 Step 1: Creating a wallet set...")
    wallet_set_id = create_wallet_set()
    
    if not wallet_set_id:
        print("❌ Failed to create wallet set. Stopping execution.")
        return
    
    # Step 2: Create a wallet
    print("\n👛 Step 2: Creating a wallet...")
    wallet_id = create_wallet(wallet_set_id)
    
    if not wallet_id:
        print("❌ Failed to create wallet. Stopping execution.")
        return
    
    # Step 3: Get wallet balance (using wallet_id from .env)
    print("\n💰 Step 3: Getting wallet balance...")
    env_wallet_id = os.environ.get("WALLET_ID")
    
    if not env_wallet_id:
        print("❌ No WALLET_ID found in environment variables.")
        return
    
    print(f"🔑 Using wallet ID from .env: {env_wallet_id}")
    balance_info = get_wallet_balance(env_wallet_id)
    
    if not balance_info:
        print("❌ Failed to get wallet balance. Stopping execution.")
        return
    
    # Step 4: Create a transaction
    print("\n📝 Step 4: Creating a transaction...")
    if balance_info["balances"]:
        print(f"📈 Available tokens for transaction: {len(balance_info['balances'])}")
        for i, bal in enumerate(balance_info['balances']):
            print(f"  {i+1}. {bal['human_readable_amount']} {bal['symbol']} (ID: {bal['token_id']})")
    
    # Get transaction parameters from environment variables
    transaction_wallet_id = os.environ.get("WALLET_ID")
    destination_address = os.environ.get("DESTINATION_ADDRESS")
    amount = os.environ.get("AMOUNT")
    token_id = os.environ.get("TOKEN_ID")
    
    print(f"🔑 Transaction parameters from .env:")
    print(f"  Wallet ID: {transaction_wallet_id}")
    print(f"  Destination: {destination_address}")
    print(f"  Amount: {amount}")
    print(f"  Token ID: {token_id}")
    
    create_transaction(transaction_wallet_id, destination_address, amount, token_id)

    print("\n✅ Quickstart completed!")

if __name__ == "__main__":
    main() 