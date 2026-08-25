import os
import re
from datetime import datetime

def extract_field(body, field_name):
    pattern = rf'### {field_name}\s*\n(.*?)(?=\n###|\Z)'
    match = re.search(pattern, body, re.DOTALL)
    return match.group(1).strip() if match else 'N/A'

def get_next_ixe_number():
    year = datetime.now().year
    registry_dir = f'registry/{year}'
    os.makedirs(registry_dir, exist_ok=True)
    
    existing = [f for f in os.listdir(registry_dir) if f.endswith('.md')]
    if not existing:
        return 1
    
    numbers = []
    for f in existing:
        match = re.search(r'IXE-\d{4}-(\d+)', f)
        if match:
            numbers.append(int(match.group(1)))
    
    return max(numbers) + 1 if numbers else 1

def main():
    title = os.getenv('ISSUE_TITLE', 'Unknown Title')
    body = os.getenv('ISSUE_BODY', '')
    issue_number = os.getenv('ISSUE_NUMBER', '0')
    
    project = extract_field(body, 'Project')
    severity = extract_field(body, 'Severity (ISS)')
    component = extract_field(body, 'Component')
    description = extract_field(body, 'Description')
    reproduction = extract_field(body, 'Steps to Reproduce')
    expected = extract_field(body, 'Expected Behavior')
    
    year = datetime.now().year
    ixe_num = get_next_ixe_number()
    ixe_id = f'IXE-{year}-{ixe_num:04d}'
    
    clean_title = re.sub(r'^\[IXE\]\s*', '', title, flags=re.IGNORECASE).strip()
    
    markdown = f"""# {ixe_id} {clean_title}

## Metadata
- **ID:** {ixe_id}
- **Project:** {project}
- **Severity:** {severity}
- **Component:** {component}
- **Status:** ✅ Resolved
- **Reported:** {datetime.now().strftime('%Y-%m-%d')}
- **Issue:** #{issue_number}

## Description

{description}

## Steps to Reproduce
{reproduction}

## Expected Behavior
{expected}

## Resolution
_Resolution details will be added here._
"""
    
    filename = f'registry/{year}/{ixe_id}.md'
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(markdown)
    
    print(f'Created {filename}')

if __name__ == '__main__':
    main()
