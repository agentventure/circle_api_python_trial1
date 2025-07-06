from circle.web3 import developer_controlled_wallets
from config import wallet_sets_api, wallets_api, transactions_api, signing_api
import os
import uuid

# Global variables to store created resources
wallet_set_id = os.environ.get("WALLET_SET_ID")
wallet_id = os.environ.get("WALLET_ID")
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
            "blockchains": ["MATIC-AMOY"]
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
                token = balance.token
                amount = balance.amount
                
                # Calculate human-readable amount
                # Only divide by 10^decimals if amount is in wei/smallest unit format
                if token.decimals > 0 and float(amount) >= (10 ** token.decimals):
                    human_readable = float(amount) / (10 ** token.decimals)
                else:
                    human_readable = float(amount)
                
                print(f"  - {human_readable} {token.symbol} ({token.name})")
                print(f"    Blockchain: {token.blockchain}")
                print(f"    Token Address: {token.token_address}")
                print(f"    Last Updated: {balance.update_date}")
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
    # Prompt user for required values
    destination_address = os.environ.get("DESTINATION_ADDRESS")
    encrypted_entity_secret = os.environ.get("ENTITY_SECRET_CIPHERTEXT")
    amount = os.environ.get("AMOUNT")
    token_id = os.environ.get("TOKEN_ID")
    # Optionally prompt for gas values
    # gas_limit = input("Enter gas limit (or leave blank to skip): ")
    # gas_price = input("Enter gas price in gwei (or leave blank to skip): ")
    # Generate a unique idempotency key
    idempotency_key = str(uuid.uuid4())
    try:
        request_dict = {
            "idempotencyKey": idempotency_key,
            "amounts": [amount],
            "destinationAddress": destination_address,
            #"entitySecretCiphertext": encrypted_entity_secret,
            "walletId": wallet_id,
            "tokenId": token_id,
            #"blockchain": "MATIC-AMOY",
            "feeLevel": 'MEDIUM',
        }
        # if gas_limit:
        #     request_dict["gasLimit"] = gas_limit
        # if gas_price:
        #     request_dict["gasPrice"] = gas_price
        request = developer_controlled_wallets.CreateTransferTransactionForDeveloperRequest.from_dict(request_dict)
        response = transactions_api.create_developer_transaction_transfer(request)
        transaction_id = response.data.id
        print(f"✅ Created transaction with ID: {transaction_id}")
        print(f"📊 Transaction State: {response.data.state}")
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
        # Sign the transaction directly with transaction ID and wallet ID
        sign_request = developer_controlled_wallets.SignTransactionRequest.from_dict({
            "transactionId": transaction_id,
            "walletId": wallet_id
        })
        sign_response = signing_api.sign_transaction(sign_request)
        
        print(f"✅ Transaction signed successfully")
        print(f"📝 Signature: {sign_response.data.signature}")
        return sign_response.data.signature
    except developer_controlled_wallets.ApiException as e:
        print(f"❌ Error signing transaction: {e}")
        return None 