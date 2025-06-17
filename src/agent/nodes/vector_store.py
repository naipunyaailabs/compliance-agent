import weaviate
from src.config.settings import settings

# Initialize the client with the new v4 syntax
client = weaviate.WeaviateClient(
    connection_params=weaviate.connect.ConnectionParams.from_url(
        url="http://weaviate:8080",  # Use the service name from docker-compose
        grpc_port=50051  # Use the gRPC port we exposed
    )
)

# Connect the client
client.connect()

def store_summaries(summaries):
    try:
        for summary in summaries:
            client.collections.get("ComplianceDoc").data.insert({
                "content": summary
            })
    except weaviate.exceptions.WeaviateClosedClientError:
        # If client is closed, reconnect and try again
        client.connect()
        for summary in summaries:
            client.collections.get("ComplianceDoc").data.insert({
                "content": summary
            })

def get_summaries(limit: int = 10):
    try:
        response = client.collections.get("ComplianceDoc").query.fetch_objects(
            limit=limit
        )
        return [obj.properties["content"] for obj in response.objects]
    except weaviate.exceptions.WeaviateClosedClientError:
        client.connect()
        response = client.collections.get("ComplianceDoc").query.fetch_objects(
            limit=limit
        )
        return [obj.properties["content"] for obj in response.objects]
