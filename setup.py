# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open("Readme.md", "r") as fh:
    long_description = fh.read()

setup(
    name='tc_aws_video',
    version='2.0.1',
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        'thumbor>=7.0.0',
        'botocore',
        'subprocess32',
        'tc_aws>=7.0.1',
        'pycurl'
    ],
    url='https://github.com/ethenoscar2011/tc-aws-video',
    author='Ethenoscar',
    author_email='ethenoscar2011@gmail.com',
    description='A customer loader for getting the video first frame from s3 compatible storage'
)
