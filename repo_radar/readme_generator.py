import openai
import anthropic

def generate_readme(config, repo_name, ai_service):
    prompt = f"Generate a README.md file for a GitHub repository named {repo_name}. Include sections for Description, Installation, Usage, and Contributing."

    if ai_service == 'claude':
        client = anthropic.Anthropic(api_key=config['ANTHROPIC_API_KEY'])
        response = client.completions.create(
            model="claude-2.0",
            prompt=f"{anthropic.HUMAN_PROMPT} {prompt}{anthropic.AI_PROMPT}",
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