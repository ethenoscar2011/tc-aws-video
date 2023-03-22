from setuptools import setup, find_packages

setup(
    name='tc_aws_video',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'thumbor>=6.0.0,<7',
        'botocore',
        'subprocess32',
        'tc_aws'
    ],
    url='https://github.com/ethenoscar2011/tc-aws-video',
    author='Ethenoscar',
    author_email='ethenoscar2011@gmail.com',
    description='A customer loader for getting the video first frame from s3 compatible storage'
)