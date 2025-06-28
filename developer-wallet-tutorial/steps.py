from circle.web3 import developer_controlled_wallets
from config import wallet_sets_api, wallets_api, transactions_api, signing_api
import os

# Global variables to store created resources
wallet_set_id = None
wallet_id = None
transaction_id = None

def create_wallet_set():
    """Step 1: Create a wallet set"""
    global wallet_set_id
    
    try:
        request = developer_controlled_wallets.CreateWalletSetRequest.from_dict({
            "name": "Quickstart Wallet Set"
        })
        response = wallet_sets_api.create_wallet_set(request)
        wallet_set_id = response.data.wallet_set.actual_instance.id
        print(f"✅ Created wallet set with ID: {wallet_set_id}")
        return wallet_set_id
    except developer_controlled_wallets.ApiException as e:
        print(f"❌ Error creating wallet set: {e}")
        return None

def create_wallet():
    """Step 2: Create a wallet"""
    global wallet_id
    
    if not wallet_set_id:
        print("❌ No wallet set ID available")
        return None
    
    try:
        request = developer_controlled_wallets.CreateWalletRequest.from_dict({
            "walletSetId": wallet_set_id,
            "description": "Quickstart Wallet",
            "blockchains": ["ETH-SEPOLIA"]
        })
        response = wallets_api.create_wallet(request)
        wallet_id = response.data.wallets[0].actual_instance.id
        print(f"✅ Created wallet with ID: {wallet_id}")
        return wallet_id
    except developer_controlled_wallets.ApiException as e:
        print(f"❌ Error creating wallet: {e}")
        return None

def get_wallet_balance():
    """Step 3: Get wallet balance"""
    if not wallet_id:
        print("❌ No wallet ID available")
        return None
    
    try:
        response = wallets_api.list_wallet_balance(wallet_id)
        balances = response.data.token_balances
        print(f"💰 Wallet balances:")
        if balances:
            for balance in balances:
                print(f"  - {balance.amount} {balance.currency}")
        else:
            print("  - No balances found")
        return balances
    except developer_controlled_wallets.ApiException as e:
        print(f"❌ Error getting wallet balance: {e}")
        return None

def create_transaction():
    """Step 4: Create a transaction"""
    global transaction_id
    
    if not wallet_id:
        print("❌ No wallet ID available")
        return None
    
    try:
        request = developer_controlled_wallets.CreateTransferTransactionForDeveloperRequest.from_dict({
            "walletId": wallet_id,
            "destinationAddress": "0x1234567890123456789012345678901234567890",
            "amount": "0.001",
            "currency": "USD",
            "blockchain": "ETH-SEPOLIA"
        })
        response = transactions_api.create_developer_transaction_transfer(request)
        transaction_id = response.data.transaction.actual_instance.transaction_id
        print(f"✅ Created transaction with ID: {transaction_id}")
        return transaction_id
    except developer_controlled_wallets.ApiException as e:
        print(f"❌ Error creating transaction: {e}")
        return None

def sign_transaction():
    """Step 5: Sign a transaction"""
    if not transaction_id:
        print("❌ No transaction ID available")
        return None
    
    try:
        # Get the transaction to sign
        response = transactions_api.get_transaction(transaction_id)
        transaction = response.data.transaction
        
        # Sign the transaction
        sign_request = developer_controlled_wallets.SignTransactionRequest.from_dict({
            "transactionId": transaction_id
        })
        sign_response = signing_api.sign_transaction(sign_request)
        
        print(f"✅ Transaction signed successfully")
        print(f"📝 Signature: {sign_response.data.signature}")
        return sign_response.data.signature
    except developer_controlled_wallets.ApiException as e:
        print(f"❌ Error signing transaction: {e}")
        return None 