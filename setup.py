from setuptools import setup, find_packages

setup(
    name='rootio-client',  # Name of your package
    version='1.0.0',  # Version number
    author='root.io',
    author_email='labs@root.io',
    description='API Client library for root.io platform.',
    long_description=open('README.md').read(),  # Long description read from the the readme file
    long_description_content_type='text/markdown',
    url='https://github.com/Root-IO-Labs/client',  # Link to your project's repository
    packages=find_packages(),  # Automatically find and include all packages
    install_requires=[
        # List of dependencies, e.g., 'requests >= 2.22.0'
        'urllib3 >= 1.25.3',
        'python-dateutil >= 2.8.2',
        'aiohttp >= 3.9.3',
        'pydantic >= 2.6.0'
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',  # Your package's license
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet',
        'Topic :: Security',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10'
    ],
    python_requires='>=3.10',  # Minimum version requirement of the package
)