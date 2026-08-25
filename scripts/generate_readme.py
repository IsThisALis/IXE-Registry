import os
import re
from datetime import datetime

def parse_ixe_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    metadata = {}
    
    # Надежный парсинг через Regex
    id_match = re.search(r'\*\*ID:\*\*\s*(.+)', content)
    metadata['id'] = id_match.group(1).strip() if id_match else 'N/A'
    
    proj_match = re.search(r'\*\*Project:\*\*\s*(.+)', content)
    metadata['project'] = proj_match.group(1).strip() if proj_match else 'N/A'
    
    sev_match = re.search(r'\*\*Severity:\*\*\s*(.+)', content)
    metadata['severity'] = sev_match.group(1).strip() if sev_match else 'N/A'
    
    comp_match = re.search(r'\*\*Component:\*\*\s*(.+)', content)
    metadata['component'] = comp_match.group(1).strip() if comp_match else 'N/A'
    
    stat_match = re.search(r'\*\*Status:\*\*\s*(.+)', content)
    metadata['status'] = stat_match.group(1).strip() if stat_match else 'N/A'
    
    # Извлекаем заголовок из первой строки: # IXE-2026-0001 Title Here
    title_match = re.search(r'^#\s*(IXE-\d{4}-\d+)\s+(.*)$', content, re.MULTILINE)
    if title_match and title_match.group(2).strip():
        metadata['title'] = title_match.group(2).strip()
    else:
        metadata['title'] = metadata['id']
    
    metadata['filepath'] = filepath
    return metadata

def generate_readme():
    all_ixes = []
    
    if not os.path.exists('registry'):
        os.makedirs('registry')
        
    for year_dir in os.listdir('registry'):
        year_path = os.path.join('registry', year_dir)
        if not os.path.isdir(year_path):
            continue
        
        for filename in os.listdir(year_path):
            if filename.endswith('.md'):
                filepath = os.path.join(year_path, filename)
                all_ixes.append(parse_ixe_file(filepath))
    
    # Сортировка по ID (новые сверху)
    all_ixes.sort(key=lambda x: x.get('id', ''), reverse=True)
    
    total = len(all_ixes)
    critical = sum(1 for i in all_ixes if 'S1' in i.get('severity', ''))
    resolved = sum(1 for i in all_ixes if '✅' in i.get('status', ''))
    open_count = total - resolved
    
    table_rows = []
    for ixe in all_ixes[:20]:
        status_icon = '✅' if '✅' in ixe.get('status', '') else '🔧'
        
        # Защита от случайных звездочек в данных
        clean_id = ixe['id'].replace('**', '').strip()
        clean_proj = ixe.get('project', 'N/A').replace('**', '').strip()
        clean_sev = ixe.get('severity', 'N/A').replace('**', '').strip()
        clean_comp = ixe.get('component', 'N/A').replace('**', '').strip()
        clean_title = ixe.get('title', 'N/A').replace('**', '').strip()
        
        table_rows.append(
            f"| [{clean_id}]({ixe['filepath']}) | {clean_proj} | "
            f"{clean_sev} | {clean_comp} | "
            f"{clean_title} | {status_icon} |"
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
{chr(10).join(table_rows) if table_rows else "| _No entries yet_ | | | | | |"}

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
