# RepoRadar

RepoRadar is a powerful CLI tool designed to help developers scan their GitHub repositories for essential components like README files and test suites. It also offers the capability to generate README files using AI, streamlining the process of maintaining well-documented projects.

![RepoRadar Scan](https://github.com/user-attachments/assets/ebe4b10e-3720-4fbe-aded-e570c317daed)
![RepoRadar Summary](https://github.com/user-attachments/assets/e371153c-428f-4f82-9f96-eaa68e32d2c1)

## Features

- 🔍 Scan GitHub repositories for missing README files and test suites
- 📊 Display scan results in a visually appealing CLI table
- 🎯 Option to scan a specific repository or all repositories
- 📝 Generate README files using AI (powered by OpenAI's GPT or Anthropic's Claude)
- 🌈 Rich, colorful CLI interface for improved user experience

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/nathanclark/repo-radar.git
   cd repo-radar
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Install the package in editable mode:
   ```
   pip install -e .
   ```

5. Create a `.env` file in the project root and add your GitHub token and AI API keys:
   ```
   GITHUB_TOKEN=your_github_token_here
   OPENAI_API_KEY=your_openai_api_key_here
   ANTHROPIC_API_KEY=your_anthropic_api_key_here
   ```

## Usage

### Scanning Repositories

To scan all your GitHub repositories:
```
repo_radar scan
```

To scan a specific repository:
```
repo_radar scan --repo your-repo-name
```

### Generating README

To generate a README for a repository:
```
repo_radar generate --repo your-repo-name --ai-service openai
```

Replace `openai` with `claude` if you prefer to use Anthropic's AI.

## Contributing

Contributions to RepoRadar are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Thanks to the creators and maintainers of the libraries used in this project.
- Inspired by the need for better repository management and documentation practices.