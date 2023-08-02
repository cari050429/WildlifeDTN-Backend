from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = 'mediawildlifedtn'
    account_key = 'GP5ABaEi4oBqi+X5Vx30C6rjFa4H2HmupqOLlKW7+FkMAPVG2K2n8/N31jvU5kha2gpLfcY5JF40+AStyOVTXA=='
    azure_container = 'media'
    expiration_secs = None  # Optional: Set a TTL for the media files
