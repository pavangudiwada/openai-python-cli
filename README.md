# OpenAI and Python Practice
Simple CLI application using Python Typer CLI tool to get responses from OpenAI


## Usage

1. Clone the repository
```bash
git clone https://github.com/pavangudiwada/openai-python-cli.git
```
2. Install dependencies
```bash
pip install -r requirements.txt
```
3. Add OpenAI API key as an environment variable
```bash
export OPENAI_API_KEY="YOUR_KEY_HERE"
```
4. Run the app
```
python get_answers.py
```

### Options

Use `--role` to give the AI more context. By default, it acts as a Professional DevOps Engineer with expert level Prometheus and Kube Prometheus Stack knowledge. 

```
python get_answers.py --role "Python FastAPI expert"
```

Run `--help` to get all options, defaults and descriptions. 