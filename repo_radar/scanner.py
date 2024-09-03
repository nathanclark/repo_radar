from github import Github
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import Progress
import time

def scan_repos(config, specific_repo=None):
    console = Console()
    g = Github(config['GITHUB_TOKEN'])
    user = g.get_user()
    
    repo_data = []
    
    with console.status("[bold green]Fetching repositories...") as status:
        if specific_repo:
            try:
                repos = [user.get_repo(specific_repo)]
            except Exception as e:
                console.print(f"[bold red]Error:[/bold red] Repository '{specific_repo}' not found or inaccessible.")
                return
        else:
            repos = list(user.get_repos())  # Convert PaginatedList to a regular list
    
    with Progress() as progress:
        task = progress.add_task("[cyan]Scanning repositories...", total=len(repos))
        
        for repo in repos:
            readme_status = "❌ Missing"
            tests_status = "❌ Missing"
            
            try:
                repo.get_contents("README.md")
                readme_status = "✅ Found"
            except:
                pass
            
            try:
                contents = repo.get_contents("")
                if any('test' in content.path.lower() for content in contents):
                    tests_status = "✅ Found"
            except:
                tests_status = "⚠️ Unable to check"
            
            repo_data.append([repo.name, readme_status, tests_status])
            
            progress.update(task, advance=1)
            time.sleep(0.1)  # Add a small delay to avoid hitting API rate limits
    
    # Sort repositories alphabetically
    repo_data.sort(key=lambda x: x[0].lower())
    
    # Create and display the table
    table = Table(title="Repository Scan Results")
    table.add_column("Repository", style="cyan", no_wrap=True)
    table.add_column("README Status", style="magenta")
    table.add_column("Tests Status", style="green")
    
    for repo in repo_data:
        table.add_row(*repo)
    
    console.print(table)
    
    # Print summary
    total_repos = len(repo_data)
    readme_count = sum(1 for repo in repo_data if "✅" in repo[1])
    tests_count = sum(1 for repo in repo_data if "✅" in repo[2])
    
    summary = f"""
[bold]Summary:[/bold]
Total repositories scanned: {total_repos}
Repositories with README: {readme_count} ({readme_count/total_repos*100:.1f}%)
Repositories with tests: {tests_count} ({tests_count/total_repos*100:.1f}%)
    """
    
    console.print(Panel(summary, title="Scan Summary", expand=False))