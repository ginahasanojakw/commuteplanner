# === Stage 84: Add final cleanup for unused helpers and duplicate code ===
# Project: CommutePlanner
def remove_unused_helpers():
    import ast, os

    for path in os.listdir('.'):
        if not path.endswith('.py'):
            continue
        with open(path) as f:
            tree = ast.parse(f.read())

        names = set()
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                names.add(node.name)
            elif isinstance(node, ast.Name):
                names.add(node.id)

        to_delete = [n for n in names if n.startswith('_') and n not in ('__init__',)]
        return to_delete
