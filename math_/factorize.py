import subprocess


def factorize(s: str) -> list[str]:
    """
    Factorize x by Linux command. Note that args s is string.
    ```
    $ factor 12 -> "b'12: 2 2 3\r\n'"
    ```
    """
    x = str(subprocess.check_output("factor " + s, shell=True))
    return x[x.rfind(":") + 2 : -3].split()
