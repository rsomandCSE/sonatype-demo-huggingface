"""
Sonatype Demo App - Hugging Face Transformers

Minimal application with intentionally vulnerable dependencies.
Sonatype Lifecycle will detect policy violations and recommend golden versions.

VULNERABILITIES:
- transformers@4.30.0: Multiple CVEs
- torch@2.0.0: CVE-2023-45852, CVE-2024-2529
- pillow@9.3.0: CVE-2023-44271, CVE-2023-50447
- numpy@1.24.0: CVE-2024-56806

GOLDEN VERSIONS:
- transformers: 4.47.1 (Trust Score: 98)
- torch: 2.5.1 (Trust Score: 95)
- tokenizers: 0.21.0 (Trust Score: 99)
- huggingface-hub: 0.27.1 (Trust Score: 99)
"""

from transformers import pipeline
import torch

def main():
    print('=' * 60)
    print('Sonatype Demo App - Hugging Face Transformers')
    print('=' * 60)
    print('Status: Built with vulnerable dependencies')
    print()
    print('Vulnerable Dependencies:')
    print('- transformers@4.30.0 (Known vulnerabilities)')
    print('- torch@2.0.0 (CVE-2023-45852 CVSS 9.8)')
    print('- pillow@9.3.0 (CVE-2023-44271 CVSS 9.8)')
    print('- numpy@1.24.0 (CVE-2024-56806)')
    print()
    print('Golden Versions:')
    print('- transformers@4.47.1 (Trust Score: 98)')
    print('- torch@2.5.1 (Trust Score: 95)')
    print('- pillow@11.0.0 (Trust Score: 97)')
    print('=' * 60)
    print()

    # Simple sentiment analysis demo
    try:
        classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
        result = classifier("Sonatype helps secure software supply chains!")
        print(f"Demo inference result: {result}")
    except Exception as e:
        print(f"Note: Model download may require network access: {e}")

    return {
        'name': 'Sonatype Demo App - HuggingFace',
        'version': '1.0.0',
        'status': 'Running with vulnerable dependencies',
        'dependencies': {
            'transformers': '4.30.0',
            'torch': '2.0.0',
            'tokenizers': '0.13.3',
            'huggingface-hub': '0.14.1',
            'numpy': '1.24.0',
            'pillow': '9.3.0'
        },
        'nextSteps': [
            'Run Lifecycle scan to see policy violations',
            'Open Lifecycle GUI to review vulnerabilities',
            'Select "Create PR for Golden Versions"',
            'Merge the remediation PR'
        ]
    }


if __name__ == '__main__':
    main()
