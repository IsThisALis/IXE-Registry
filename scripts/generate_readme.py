import os
import re
from datetime import datetime

def parse_ixe_file(filepath):
    """Parse IXE markdown file and extract metadata"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    metadata = {}
    for line in content.split('\n'):
        if line.startswith('- **ID:**'):
            metadata['id'] = line.split(':', 1)[1].strip()
        elif line.startswith('- **Project:**'):
            metadata['project'] = line.split(':', 1)[1].strip()
        elif line.startswith('- **Severity:**'):
            metadata['severity'] = line.split(':', 1)[1].strip()
        elif line.startswith('- **Component:**'):
            metadata['component'] = line.split(':', 1)[1].strip()
        elif line.startswith('- **Status:**'):
            metadata['status'] = line.split(':', 1)[1].strip()
    
    # Extract title from first line
    title_match = re.search(r'^# (IXE-\d{4}-\d+)\s+(.*)$', content, re.MULTILINE)
    if title_match:
        metadata['title'] = title_match.group(2)
    else:
        metadata['title'] = 'N/A'
    
    metadata['filepath'] = filepath
    return metadata

def generate_readme():
    """Generate README.md from all IXE files"""
    all_ixes = []
    
    for year_dir in os.listdir('registry'):
        year_path = os.path.join('registry', year_dir)
        if not os.path.isdir(year_path):
            continue
        
        for filename in os.listdir(year_path):
            if filename.endswith('.md'):
                filepath = os.path.join(year_path, filename)
                all_ixes.append(parse_ixe_file(filepath))
    
    # Sort by ID descending
    all_ixes.sort(key=lambda x: x.get('id', ''), reverse=True)
    
    # Calculate statistics
    total = len(all_ixes)
    critical = sum(1 for i in all_ixes if 'S1' in i.get('severity', ''))
    resolved = sum(1 for i in all_ixes if '✅' in i.get('status', ''))
    open_count = total - resolved
    
    # Generate table
    table_rows = []
    for ixe in all_ixes[:20]:  # Show last 20
        status_icon = '✅' if '✅' in ixe.get('status', '') else '🔧'
        table_rows.append(
            f"| [{ixe['id']}]({ixe['filepath']}) | {ixe.get('project', 'N/A')} | "
            f"{ixe.get('severity', 'N/A')} | {ixe.get('component', 'N/A')} | "
            f"{ixe.get('title', 'N/A')} | {status_icon} |"
        )
    
    readme = f"""# IXE Registry

Official registry of IsThisALis eXceptions and Exposures.

## Statistics
- **Total IXE:** {total}
- **Critical (S1):** {critical}
- **Open:** {open_count}
- **Resolved:** {resolved}

## Recent IXE

| ID | Project | Severity | Component | Title | Status |
|----|---------|----------|-----------|-------|--------|
{chr(10).join(table_rows)}

## How to report
1. Create a new issue using the IXE template
2. Fill in all required fields
3. Close the issue when resolved
4. GitHub Actions will automatically update this registry

## Severity Levels
- **S1 (Critical):** System crash, data loss, security vulnerability
- **S2 (Major):** Feature broken, workaround exists
- **S3 (Minor):** Minor bug, cosmetic issue
- **S4 (Cosmetic):** Typos, refactoring, documentation

_Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}_
"""
    
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(readme)
    
    print(f'Updated README.md with {total} IXE entries')

if __name__ == '__main__':
    generate_readme()
