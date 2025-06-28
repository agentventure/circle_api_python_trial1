from circle.web3 import developer_controlled_wallets

def debug_transaction_classes():
    print("Available transaction-related classes:")
    for attr in dir(developer_controlled_wallets):
        if 'transaction' in attr.lower() or 'transfer' in attr.lower():
            print(f"  {attr}")

def debug_transaction_request():
    try:
        # Use the wallet ID from the previous successful creation
        wallet_id = "ad01d502-fdc6-5909-a7ee-cd59006f1c45"
        
        # Try different possible class names
        possible_classes = [
            'CreateDeveloperTransactionTransferRequest',
            'CreateTransactionTransferRequest',
            'CreateTransferRequest',
            'CreateTransactionRequest'
        ]
        
        for class_name in possible_classes:
            try:
                class_obj = getattr(developer_controlled_wallets, class_name)
                print(f"✅ Found class: {class_name}")
                
                # Try to create a request
                request = class_obj.from_dict({
                    "walletId": wallet_id,
                    "destinationAddress": "0x1234567890123456789012345678901234567890",
                    "amount": "0.001",
                    "currency": "USD",
                    "blockchain": "ETH-SEPOLIA"
                })
                print(f"✅ Successfully created request with {class_name}")
                return class_name
                
            except AttributeError:
                print(f"❌ Class not found: {class_name}")
            except Exception as e:
                print(f"⚠️ Error with {class_name}: {e}")
                
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    debug_transaction_classes()
    print("\n" + "="*50 + "\n")
    debug_transaction_request() 