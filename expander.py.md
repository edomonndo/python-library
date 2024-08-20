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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "import sys\nimport os\n\nif __name__ == \"__main__\":\n\n    # source_file\
    \ = sys.argv[1]\n    source_file = \"main.py\"\n    if not os.path.exists(source_file):\n\
    \        raise FileNotFoundError\n\n    standard_imports = set()\n    sort_order\
    \ = dict()\n    library_imports = set()\n    import_functions = dict()\n    output_lines\
    \ = dict()\n    const = set()\n\n    defind_const = [\n        \"MOD = 998244353\"\
    ,\n        'T = TypeVar(\"T\")',\n        'S = TypeVar(\"S\")',\n        'F =\
    \ TypeVar(\"F\")',\n    ]\n\n    res = []\n    order = 0\n\n    def dfs(input_file:\
    \ str):\n        global order\n        sort_order[input_file] = order\n      \
    \  order -= 1\n        try:\n            with open(input_file, mode=\"r\", encoding=\"\
    utf-8\") as f:\n                lines = f.readlines()\n\n            for line\
    \ in lines:\n                if line.startswith(\"from\"):\n                 \
    \   prefix, path, _, *funcs = line.split()\n                    fpath = path.replace(\"\
    .\", \"/\") + \".py\"\n                    if os.path.exists(fpath):\n       \
    \                 dfs(fpath)\n                        library_imports.add(fpath)\n\
    \                        for func in funcs:\n                            if fpath\
    \ not in import_functions:\n                                import_functions[fpath]\
    \ = set()\n                            import_functions[fpath].add(func)\n   \
    \                 else:\n                        standard_imports.add(path)\n\
    \                        for func in funcs:\n                            if path\
    \ not in import_functions:\n                                import_functions[path]\
    \ = set()\n                            if func.endswith(\",\"):\n            \
    \                    func = func[:-1]\n                            import_functions[path].add(func)\n\
    \n            output_lines[input_file] = []\n            for line in lines:\n\
    \                if line.startswith(\"from\"):\n                    continue\n\
    \                if line.strip() in defind_const:\n                    const.add(line)\n\
    \                    continue\n                output_lines[input_file].append(line)\n\
    \n        except FileNotFoundError:\n            pass\n\n    dfs(source_file)\n\
    \n    library_imports = sorted(library_imports, key=lambda p: sort_order[p])\n\
    \    const = sorted(const, key=lambda s: defind_const.index(s.strip()))\n\n  \
    \  with open(\"bundled.py\", mode=\"w\", encoding=\"utf-8\") as f:\n\n       \
    \ for module in standard_imports:\n            f.write(f\"from {module} import\
    \ \")\n            if \"*\" in import_functions[module]:\n                f.write(\"\
    *\")\n            else:\n                f.write(\", \".join(sorted(import_functions[module])))\n\
    \            f.write(\"\\n\")\n        if standard_imports:\n            f.write(\"\
    \\n\")\n\n        for line in const:\n            f.write(line)\n        if const:\n\
    \            f.write(\"\\n\")\n\n        for path in library_imports:\n      \
    \      for line in output_lines[path]:\n                f.write(line)\n      \
    \      f.write(\"\\n\")\n        if library_imports:\n            f.write(\"\\\
    n\")\n\n        for line in output_lines[source_file]:\n            f.write(line)\n\
    \        f.write(\"\\n\")\n"
  dependsOn: []
  isVerificationFile: false
  path: expander.py
  requiredBy: []
  timestamp: '2024-08-20 10:54:57+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: expander.py
layout: document
redirect_from:
- /library/expander.py
- /library/expander.py.html
title: expander.py
---
