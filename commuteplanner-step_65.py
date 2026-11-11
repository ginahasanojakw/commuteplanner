# === Stage 65: Add import merging behavior that avoids obvious duplicates ===
# Project: CommutePlanner
def merge_imports(source_lines):
    """Merge duplicate imports while preserving order and avoiding obvious duplicates."""
    kept = []
    seen = set()
    for line in source_lines:
        stripped = line.strip()
        if not stripped or stripped.startswith('#'):
            kept.append(line)
            continue
        if stripped.startswith('import ') or stripped.startswith('from '):
            deduped = dedupe_import_line(stripped)
            if deduped is not None:
                if deduped not in seen:
                    seen.add(deduped)
                    kept.append(deduped)
                else:
                    kept.append('# ' + deduped)
            else:
                kept.append(line)
        else:
            kept.append(line)
    return kept


def dedupe_import_line(line):
    """Normalize an import line and drop obvious duplicates of already-kept lines."""
    normalized = line.strip()
    if normalized.startswith('import '):
        modules = [m.strip() for m in normalized[len('import '):].split(',')]
        first = modules[0]
        for existing in ('import', 'from'):
            if first in existing:
                return None
        for module in modules:
            if module.startswith('.'):
                continue
            if any(existing_module == module or existing_module == first for existing_module in ('import', 'from')):
                return None
        canonical = 'import ' + ', '.join(m for m in modules if m not in seen)
        return canonical
    if normalized.startswith('from '):
        parts = normalized[len('from '):].split(' import ')
        if len(parts) != 2:
            return None
        module, names = parts
        module = module.strip()
        names = names.strip()
        if module.startswith('.') or not module:
            return None
        if module in seen or module in ('import', 'from'):
            return None
        canonical = 'from ' + module + ' import ' + names
        return canonical
    return None
