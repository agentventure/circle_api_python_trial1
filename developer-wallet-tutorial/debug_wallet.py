from config import wallets_api
from circle.web3 import developer_controlled_wallets

def debug_wallet_response():
    try:
        # Use the wallet set ID from the previous successful creation
        wallet_set_id = "43d74a20-e9ec-5edc-9bd2-d342dc3d8bad"
        
        request = developer_controlled_wallets.CreateWalletRequest.from_dict({
            "walletSetId": wallet_set_id,
            "description": "Debug Wallet",
            "blockchains": ["ETH-SEPOLIA"]
        })
        response = wallets_api.create_wallet(request)
        
        print("Wallet Response structure:")
        print(f"Response type: {type(response)}")
        print(f"Response data type: {type(response.data)}")
        print(f"Response data dir: {dir(response.data)}")
        print(f"Response data: {response.data}")
        
        # Try to access different possible attributes
        data = response.data
        for attr in dir(data):
            if not attr.startswith('_'):
                try:
                    value = getattr(data, attr)
                    print(f"  {attr}: {value}")
                except:
                    print(f"  {attr}: <error accessing>")
                    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    debug_wallet_response() 