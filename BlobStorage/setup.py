from setuptools import setup, find_packages

setup(
    name='blob_storage_utils',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'azure-storage-blob',
    ],
    entry_points={
        'console_scripts': [
            'delete-command=azure-blob-cleanup',
        ],
    },
    author='Michel Borrego',
    author_email='michel@fxstreet.com, michelbh93@gmail.com',
    description='A console application to delete old Azure blobs.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Michel930107/Automations/tree/main/BlobStorage',
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
)