from circle.web3 import utils
from circle.web3 import developer_controlled_wallets
import os

# Initialize the client
client = utils.init_developer_controlled_wallets_client(
    api_key=os.environ.get("CIRCLE_API_KEY"),
    entity_secret=os.environ.get("CIRCLE_ENTITY_SECRET")
)

# Create API instances
wallet_sets_api = developer_controlled_wallets.WalletSetsApi(client)
wallets_api = developer_controlled_wallets.WalletsApi(client)
transactions_api = developer_controlled_wallets.TransactionsApi(client)
signing_api = developer_controlled_wallets.SigningApi(client) 