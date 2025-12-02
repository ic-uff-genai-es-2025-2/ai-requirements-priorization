# AI Requirements Prioritization

This repository contains tools and notebooks for automating the prioritization of software requirements using AI models. The project is designed to assist in analyzing, extracting, and prioritizing requirements for software projects, leveraging state-of-the-art natural language processing techniques.

## Repository Structure

```
LICENSE

# Data files used in the project
├── data/
│   ├── pure/
│   │   ├── gemini/
│   │   │   └── gemini.xml
│   │   ├── mashbot/
│   │   │   └── mashbot.csv

# Jupyter notebooks for requirements analysis
├── notebooks/
│   ├── 01-requirements-extraction.ipynb
│   ├── 02-prioritize-requirements.ipynb
```

## Notebooks

### 01-requirements-extraction.ipynb

This notebook focuses on extracting functional requirements from textual descriptions. It uses tokenization and other preprocessing techniques to prepare the data for further analysis.

### 02-prioritize-requirements.ipynb

This notebook prioritizes software requirements based on their cost, risk, and value. It uses a pre-trained language model to generate a roadmap for the project.

## Setup

### Prerequisites

- Python 3.8+
- [Hugging Face Transformers](https://huggingface.co/transformers/)
- PyTorch
- dotenv

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ic-uff-genai-es-2025-2/ai-requirements-priorization.git
   cd ai-requirements-priorization
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up environment variables:
   - Create a `.env` file in the root directory.
   - Add your Hugging Face Hub token:
     ```
     HUGGINGFACE_HUB_TOKEN=your_token_here
     ```

## Usage

### Running the Notebooks

1. Start Jupyter Notebook:
   ```bash
   jupyter notebook
   ```
2. Open and run the desired notebook from the `notebooks/` directory.

### Data

- Place your project data in the `data/` directory, following the structure provided.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Hugging Face](https://huggingface.co/) for providing pre-trained models.
- The UFF GENAI ES 2025-2 team for their support and collaboration.
