import re

def find_sql_injection_vulnerabilities(code):
    patterns = [
        # Look for SQL keywords and suspicious patterns
        r'\bSELECT\b.*?\bFROM\b',
        r'\bUPDATE\b.*?\bSET\b',
        r'\bDELETE\b.*?\bFROM\b',
        r'\bINSERT\b.*?\bINTO\b',
        r'\bOR\b.*?=\s*["\'][^"\']*["\']',
        r'\bUNION\b.*?\bSELECT\b',
        # Look for PHP variables used in SQL queries without proper validation
        r'\$[a-zA-Z_][a-zA-Z0-9_]*\s*=\s*["\'].*\'.*\'.*["\']'
    ]

    matches = []
    for pattern in patterns:
        matches.extend(re.finditer(pattern, code, re.IGNORECASE))

    vulnerabilities = []
    for match in matches:
        vulnerability = {
            'type': 'SQL Injection',
            'pattern': match.group(),
            'line_number': code.count('\n', 0, match.start()) + 1
        }
        vulnerabilities.append(vulnerability)

    return vulnerabilities
