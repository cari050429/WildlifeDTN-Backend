
from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    connection_string = 'DefaultEndpointsProtocol=https;AccountName=mediawildlifedtn;AccountKey=GP5ABaEi4oBqi+X5Vx30C6rjFa4H2HmupqOLlKW7+FkMAPVG2K2n8/N31jvU5kha2gpLfcY5JF40+AStyOVTXA==;EndpointSuffix=core.windows.net'
    azure_container = 'media'
    expiration_secs = None  # Optional: Set a TTL for the media files
