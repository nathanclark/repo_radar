import os
import sys

def create_directory(path):
    os.makedirs(path, exist_ok=True)

def create_file(path, content):
    with open(path, 'w') as file:
        file.write(content)

def setup_repo_radar():
    base_dir = 'repo_radar'
    create_directory(base_dir)

    # Create __init__.py
    create_file(os.path.join(base_dir, '__init__.py'), '')

    # Create main.py
    main_content = '''
import click
from dotenv import load_dotenv
from .scanner import scan_repos
from .readme_generator import generate_readme
from .config import load_config

@click.group()
def cli():
    """RepoRadar - Scan and improve your GitHub repositories"""
    pass

@cli.command()
def scan():
    """Scan GitHub repositories for missing README and tests"""
    config = load_config()
    scan_repos(config)

@cli.command()
@click.option('--repo', prompt='Enter the repository name', help='Repository to generate README for')
@click.option('--ai-service', type=click.Choice(['claude', 'openai']), prompt='Choose AI service (claude/openai)', help='AI service to use for README generation')
def generate(repo, ai_service):
    """Generate README for a repository using AI"""
    config = load_config()
    generate_readme(config, repo, ai_service)

if __name__ == '__main__':
    load_dotenv()
    cli()
'''
    create_file(os.path.join(base_dir, 'main.py'), main_content)

    # Create scanner.py
    scanner_content = '''
from github import Github

def scan_repos(config):
    g = Github(config['GITHUB_TOKEN'])
    user = g.get_user()
    
    for repo in user.get_repos():
        print(f"Scanning repository: {repo.name}")
        
        # Check for README
        try:
            repo.get_contents("README.md")
            print("  README.md: Found")
        except:
            print("  README.md: Missing")
        
        # Check for tests
        try:
            contents = repo.get_contents("")
            has_tests = any('test' in content.path.lower() for content in contents)
            print(f"  Tests: {'Found' if has_tests else 'Missing'}")
        except:
            print("  Unable to check for tests")
'''
    create_file(os.path.join(base_dir, 'scanner.py'), scanner_content)

    # Create readme_generator.py
    readme_generator_content = '''
import openai
from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT

def generate_readme(config, repo_name, ai_service):
    prompt = f"Generate a README.md file for a GitHub repository named {repo_name}. Include sections for Description, Installation, Usage, and Contributing."

    if ai_service == 'claude':
        anthropic = Anthropic(api_key=config['ANTHROPIC_API_KEY'])
        response = anthropic.completions.create(
            model="claude-2.0",
            prompt=f"{HUMAN_PROMPT} {prompt}{AI_PROMPT}",
            max_tokens_to_sample=1000
        )
        readme_content = response.completion
    elif ai_service == 'openai':
        openai.api_key = config['OPENAI_API_KEY']
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=1000
        )
        readme_content = response.choices[0].text

    print(f"README generated for {repo_name}:")
    print(readme_content)
'''
    create_file(os.path.join(base_dir, 'readme_generator.py'), readme_generator_content)

    # Create config.py
    config_content = '''
import os

def load_config():
    return {
        'GITHUB_TOKEN': os.getenv('GITHUB_TOKEN'),
        'ANTHROPIC_API_KEY': os.getenv('ANTHROPIC_API_KEY'),
        'OPENAI_API_KEY': os.getenv('OPENAI_API_KEY'),
    }
'''
    create_file(os.path.join(base_dir, 'config.py'), config_content)

    # Create .env.example
    env_example_content = '''
GITHUB_TOKEN=your_github_token_here
ANTHROPIC_API_KEY=your_anthropic_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
'''
    create_file(os.path.join(base_dir, '.env.example'), env_example_content)

    # Create requirements.txt
    requirements_content = '''
click==8.0.3
python-dotenv==0.19.2
requests==2.26.0
PyGithub==1.55
openai==0.27.0
anthropic==0.2.6
'''
    create_file('requirements.txt', requirements_content)

    # Create setup.py
    setup_content = '''
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
'''
    create_file('setup.py', setup_content)

    # Create README.md
    readme_content = '''
# RepoRadar

RepoRadar is a CLI application to scan GitHub repositories for missing README files and tests, and generate READMEs using AI.

## Installation

1. Clone this repository
2. Run `pip install -e .` in the project directory
3. Copy `.env.example` to `.env` and fill in your API keys

## Usage

- To scan repositories: `repo_radar scan`
- To generate a README: `repo_radar generate`

For more information, run `repo_radar --help`
'''
    create_file('README.md', readme_content)

    print("RepoRadar project structure created successfully!")

if __name__ == "__main__":
    setup_repo_radar()