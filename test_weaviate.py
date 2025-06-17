import weaviate
from weaviate.util import generate_uuid
import json

def test_weaviate_connection():
    # Initialize the client
    client = weaviate.Client(
        url="http://localhost:8080",
        auth_client_secret=weaviate.AuthApiKey(api_key="")  # Empty string for anonymous access
    )

    # Test if Weaviate is ready
    if client.is_ready():
        print("Successfully connected to Weaviate!")
        
        # Create a test schema
        schema = {
            "classes": [{
                "class": "Document",
                "vectorizer": "text2vec-transformers",
                "properties": [
                    {
                        "name": "content",
                        "dataType": ["text"],
                    },
                    {
                        "name": "documentType",
                        "dataType": ["text"],
                    },
                    {
                        "name": "filename",
                        "dataType": ["text"],
                    }
                ]
            }]
        }

        try:
            # Create the schema
            client.schema.create(schema)
            print("Schema created successfully!")

            # Test adding a document
            test_doc = {
                "content": "This is a test document for compliance checking.",
                "documentType": "regulatory",
                "filename": "test_doc.txt"
            }

            # Add the document
            result = client.data_object.create(
                data_object=test_doc,
                class_name="Document"
            )
            print(f"Test document added successfully! ID: {result}")

            # Test querying
            result = (
                client.query
                .get("Document", ["content", "documentType", "filename"])
                .with_limit(1)
                .do()
            )
            print("\nQuery result:")
            print(json.dumps(result, indent=2))

        except Exception as e:
            print(f"Error during schema creation or document addition: {str(e)}")

    else:
        print("Failed to connect to Weaviate!")

if __name__ == "__main__":
    test_weaviate_connection() 