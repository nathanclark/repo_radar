import click
from dotenv import load_dotenv
from rich.console import Console
from .scanner import scan_repos
from .readme_generator import generate_readme
from .config import load_config

console = Console()

@click.group()
def cli():
    """RepoRadar - Scan and improve your GitHub repositories"""
    pass

@cli.command()
@click.option('--repo', help='Specific repository to scan. If not provided, all repositories will be scanned.')
def scan(repo):
    """Scan GitHub repositories for missing README and tests"""
    config = load_config()
    try:
        scan_repos(config, repo)
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {str(e)}")

@cli.command()
@click.option('--repo', prompt='Enter the repository name', help='Repository to generate README for')
@click.option('--ai-service', type=click.Choice(['claude', 'openai']), prompt='Choose AI service (claude/openai)', help='AI service to use for README generation')
def generate(repo, ai_service):
    """Generate README for a repository using AI"""
    config = load_config()
    try:
        generate_readme(config, repo, ai_service)
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {str(e)}")

if __name__ == '__main__':
    load_dotenv()
    cli()