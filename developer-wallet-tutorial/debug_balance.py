from config import wallets_api

def debug_balance_response():
    try:
        # Use the wallet ID from the previous successful creation
        wallet_id = "4e954899-c507-50e2-8fe4-8f7bf548993d"
        
        response = wallets_api.list_wallet_balance(wallet_id)
        
        print("Balance Response structure:")
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
    debug_balance_response() 