---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/1/ITP1_1_A
    links:
    - https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/1/ITP1_1_A
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/1/ITP1_1_A\n\
    \nif __name__ == \"__main__\":\n    from pathlib import Path\n    import sys\n\
    \n    sys.path.append(str(Path(__file__).resolve().parent.parent.parent))\n  \
    \  from tree.heavy_light_decomposition import HeavyLightDecomposition\n\n    N\
    \ = 12\n    tree = [[1, 6, 10], [2, 5], [3, 4], [], [], [], [7], [8, 9], [], [],\
    \ [11], []]\n    parent = [-1, 0, 1, 2, 2, 1, 0, 6, 7, 7, 0, 10]\n    v_bfs_order\
    \ = [0, 1, 6, 10, 2, 5, 7, 11, 3, 4, 8, 9]\n    hld = HeavyLightDecomposition(N,\
    \ tree, parent, v_bfs_order)\n\n    assert hld.size == [12, 5, 3, 1, 1, 1, 4,\
    \ 3, 1, 1, 2, 1]\n    assert hld.ancestor == [0, 1, 2, 3, 3, 2, 1, 2, 3, 3, 1,\
    \ 2]\n    assert hld.root_in_group == [0, 0, 0, 0, 4, 5, 6, 6, 6, 9, 10, 10]\n\
    \    assert hld.depth == [0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 1, 1], hld.depth\n   \
    \ assert hld.group == [[0, 1, 2, 3], [6, 7, 8], [10, 11], [5], [4], [9]]\n   \
    \ assert hld.group_id == [0, 0, 0, 0, 4, 3, 1, 1, 1, 5, 2, 2]\n    assert hld.depth_in_group\
    \ == [0, 1, 2, 3, 0, 0, 0, 1, 2, 0, 0, 1]\n    assert hld.ET == [0, 1, 2, 3, 4,\
    \ 5, 6, 7, 8, 9, 10, 11]\n    assert hld.ET1 == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,\
    \ 10, 11]\n    assert hld.ET2 == [11, 5, 4, 3, 4, 5, 9, 9, 8, 9, 11, 11]\n\n \
    \   assert hld.path(0, 4) == [(0, 2), (4, 4)]\n    assert hld.path_e(0, 4) ==\
    \ [(1, 2), (4, 4)]\n    assert hld.path_ranges(0, 4) == [(0, 3), (4, 5)]\n   \
    \ assert hld.path_ranges_e(0, 4) == [(1, 3), (4, 5)]\n    assert hld.subtree_range(4)\
    \ == (4, 5)\n    assert hld.subtree_range_e(4) == (5, 5)\n\n    print(\"Hello\
    \ World\")\n"
  dependsOn: []
  isVerificationFile: true
  path: test/unit_test/heavy_light_decomposition.test.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/unit_test/heavy_light_decomposition.test.py
layout: document
redirect_from:
- /verify/test/unit_test/heavy_light_decomposition.test.py
- /verify/test/unit_test/heavy_light_decomposition.test.py.html
title: test/unit_test/heavy_light_decomposition.test.py
---
