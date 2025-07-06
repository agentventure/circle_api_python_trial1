from circle.web3 import developer_controlled_wallets
from config import transactions_api
import os
import uuid

# Use environment variables
wallet_id = os.environ.get("WALLET_ID")
destination_address = os.environ.get("DESTINATION_ADDRESS") 
amount = os.environ.get("AMOUNT")
token_id = os.environ.get("TOKEN_ID")

print(f"Wallet ID: {wallet_id}")
print(f"Destination: {destination_address}")
print(f"Amount: {amount}")
print(f"Token ID: {token_id}")

if wallet_id and destination_address and amount and token_id:
    try:
        idempotency_key = str(uuid.uuid4())
        request_dict = {
            "idempotencyKey": idempotency_key,
            "amounts": [amount],
            "destinationAddress": destination_address,
            "walletId": wallet_id,
            "tokenId": token_id,
            "feeLevel": 'MEDIUM',
        }
        
        print(f"\nRequest dict: {request_dict}")
        
        request = developer_controlled_wallets.CreateTransferTransactionForDeveloperRequest.from_dict(request_dict)
        response = transactions_api.create_developer_transaction_transfer(request)
        
        print(f"\nResponse type: {type(response)}")
        print(f"Response data type: {type(response.data)}")
        print(f"Response data attributes: {dir(response.data)}")
        print(f"Response data: {response.data}")
        
        # Try different ways to access transaction ID
        print(f"\nTrying to find transaction ID...")
        if hasattr(response.data, 'transaction_id'):
            print(f"Found transaction_id: {response.data.transaction_id}")
        if hasattr(response.data, 'transaction'):
            print(f"Found transaction: {response.data.transaction}")
        if hasattr(response.data, 'id'):
            print(f"Found id: {response.data.id}")
            
    except Exception as e:
        print(f"Error: {e}")
else:
    print("Missing required environment variables")
