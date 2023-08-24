import boto3
import json
from botocore.exceptions import ClientError

def get_secret():
    secret_name = "cred/mysql"
    region_name = "us-east-1"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
        secret = get_secret_value_response['SecretString']

        # Parse the JSON string
        secret_dict = json.loads(secret)

        # Extract the values
        username = secret_dict.get('username')
        password = secret_dict.get('password')

        return username, password
    except ClientError as e:
        print("Error fetching secret:", e)
        return None, None

if __name__ == '__main__':
    username, password = get_secret()
    
    if username and password:
        print(f"export DB_USERNAME={username}")
        print(f"export DB_PASSWORD={password}")
    else:
        print("Unable to retrieve secret.")
