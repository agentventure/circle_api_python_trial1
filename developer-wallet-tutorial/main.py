from steps import create_wallet_set, create_wallet, get_wallet_balance, create_transaction, sign_transaction

def main():
    print("🚀 Starting Circle Developer-Controlled Wallets Quickstart...")
    
    # # Step 1: Create a wallet set
    # print("\n📦 Step 1: Creating a wallet set...")
    # create_wallet_set()
    
    # # Step 2: Create a wallet
    # print("\n👛 Step 2: Creating a wallet...")
    # create_wallet()
    
    # Step 3: Get wallet balance
    print("\n💰 Step 3: Getting wallet balance...")
    get_wallet_balance()
    
    # Step 4: Create a transaction
    print("\n📝 Step 4: Creating a transaction...")
    create_transaction()
    
    # Step 5: Sign a transaction
    print("\n✍️ Step 5: Signing a transaction...")
    sign_transaction()
    
    print("\n✅ Quickstart completed!")

if __name__ == "__main__":
    main() 