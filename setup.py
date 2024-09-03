
from setuptools import setup, find_packages

setup(
    name='repo_radar',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click',
        'python-dotenv',
        'requests',
        'PyGithub',
        'openai',
        'anthropic',
    ],
    entry_points={
        'console_scripts': [
            'repo_radar=repo_radar.main:cli',
        ],
    },
)
