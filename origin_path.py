import boto3
import os

def update_specific_origin_path(distribution_id, target_origin_domain, new_origin_path):
    # Create a CloudFront client
    client = boto3.client('cloudfront')

    # Get the current configuration of the specified distribution
    distribution_config = client.get_distribution_config(Id=distribution_id)
    config = distribution_config['DistributionConfig']
    # Update the Origin Path for the specified origin
    updated = False
    for origin in config['Origins']['Items']:
        if origin['DomainName'] == target_origin_domain:
            origin['OriginPath'] = new_origin_path


    # Update the distribution with the new configuration
    try:
        client.update_distribution(DistributionConfig=config, Id=distribution_id, IfMatch=distribution_config['ETag'])
        print(f"Updated Origin Path for origin '{target_origin_domain}' in distribution {distribution_id}")
    except Exception as e:
        print(f"Error updating distribution: {e}")

if __name__ == "__main__":
    distribution_id = "ERH2GU3TYXEKE"
    # distribution_id = "ERH2GU3TYXEKN"
    target_origin_domain = "katka123.s3.us-east-1.amazonaws.com"
    new_origin_path = "/new/path3"  # Replace with your desired new origin path
    update_specific_origin_path(distribution_id, target_origin_domain, new_origin_path)

    # distribution_id = os.getenv('AWS_DISTRIBUTION_ID')
    # target_origin_domain = os.getenv('AWS_TARGET_ORIGIN_DOMAIN')
    # new_origin_path = os.getenv('AWS_NEW_ORIGIN_PATH')