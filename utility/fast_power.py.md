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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def fast_power(base, power, mod=1000000007):\n    \"\"\"\n    Returns the\
    \ result of a^b i.e. a**b\n    We assume that a >= 1 and b >= 0\n\n    Remember\
    \ two things!\n     - Divide power by 2 and multiply base to itself (if the power\
    \ is even)\n     - Decrement power by 1 to make it even and then follow the first\
    \ step\n    \"\"\"\n\n    result = 1\n    while power > 0:\n        # If power\
    \ is odd\n        if power % 2 == 1:\n            result = (result * base) % mod\n\
    \n        # Divide the power by 2\n        power = power // 2\n        # Multiply\
    \ base to itself\n        base = (base * base) % mod\n\n    return result\n\n\n\
    if __name__ == \"__main__\":\n    assert fast_power(2, 1) == 2\n    assert fast_power(2,\
    \ 2) == 4\n    assert fast_power(2, 4) == 16\n    assert fast_power(2, 100) ==\
    \ 976371285\n"
  dependsOn: []
  isVerificationFile: false
  path: utility/fast_power.py
  requiredBy: []
  timestamp: '2023-07-23 00:15:14+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: utility/fast_power.py
layout: document
title: "\u51AA\u4E57"
---

