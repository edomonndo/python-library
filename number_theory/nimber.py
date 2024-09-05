class Nimber:
    exp = [0] * 262300
    log = [0] * 65536

    def __init__(self):
        base = (
            1,
            10279,
            14635,
            32768,
            8445,
            19741,
            56906,
            2583,
            13412,
            58281,
            28045,
            13500,
            43297,
            41331,
            3772,
            3689,
        )

        exp, log = self.exp, self.log
        exp[0] = 1
        for i in range(1, 65535):
            exp[i] = exp[i - 1] << 1
            if exp[i] > 65535:
                exp[i] ^= 92191
        pre = [0] * (65535 + 1)
        for b in range(16):
            s, t = 1 << b, 1 << (b + 1)
            for i in range(s, t):
                pre[i] = pre[i - s] ^ base[b]
        for i in range(65535):
            exp[i] = pre[exp[i]]
            log[exp[i]] = i
        for i in range(65535, 2 * 65535 + 30):
            exp[i] = exp[i - 65535]
        log[0] = 2 * 65535 + 31

    def product_32(self, a: int, b: int) -> int:
        exp, log = self.exp, self.log
        au, al = a >> 16, a & 0xFFFF
        bu, bl = b >> 16, b & 0xFFFF
        l = exp[log[al] + log[bl]]
        ul = exp[log[au ^ al] + log[bu ^ bl]]
        uq = exp[log[au] + log[bu] + 3]
        return ((ul ^ l) << 16) ^ uq ^ l

    def Hproduct_32(self, a: int, b: int) -> int:
        exp, log = self.exp, self.log
        au, al = a >> 16, a & 0xFFFF
        bu, bl = b >> 16, b & 0xFFFF
        l = exp[log[al] + log[bl]]
        ul = exp[log[au ^ al] + log[bu ^ bl]]
        uq = exp[log[au] + log[bu] + 3]
        ku, kl = ul ^ l, uq ^ l
        return (exp[log[ku ^ kl] + 3] << 16) ^ exp[log[ku] + 6]

    def product_64(self, a: int, b: int) -> int:
        a = a & 0xFFFFFFFFFFFFFFFF
        b = b & 0xFFFFFFFFFFFFFFFF
        au, al = a >> 32, a & 0xFFFFFFFF
        bu, bl = b >> 32, b & 0xFFFFFFFF
        l = self.product_32(al, bl)
        ul = self.product_32(au ^ al, bu ^ bl)
        uq = self.Hproduct_32(au, bu)
        return ((ul ^ l) << 32) | (uq ^ l)
