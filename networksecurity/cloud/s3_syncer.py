import os

class S3Sync:
    def sync_folder_to_s3(self, folder, aws_bucket_url):
        """
        Syncs a local folder to an S3 bucket using the AWS CLI.
        """
        command = f"aws s3 sync {folder} {aws_bucket_url}"
        os.system(command)
        
    def sync_folder_from_s3(self, aws_bucket_url, folder):
        """
        Syncs an S3 bucket to a local folder using the AWS CLI.
        """
        command = f"aws s3 sync {aws_bucket_url} {folder}"
        os.system(command)