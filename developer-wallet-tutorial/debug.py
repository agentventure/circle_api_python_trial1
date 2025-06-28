from config import wallet_sets_api
from circle.web3 import developer_controlled_wallets

def debug_wallet_set_response():
    try:
        request = developer_controlled_wallets.CreateWalletSetRequest.from_dict({
            "name": "Debug Wallet Set"
        })
        response = wallet_sets_api.create_wallet_set(request)
        
        print("Response structure:")
        print(f"Response type: {type(response)}")
        print(f"Response data type: {type(response.data)}")
        print(f"Response data wallet_set type: {type(response.data.wallet_set)}")
        print(f"Response data wallet_set dir: {dir(response.data.wallet_set)}")
        print(f"Response data wallet_set: {response.data.wallet_set}")
        
        # Try to access different possible attributes
        wallet_set = response.data.wallet_set
        for attr in dir(wallet_set):
            if not attr.startswith('_'):
                try:
                    value = getattr(wallet_set, attr)
                    print(f"  {attr}: {value}")
                except:
                    print(f"  {attr}: <error accessing>")
                    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    debug_wallet_set_response() 