#!/usr/bin/env python3
"""Obscure fields"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Create regex pattern and replace the part needed to be obscure"""
    pattern = '|'.join(re.escape(field) for field in fields)
    return re.sub(f'({pattern})=[^\\{separator}]+',
                  f'\\1={redaction}', message)
