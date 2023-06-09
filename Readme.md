# Thumbor AWS

[![Join the chat at https://gitter.im/thumbor-community/aws](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/thumbor-community/aws?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

[![Circle CI](https://circleci.com/gh/thumbor-community/aws.svg?style=svg)](https://circleci.com/gh/thumbor-community/aws)

## Installation

```bash
    pip install tc_aws_video
```

### Authentication

Authentication is handled by botocore, see [Boto3 documentation](https://boto3.readthedocs.org/en/latest/guide/quickstart.html#configuration).

## Origin story

If you store the images or videos in s3 compatible storage , such as aws , minio etc.

And now, you want to access the images or the first frame of the videos on it.


This is a custom loader will help you to do this!


## Features

 * tc_aws_video.s3_video_loader

Additional Configuration values used:

```bash
# Reuse tc_aws configs 
# If you have credentials in ~/.aws/credentials , 
# then you can ignore TC_AWS_LOADER_ACCESS_KEY and TC_AWS_LOADER_SECRET_KEY
TC_AWS_REGION='your-s3-region'
TC_AWS_ENDPOINT='your-s3-endpoint'
TC_AWS_LOADER_ACCESS_KEY='your-s3-accesskey'
TC_AWS_LOADER_SECRET_KEY='your-s3-secret'

# Customize the temp storage for first frame of video
# The loader will delete the temp file while it read it into memory
TC_AWS_LOADER_VIDEO_FRAME_CACHE='/path/to/your/cache'

# Enable this loader
LOADER = 'tc_aws_video.s3_video_loader'

# Pay attention to this config 
# If you have cdn to access this , then you can set to no_storage
STORAGE = "thumbor.storages.no_storage"
# else if you just want to cache the file into local storage , you can use file_storage 
# but you should remember , if you use the file_storage , the files will persistent in the file system until you remove them
FILE_STORAGE_ROOT_PATH = '/path/to/you/cache'
RESULT_STORAGE_EXPIRATION_SECONDS = 60
```
