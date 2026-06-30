"""
Sonatype Demo App - Hugging Face Transformers

Minimal application with intentionally vulnerable dependencies.
Sonatype Lifecycle will detect policy violations and recommend golden versions.

VULNERABILITIES:
- transformers@4.30.0: Multiple CVEs
- pillow@9.3.0: CVE-2023-44271, CVE-2023-50447
- numpy@1.24.0: CVE-2024-56806
- requests@2.26.0: CVE-2023-32681, CVE-2024-35195

GOLDEN VERSIONS:
- transformers: 4.47.1 (Trust Score: 98)
- tokenizers: 0.21.0 (Trust Score: 99)
- huggingface-hub: 0.27.1 (Trust Score: 99)
- pillow: 11.0.0 (Trust Score: 97)
- numpy: 2.2.1
- requests: 2.33.1
"""

def main():
    print('=' * 60)
    print('Sonatype Demo App - Hugging Face Transformers')
    print('=' * 60)
    print('Status: Built with vulnerable dependencies')
    print()
    print('Vulnerable Dependencies:')
    print('- transformers@4.30.0 (Known vulnerabilities)')
    print('- pillow@9.3.0 (CVE-2023-44271 CVSS 9.8)')
    print('- numpy@1.24.0 (CVE-2024-56806)')
    print('- requests@2.26.0 (CVE-2023-32681 CVSS 6.1)')
    print()
    print('Golden Versions:')
    print('- transformers@4.47.1 (Trust Score: 98)')
    print('- pillow@11.0.0 (Trust Score: 97)')
    print('- requests@2.33.1 (Trust Score: 99)')
    print('=' * 60)
    print()

    return {
        'name': 'Sonatype Demo App - HuggingFace',
        'version': '1.0.0',
        'status': 'Running with vulnerable dependencies',
        'dependencies': {
            'transformers': '4.30.0',
            'tokenizers': '0.13.3',
            'huggingface-hub': '0.14.1',
            'numpy': '1.24.0',
            'pillow': '9.3.0',
            'requests': '2.26.0'
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
