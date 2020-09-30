import os
from typing import Dict, Text, Any

import hvac


class Vault:
    def _init_(self):
        # configure and connect the client to the local dev server
        self.vault_client = hvac.Client(
            url=os.environ["VAULT_ADDR"], token=os.environ["VAULT_TOKEN"]
        )

    def load_secret(self, name) -> Dict[Text, Any]:
        # Load the secret and return data dictionary

        secret_response = self.vault_client.secrets.kv.read_secret_version(path=name)
        return secret_response["data"]["data"]
