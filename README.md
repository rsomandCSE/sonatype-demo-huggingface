# Sonatype Demo App - Hugging Face Transformers

Minimal Python application using Hugging Face transformers with intentionally vulnerable dependencies.

## Vulnerable Dependencies

| Package | Version | Known Issues | Golden Version |
|---------|---------|--------------|----------------|
| transformers | 4.30.0 | Multiple CVEs | 4.47.1 |
| torch | 2.0.0 | CVE-2023-45852 (CVSS 9.8) | 2.5.1 |
| pillow | 9.3.0 | CVE-2023-44271 (CVSS 9.8) | 11.0.0 |
| numpy | 1.24.0 | CVE-2024-56806 | 2.2.1 |
| huggingface-hub | 0.14.1 | Security updates | 0.27.1 |

## Build Instructions

### Prerequisites
- Python 3.8+
- pip
- Nexus Repository Manager
- Sonatype Lifecycle (IQ Server)

### Quick Build

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Configure pip to use Nexus (optional)
mkdir -p ~/.config/pip
cat > ~/.config/pip/pip.conf << 'EOF'
[global]
index-url = http://localhost:8081/repository/pypi-public/simple/
trusted-host = localhost
EOF

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

## Remediation Workflow

1. **Build fails** - Lifecycle detects policy violations
2. **Open Lifecycle GUI** - Navigate to your application
3. **Review violations** - See vulnerability details and CVSS scores
4. **Create PR** - Click "Create PR for Golden Versions"
5. **Merge PR** - Remediation is applied, CI passes

## Manual Upgrade to Golden Versions

Edit `requirements.txt`:

```text
transformers==4.47.1
torch==2.5.1
tokenizers==0.21.0
huggingface-hub==0.27.1
numpy==2.2.1
pillow==11.0.0
```

Then rebuild:

```bash
source venv/bin/activate
pip install -r requirements.txt
```
