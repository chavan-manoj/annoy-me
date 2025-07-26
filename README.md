# Annoy Me

An AI interface that is designed to annoy you with its responses. All its responses are meant to be short, crisp, logical, factual but of least help unless you know the art of asking questions. Hence this tool can be used to become better at your prompt engineering skills.

## Features

- Leverages GPT 4o-mini
- CLI interface to talk to agent

## Installation

1. Clone the repository:
```bash
git clone https://github.com/chavan-manoj/annoy-me.git
cd annoy-me
```

2. Create a virtual environment:

Using standard venv:
```bash
python -m venv annoy-me-venv
source annoy-me-venv/bin/activate  # On Windows: annoy-me-venv\Scripts\activate
```

Or using Conda:
```bash
conda create -n annoy-me-venv python=3.9
conda activate annoy-me-venv
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file with your API keys:
```bash
OPENAI_API_KEY=your_openai_api_key_here
```

You can get your OpenAI API keys from https://platform.openai.com/api-keys

## Usage

1. Run the main script:
```bash
python main.py
```

2. Ask any questions.

## Example Questions

- "Who is the Prime Minister of India?"
- "Suggest me some cool places in Bengaluru for this weekend."
- "Why don't you give me straight answers?"

## Dependencies

- langchain==0.1.12
- langchain-openai==0.0.8
- langgraph==0.0.27
- chromadb==0.4.24
- PyPDF2==3.0.1
- python-dotenv==1.0.1
- openai==1.14.2
- rank_bm25==0.2.2

## License

MIT License