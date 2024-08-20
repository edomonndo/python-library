import sys
import os

if __name__ == "__main__":

    # source_file = sys.argv[1]
    source_file = "main.py"
    if not os.path.exists(source_file):
        raise FileNotFoundError

    standard_imports = set()
    sort_order = dict()
    library_imports = set()
    import_functions = dict()
    output_lines = dict()
    const = set()

    defind_const = [
        "MOD = 998244353",
        'T = TypeVar("T")',
        'S = TypeVar("S")',
        'F = TypeVar("F")',
    ]

    res = []
    order = 0

    def dfs(input_file: str):
        global order
        sort_order[input_file] = order
        order -= 1
        try:
            with open(input_file, mode="r", encoding="utf-8") as f:
                lines = f.readlines()

            for line in lines:
                if line.startswith("from"):
                    prefix, path, _, *funcs = line.split()
                    fpath = path.replace(".", "/") + ".py"
                    if os.path.exists(fpath):
                        dfs(fpath)
                        library_imports.add(fpath)
                        for func in funcs:
                            if fpath not in import_functions:
                                import_functions[fpath] = set()
                            import_functions[fpath].add(func)
                    else:
                        standard_imports.add(path)
                        for func in funcs:
                            if path not in import_functions:
                                import_functions[path] = set()
                            if func.endswith(","):
                                func = func[:-1]
                            import_functions[path].add(func)

            output_lines[input_file] = []
            for line in lines:
                if line.startswith("from"):
                    continue
                if line.strip() in defind_const:
                    const.add(line)
                    continue
                output_lines[input_file].append(line)

        except FileNotFoundError:
            pass

    dfs(source_file)

    library_imports = sorted(library_imports, key=lambda p: sort_order[p])
    const = sorted(const, key=lambda s: defind_const.index(s.strip()))

    with open("bundled.py", mode="w", encoding="utf-8") as f:

        for module in standard_imports:
            f.write(f"from {module} import ")
            if "*" in import_functions[module]:
                f.write("*")
            else:
                f.write(", ".join(sorted(import_functions[module])))
            f.write("\n")
        if standard_imports:
            f.write("\n")

        for line in const:
            f.write(line)
        if const:
            f.write("\n")

        for path in library_imports:
            for line in output_lines[path]:
                f.write(line)
            f.write("\n")
        if library_imports:
            f.write("\n")

        for line in output_lines[source_file]:
            f.write(line)
        f.write("\n")
