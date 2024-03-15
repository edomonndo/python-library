---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "import argparse\nimport ast\nimport importlib\nimport inspect\nimport re\n\
    from typing import List, Optional, cast\n\n\nclass ImportInfo:\n    def __init__(self,\
    \ lineno: int, end_lineno: int,\n                 import_from: Optional[str] =\
    \ None,\n                 name: Optional[str] = None,\n                 asname:\
    \ Optional[str] = None) -> None:\n        self.lineno = lineno\n        self.end_lineno\
    \ = end_lineno\n        self.import_from = import_from\n        self.name = name\n\
    \        self.asname = asname\n\n\ndef iter_child_nodes(\n        node: ast.AST,\n\
    \        import_info: Optional[ImportInfo] = None) -> List[ImportInfo]:\n    result\
    \ = []\n\n    if isinstance(node, ast.alias):\n        if import_info:\n     \
    \       result.append(ImportInfo(\n                import_info.lineno, import_info.end_lineno,\n\
    \                import_info.import_from, node.name, node.asname))\n        return\
    \ result\n\n    if isinstance(node, ast.Import):\n        for name in node.names:\n\
    \            if re.match(r'^atcoder\\.?', name.name):\n                if hasattr(node,\
    \ 'end_lineno'):\n                    end_lineno = cast(int, node.end_lineno)\
    \  # type: ignore\n                else:\n                    end_lineno = node.lineno\n\
    \                import_info = ImportInfo(node.lineno, end_lineno)\n    elif isinstance(node,\
    \ ast.ImportFrom):\n        if re.match(r'^atcoder\\.?', cast(str, node.module)):\n\
    \            if hasattr(node, 'end_lineno'):\n                end_lineno = cast(int,\
    \ node.end_lineno)  # type: ignore\n            else:\n                end_lineno\
    \ = node.lineno\n            import_info = ImportInfo(node.lineno, end_lineno,\
    \ node.module)\n\n    for child in ast.iter_child_nodes(node):\n        result\
    \ += iter_child_nodes(child, import_info)\n    return result\n\n\nclass ModuleImporter:\n\
    \    def __init__(self) -> None:\n        self.imported_modules: List[str] = []\n\
    \n    def import_module(self, import_from: Optional[str], name: str,\n       \
    \               asname: Optional[str] = None) -> str:\n        result = ''\n\n\
    \        if import_from is None:\n            module_name = name\n        else:\n\
    \            try:\n                module_name = import_from + '.' + name\n  \
    \              importlib.import_module(module_name)\n            except ImportError:\n\
    \                module_name = import_from\n\n        if module_name not in self.imported_modules:\n\
    \            self.imported_modules.append(module_name)\n\n            module =\
    \ importlib.import_module(module_name)\n            source = inspect.getsource(module)\n\
    \            lines = source.split('\\n')\n            imports = iter_child_nodes(ast.parse(source))\n\
    \n            import_lines = []\n            for import_info in imports:\n   \
    \             result += self.import_module(\n                    import_info.import_from,\
    \ cast(str, import_info.name),\n                    import_info.asname)\n    \
    \            for line in range(import_info.lineno - 1,\n                     \
    \             import_info.end_lineno):\n                    import_lines.append(line)\n\
    \n            for lineno, line_str in enumerate(lines):\n                if lineno\
    \ not in import_lines:\n                    continue\n                lines[lineno]\
    \ = '# ' + line_str  # TODO(not): indent\n\n            modules = module_name.split('.')\n\
    \            for i in range(len(modules) - 1):\n                result += self.import_module(None,\
    \ '.'.join(modules[:i + 1]))\n\n            code = '_' + module_name.replace('.',\
    \ '_') + '_code'\n            result += f'{code} = \"\"\"\\n'\n            result\
    \ += '\\n'.join(lines)\n            result += '\"\"\"\\n\\n'\n            result\
    \ += f\"{module_name} = types.ModuleType('{module_name}')\\n\"\n\n           \
    \ # TODO(not): asname\n            imported = []\n            for import_info\
    \ in imports:\n                if import_info.import_from is None:\n         \
    \           modules = cast(str, import_info.name).split('.')\n               \
    \     for i in range(len(modules)):\n                        import_name = '.'.join(modules[:i\
    \ + 1])\n                        if import_name in imported:\n               \
    \             continue\n                        imported.append(import_name)\n\
    \                        result += f\"{module_name}.__dict__['{import_name}']\"\
    \ \\\n                            f\" = {import_name}\\n\"\n                else:\n\
    \                    result += f\"{module_name}.__dict__['{import_info.name}']\"\
    \ \\\n                        f\" = {import_info.import_from}.{import_info.name}\\\
    n\"\n\n            result += f'exec({code}, {module_name}.__dict__)\\n'\n\n  \
    \      if import_from is None:\n            if asname is None:\n             \
    \   if name != module_name:\n                    result += f'{name} = {module_name}\\\
    n'\n            else:\n                result += f'{asname} = {module_name}\\\
    n'\n        else:\n            if asname is None:\n                if name !=\
    \ import_from + '.' + name:\n                    result += f'{name} = {import_from}.{name}\\\
    n'\n            else:\n                result += f'{asname} = {import_from}.{name}\\\
    n'\n\n        return result + '\\n'\n\n\ndef main() -> None:\n    parser = argparse.ArgumentParser()\n\
    \    parser.add_argument('src', help='Source code')\n    parser.add_argument('-o',\
    \ '--output', help='Single combined code')\n    args = parser.parse_args()\n\n\
    \    with open(args.src) as f:\n        lines = f.readlines()\n    imports = iter_child_nodes(ast.parse(''.join(lines)))\n\
    \n    importer = ModuleImporter()\n    result = 'import types\\n\\n'\n    import_lines\
    \ = []\n    for import_info in imports:\n        result += importer.import_module(\n\
    \            import_info.import_from, cast(str, import_info.name),\n         \
    \   import_info.asname)\n        for line in range(import_info.lineno - 1, import_info.end_lineno):\n\
    \            import_lines.append(line)\n\n    for lineno, line_str in enumerate(lines):\n\
    \        if lineno not in import_lines:\n            continue\n        lines[lineno]\
    \ = '# ' + line_str  # TODO(not): indent\n    result += ''.join(lines)\n\n   \
    \ if args.output:\n        with open(args.output, 'w') as f:\n            f.write(result)\n\
    \    else:\n        print(result, end='')\n\n\nif __name__ == '__main__':\n  \
    \  main()\n"
  dependsOn: []
  isVerificationFile: false
  path: atcoder/__main__.py
  requiredBy: []
  timestamp: '2024-02-05 08:23:41+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: atcoder/__main__.py
layout: document
redirect_from:
- /library/atcoder/__main__.py
- /library/atcoder/__main__.py.html
title: atcoder/__main__.py
---
