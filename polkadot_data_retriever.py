from substrateinterface import SubstrateInterface, Keypair
from substrateinterface.exceptions import SubstrateRequestException
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Connect to Polkadot network
substrate = SubstrateInterface(
    url="wss://rpc.polkadot.io",
    ss58_format=0,
    type_registry_preset='polkadot'
)

def fetch_block_info():
    try:
        # Fetch the latest block header
        block_hash = substrate.get_block_hash()
        block_header = substrate.get_block_header(block_hash)
        logging.info(f"Latest block number: {block_header['number']}")
        logging.info(f"Block hash: {block_hash}")
        return block_header
    except SubstrateRequestException as e:
        logging.error(f"Failed to retrieve block info: {e}")

def fetch_account_balance(address):
    try:
        # Retrieve account information (free balance)
        result = substrate.query(
            module='System',
            storage_function='Account',
            params=[address]
        )
        free_balance = result.value['data']['free']
        logging.info(f"Account {address} has free balance: {free_balance}")
        return free_balance
    except SubstrateRequestException as e:
        logging.error(f"Failed to retrieve account balance: {e}")

def fetch_validator_status():
    try:
        # Fetch all active validators
        validators = substrate.query_map('Staking', 'Validators')
        logging.info("Active Validators:")
        for validator, _ in validators:
            logging.info(f"Validator: {validator.value}")
    except SubstrateRequestException as e:
        logging.error(f"Failed to retrieve validator status: {e}")

def main():
    logging.info("Connecting to Polkadot blockchain...")
    # Fetch latest block info
    block_info = fetch_block_info()

    # Fetch a specific account's balance (replace with a valid address)
    account_address = '14G7...YourAccount'
    balance = fetch_account_balance(account_address)

    # Fetch the list of active validators
    fetch_validator_status()

if __name__ == '__main__':
    main()
