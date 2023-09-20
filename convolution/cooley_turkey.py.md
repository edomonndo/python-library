---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library_checker/convolution/convolution_mod_1000000007.test.py
    title: test/library_checker/convolution/convolution_mod_1000000007.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.12/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.10.12/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "import math\n\n\nclass CooleyTukey:\n    wr = [0] * (1 << 20)\n    wi = [0]\
    \ * (1 << 20)\n    baser = [0] * 20\n    basei = [0] * 20\n\n    @staticmethod\n\
    \    def mul(xr: float, xi: float, yr: float, yi: float) -> tuple:\n        return\
    \ xr * yr - xi * yi, xr * yi + yr * xi\n\n    def genw(self, i: int, b: int, zr:\
    \ float, zi: float) -> None:\n        if b == -1:\n            self.wr[i] = zr\n\
    \            self.wi[i] = zi\n        else:\n            self.genw(i, b - 1, zr,\
    \ zi)\n            wr, wi = self.baser[b], self.basei[b]\n            self.genw(i\
    \ | (1 << b), b - 1, zr * wr - zi * wi, zr * wi + zi * wr)\n\n    def setw(self,\
    \ k: int) -> None:\n        k -= 1\n        arg = math.pi / (1 << k)\n       \
    \ i = 0\n        j = 1 << (k - 1)\n        while j:\n            self.baser[i]\
    \ = math.cos(arg * j)\n            self.basei[i] = math.sin(arg * j)\n       \
    \     i += 1\n            j >>= 1\n        self.genw(0, k - 1, 1, 0)\n\n    def\
    \ fft(self, ar: list, ai: list, k: int) -> None:\n        if k == 0:\n       \
    \     return\n        if k == 1:\n            ar[0], ar[1] = ar[0] + ar[1], ar[0]\
    \ - ar[1]\n            ai[0], ai[1] = ai[0] + ai[1], ai[0] - ai[1]\n         \
    \   return\n        if k & 1:\n            v = 1 << (k - 1)\n            for j\
    \ in range(v):\n                ar[j], ar[j + v] = ar[j] + ar[j + v], ar[j] -\
    \ ar[j + v]\n                ai[j], ai[j + v] = ai[j] + ai[j + v], ai[j] - ai[j\
    \ + v]\n        u = 1 << (k & 1)\n        v = 1 << (k - 2 - (k & 1))\n       \
    \ wr1, wi1 = self.wr[1], self.wi[1]\n        while v:\n            for j0 in range(v):\n\
    \                t0r = ar[j0]\n                t0i = ai[j0]\n                t1r\
    \ = ar[j0 + v]\n                t1i = ai[j0 + v]\n                t2r = ar[j0\
    \ + v * 2]\n                t2i = ai[j0 + v * 2]\n                t3r = ar[j0\
    \ + v * 3]\n                t3i = ai[j0 + v * 3]\n                t1m3r, t1m3i\
    \ = self.mul(t1r - t3r, t1i - t3i, wr1, wi1)\n                ar[j0] = (t0r +\
    \ t2r) + (t1r + t3r)\n                ai[j0] = (t0i + t2i) + (t1i + t3i)\n   \
    \             ar[j0 + v] = (t0r + t2r) - (t1r + t3r)\n                ai[j0 +\
    \ v] = (t0i + t2i) - (t1i + t3i)\n                ar[j0 + v * 2] = (t0r - t2r)\
    \ + t1m3r\n                ai[j0 + v * 2] = (t0i - t2i) + t1m3i\n            \
    \    ar[j0 + v * 3] = (t0r - t2r) - t1m3r\n                ai[j0 + v * 3] = (t0i\
    \ - t2i) - t1m3i\n\n            for jh in range(1, u):\n                p = jh\
    \ * v * 4\n                Wr = self.wr[jh]\n                Wi = self.wi[jh]\n\
    \                Xr = self.wr[jh << 1]\n                Xi = self.wi[jh << 1]\n\
    \                WXr, WXi = self.mul(Wr, Wi, Xr, Xi)\n                for offset\
    \ in range(v):\n                    t0r = ar[p + offset]\n                   \
    \ t0i = ai[p + offset]\n                    t1r, t1i = self.mul(ar[p + offset\
    \ + v], ai[p + offset + v], Xr, Xi)\n                    t2r, t2i = self.mul(\n\
    \                        ar[p + offset + v * 2], ai[p + offset + v * 2], Wr, Wi\n\
    \                    )\n                    t3r, t3i = self.mul(\n           \
    \             ar[p + offset + v * 3], ai[p + offset + v * 3], WXr, WXi\n     \
    \               )\n                    t1m3r, t1m3i = self.mul(t1r - t3r, t1i\
    \ - t3i, wr1, wi1)\n                    ar[p + offset] = (t0r + t2r) + (t1r +\
    \ t3r)\n                    ai[p + offset] = (t0i + t2i) + (t1i + t3i)\n     \
    \               ar[p + offset + v] = (t0r + t2r) - (t1r + t3r)\n             \
    \       ai[p + offset + v] = (t0i + t2i) - (t1i + t3i)\n                    ar[p\
    \ + offset + v * 2] = (t0r - t2r) + t1m3r\n                    ai[p + offset +\
    \ v * 2] = (t0i - t2i) + t1m3i\n                    ar[p + offset + v * 3] = (t0r\
    \ - t2r) - t1m3r\n                    ai[p + offset + v * 3] = (t0i - t2i) - t1m3i\n\
    \            u <<= 2\n            v >>= 2\n\n    def ifft(self, ar: list, ai:\
    \ list, k: int) -> None:\n        if k == 0:\n            return\n        if k\
    \ == 1:\n            ar[0], ar[1] = ar[0] + ar[1], ar[0] - ar[1]\n           \
    \ ai[0], ai[1] = ai[0] + ai[1], ai[0] - ai[1]\n            return\n        u =\
    \ 1 << (k - 2)\n        v = 1\n        wr1, mwi1 = self.wr[1], -self.wi[1]\n \
    \       while u:\n            for j0 in range(v):\n                t0r = ar[j0]\n\
    \                t0i = ai[j0]\n                t1r = ar[j0 + v]\n            \
    \    t1i = ai[j0 + v]\n                t2r = ar[j0 + v * 2]\n                t2i\
    \ = ai[j0 + v * 2]\n                t3r = ar[j0 + v * 3]\n                t3i\
    \ = ai[j0 + v * 3]\n                t2m3r, t2m3i = self.mul(t2r - t3r, t2i - t3i,\
    \ wr1, mwi1)\n                ar[j0] = (t0r + t1r) + (t2r + t3r)\n           \
    \     ai[j0] = (t0i + t1i) + (t2i + t3i)\n                ar[j0 + v * 2] = (t0r\
    \ + t1r) - (t2r + t3r)\n                ai[j0 + v * 2] = (t0i + t1i) - (t2i +\
    \ t3i)\n                ar[j0 + v] = (t0r - t1r) + t2m3r\n                ai[j0\
    \ + v] = (t0i - t1i) + t2m3i\n                ar[j0 + v * 3] = (t0r - t1r) - t2m3r\n\
    \                ai[j0 + v * 3] = (t0i - t1i) - t2m3i\n            for jh in range(1,\
    \ u):\n                p = jh * v * 4\n                Wr = self.wr[jh]\n    \
    \            Wi = -self.wi[jh]\n                Xr = self.wr[(jh << 1) + 0]\n\
    \                Xi = -self.wi[(jh << 1) + 0]\n                Yr = self.wr[(jh\
    \ << 1) + 1]\n                Yi = -self.wi[(jh << 1) + 1]\n                for\
    \ offset in range(v):\n                    t0r = ar[p + offset]\n            \
    \        t0i = ai[p + offset]\n                    t1r = ar[p + offset + v]\n\
    \                    t1i = ai[p + offset + v]\n                    t2r = ar[p\
    \ + offset + v * 2]\n                    t2i = ai[p + offset + v * 2]\n      \
    \              t3r = ar[p + offset + v * 3]\n                    t3i = ai[p +\
    \ offset + v * 3]\n                    t0m1r, t0m1i = self.mul(t0r - t1r, t0i\
    \ - t1i, Xr, Xi)\n                    t2m3r, t2m3i = self.mul(t2r - t3r, t2i -\
    \ t3i, Yr, Yi)\n                    ar[p + offset] = (t0r + t1r) + (t2r + t3r)\n\
    \                    ai[p + offset] = (t0i + t1i) + (t2i + t3i)\n            \
    \        ar[p + offset + v] = t0m1r + t2m3r\n                    ai[p + offset\
    \ + v] = t0m1i + t2m3i\n                    ar[p + offset + v * 2], ai[p + offset\
    \ + v * 2] = self.mul(\n                        (t0r + t1r) - (t2r + t3r), (t0i\
    \ + t1i) - (t2i + t3i), Wr, Wi\n                    )\n                    ar[p\
    \ + offset + v * 3], ai[p + offset + v * 3] = self.mul(\n                    \
    \    t0m1r - t2m3r, t0m1i - t2m3i, Wr, Wi\n                    )\n           \
    \ u >>= 2\n            v <<= 2\n        if k & 1:\n            u = 1 << (k - 1)\n\
    \            for j in range(u):\n                ar[j], ar[j + u] = ar[j] + ar[j\
    \ + u], ar[j] - ar[j + u]\n                ai[j], ai[j + u] = ai[j] + ai[j + u],\
    \ ai[j] - ai[j + u]\n\n    def fft_real(self, ALr: list, ALi: list, AHr: list,\
    \ AHi: list, k: int) -> None:\n        self.fft(ALr, ALi, k)\n        AHr[0] =\
    \ ALi[0] * 2\n        AHi[0] = 0\n        ALr[0] = ALr[0] * 2\n        ALi[0]\
    \ = 0\n        AHr[1] = ALi[1] * 2\n        AHi[1] = 0\n        ALr[1] = ALr[1]\
    \ * 2\n        ALi[1] = 0\n        i = 2\n        y = 2\n        while y < 1 <<\
    \ k:\n            while i < y << 1:\n                j = i ^ (y - 1)\n       \
    \         AHr[i] = ALi[j] + ALi[i]\n                AHi[i] = ALr[j] - ALr[i]\n\
    \                ALr[i] = ALr[j] + ALr[i]\n                ALi[i] = -ALi[j] +\
    \ ALi[i]\n                AHr[j] = AHr[i]\n                AHi[j] = -AHi[i]\n\
    \                ALr[j] = ALr[i]\n                ALi[j] = -ALi[i]\n         \
    \       i += 2\n            y <<= 1\n\n    def karatsuba(self, a: list, b: list,\
    \ mod: int) -> list:\n        B = 32000\n        bbmod = B * B % mod\n       \
    \ l = len(a) + len(b) - 1\n        k = 2\n        M = 4\n        while M < l:\n\
    \            M <<= 1\n            k += 1\n        self.setw(k)\n        alr =\
    \ [float()] * M\n        ali = [float()] * M\n        ahr = [float()] * M\n  \
    \      ahi = [float()] * M\n        blr = [float()] * M\n        bli = [float()]\
    \ * M\n        bhi = [float()] * M\n        bhr = [float()] * M\n        for i,\
    \ x in enumerate(a):\n            quo, rem = divmod(x, B)\n            alr[i],\
    \ ali[i] = float(rem), float(quo)\n        for i, x in enumerate(b):\n       \
    \     quo, rem = divmod(x, B)\n            blr[i], bli[i] = float(rem), float(quo)\n\
    \n        self.fft_real(alr, ali, ahr, ahi, k)\n        self.fft_real(blr, bli,\
    \ bhr, bhi, k)\n\n        for i in range(M):\n            alri = alr[i]\n    \
    \        alii = ali[i]\n            mahii = -ahi[i]\n            ahri = ahr[i]\n\
    \            tmp1r, tmp1i = self.mul(alri, alii, blr[i], bli[i])\n           \
    \ tmp2r, tmp2i = self.mul(mahii, ahri, bhr[i], bhi[i])\n            tmp3r, tmp3i\
    \ = self.mul(alri, alii, bhr[i], bhi[i])\n            tmp4r, tmp4i = self.mul(mahii,\
    \ ahri, blr[i], bli[i])\n            blr[i] = tmp1r + tmp2r\n            bli[i]\
    \ = tmp1i + tmp2i\n            bhr[i] = tmp3r + tmp4r\n            bhi[i] = tmp3i\
    \ + tmp4i\n\n        self.ifft(blr, bli, k)\n        self.ifft(bhr, bhi, k)\n\n\
    \        u = [0] * l\n        im = float(1 / (4 * M))\n        for i in range(l):\n\
    \            x1 = round(blr[i] * im) % mod\n            x2 = (round(bhr[i] * im)\
    \ + round(bhi[i] * im)) % mod * B % mod\n            x3 = round(bli[i] * im) %\
    \ mod * bbmod % mod\n            x = x1 + x2 + x3\n            if x >= mod:\n\
    \                x -= mod\n            if x >= mod:\n                x -= mod\n\
    \            u[i] = x\n        return u\n\n    def karatsuba_pow2(self, a: list,\
    \ mod: int) -> list:\n        B = 32000\n        l = len(a) * 2 - 1\n        k\
    \ = 2\n        M = 4\n        while M < l:\n            M <<= 1\n            k\
    \ += 1\n        self.setw(k)\n        alr = [float()] * M\n        ali = [float()]\
    \ * M\n        ahr = [float()] * M\n        ahi = [float()] * M\n        for i,\
    \ x in enumerate(a):\n            quo, rem = divmod(x, B)\n            alr[i],\
    \ ali[i] = float(rem), float(quo)\n\n        self.fft_real(alr, ali, ahr, ahi,\
    \ k)\n\n        for i in range(M):\n            tmp1r = alr[i]\n            tmp1i\
    \ = ali[i]\n            tmp2r = -ahi[i]\n            tmp2i = ahr[i]\n        \
    \    tmp3r = tmp1r\n            tmp3i = tmp1i\n            tmp4r = tmp2r\n   \
    \         tmp4i = tmp2i\n            tmp1r, tmp1i = self.mul(tmp1r, tmp1i, alr[i],\
    \ ali[i])\n            tmp2r, tmp2i = self.mul(tmp2r, tmp2i, ahr[i], ahi[i])\n\
    \            tmp3r, tmp3i = self.mul(tmp3r, tmp3i, ahr[i], ahi[i])\n         \
    \   tmp4r, tmp4i = self.mul(tmp4r, tmp4i, alr[i], ali[i])\n            alr[i]\
    \ = tmp1r + tmp2r\n            ali[i] = tmp1i + tmp2i\n            ahr[i] = tmp3r\
    \ + tmp4r\n            ahi[i] = tmp3i + tmp4i\n\n        self.ifft(alr, ali, k)\n\
    \        self.ifft(ahr, ahi, k)\n\n        u = [0] * l\n        im = float(1 /\
    \ (4 * M))\n        for i in range(l):\n            alr[i] *= im\n           \
    \ ali[i] *= im\n            ahr[i] *= im\n            ahi[i] *= im\n         \
    \   x1 = round(alr[i]) % mod\n            x2 = (round(ahr[i]) + round(ahi[i]))\
    \ % mod * B % mod\n            x3 = round(ali[i]) % mod * (B * B % mod) % mod\n\
    \            x1 += x2\n            if x1 >= mod:\n                x1 -= mod\n\
    \            x1 += x3\n            if x1 >= mod:\n                x1 -= mod\n\
    \            u[i] = x1\n        return u\n"
  dependsOn: []
  isVerificationFile: false
  path: convolution/cooley_turkey.py
  requiredBy: []
  timestamp: '2023-09-15 08:31:51+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/convolution/convolution_mod_1000000007.test.py
documentation_of: convolution/cooley_turkey.py
layout: document
title: "\u7573\u307F\u8FBC\u307F \u30AB\u30E9\u30C4\u30D0\u6CD5"
---

内容は理解できていない.

多項式 $a_0 + a_1x + a_2x^2 + a_{n-1}x^{n-1}$ を配列 $[a_0, a_1, ..., a_{n-1}]$　で表す.

このとき,$A = [a_0, a_1, ..., a_{n-1}]$ と $B = [b_0, b_1, ..., b_{m-1}]$ から $C = [c_0, c_1, ..., c_{(n-1)+(m-1)}]$ を求める.
ただし,

$$C_k = \displaystyle\sum^{}_{i+j=k} a_i b_j\mod 1,000,000,007$$

###　使い方

```
C = CooleyTukey().karatsuba(A, B, 10**9 + 7)
```