import boto3
import pandas as pd

# Initialize AWS S3 client
s3 = boto3.client('s3')

# Function to download data from S3
def download_data(bucket_name, file_name):
    s3.download_file(bucket_name, file_name, file_name)
    print(f"Downloaded {file_name} from {bucket_name}")

# Function to label data (simple example)
def label_data(file_name):
    data = pd.read_csv(file_name)
    data['label'] = data['text'].apply(lambda x: 'Positive' if 'good' in x else 'Negative')
    return data

# Function to upload labeled data back to S3
def upload_labeled_data(bucket_name, file_name, labeled_data):
    labeled_data.to_csv(file_name, index=False)
    s3.upload_file(file_name, bucket_name, f'labeled_{file_name}')
    print(f"Labeled data uploaded to {bucket_name}/labeled_{file_name}")

# Main function to process the data
def process_data(bucket_name, file_name):
    download_data(bucket_name, file_name)
    labeled_data = label_data(file_name)
    upload_labeled_data(bucket_name, file_name, labeled_data)

if __name__ == "__main__":
    process_data('your-bucket-name', 'data.csv')
