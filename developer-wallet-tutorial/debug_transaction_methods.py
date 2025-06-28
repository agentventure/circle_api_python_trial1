from config import transactions_api

def debug_transaction_methods():
    print("Available TransactionsApi methods:")
    for attr in dir(transactions_api):
        if not attr.startswith('_') and 'transfer' in attr.lower():
            print(f"  {attr}")

def debug_transaction_methods_all():
    print("All available TransactionsApi methods:")
    for attr in dir(transactions_api):
        if not attr.startswith('_'):
            print(f"  {attr}")

if __name__ == "__main__":
    debug_transaction_methods()
    print("\n" + "="*50 + "\n")
    debug_transaction_methods_all() 