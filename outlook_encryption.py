
from py_mini_racer.py_mini_racer import MiniRacer
ctx = MiniRacer()

ctx.eval("""

var Key="e=10001;m=abef72b26a0f2555ad7e7f8b3f4972878235c2df6ea147e58f062a176964eb6dda829756960fdec18fbcabb9cf4d57493ef885093f4bd1a846a63bdebdeefd20eebe71d9f5eb6f8ddb8e9ee7c9de12c6f6963f8486a3434ce0289eeaf5fea94ae1474e13ebcd03d0b7ffdb353b9db4abdda91240bb03e5110282743a9bfe993e578b49b0adde478b3caf7d8a0c7b0355ff8ef106018cedcccfde2db51bca63af10bbb30ce1168d5efdb5e84b01b02c2ffe4d5b6b6c67e1ea54be792a887fc41a866591bfe7afab22c80db20d50d6515dcaa6b039ca3c06dbc623817340d429f43e7a079858f4b863990074051e7d7109be2f1f194114b25537d63ec630b4d789"; 
var randomNum="B28BB58107DA565EFE9179FCE862E15FC720287BD9697F08DCD547132EC71F67C97B3AB701E73E1800B01015945388FFD3EA2C6648DBB6A79F494F37D000FB5258C689E2EED2349789F65CFD4FC6B8D2018E9C3E8EFDDBE024C4B7FE9D25A6A718D4ECC0"; 
var SKI="4B8F32B06B3633468A617C4D5781E6B301099447";

function Encrypt(e, t, n, a,key,num,sk) {
    Key=key;
    randomNum=num;
    SKI=sk;
    var i = [];
    switch (n.toLowerCase()) {
        case "chgsqsa":
            if (null == e || null == t) {
                return null
            }
            i = PackageSAData(e, t);
            break;
        case "chgpwd":
            if (null == e || null == a) {
                return null
            }
            i = PackageNewAndOldPwd(e, a);
            break;
        case "pwd":
            if (null == e) {
                return null
            }
            i = PackagePwdOnly(e);
            break;
        case "pin":
            if (null == e) {
                return null
            }
            i = PackagePinOnly(e);
            break;
        case "proof":
            if (null == e && null == t) {
                return null
            }
            i = PackageLoginIntData(null != e ? e : t);
            break;
        case "saproof":
            if (null == t) {
                return null
            }
            i = PackageSADataForProof(t);
            break;
        case "newpwd":
            if (null == a) {
                return null
            }
            i = PackageNewPwdOnly(a)
    }
    if (null == i || "undefined" == typeof i) {
        return i
    }
    if ("undefined" != typeof Key && void 0 !== parseRSAKeyFromString) {
        console.log('here')
        var o = parseRSAKeyFromString(Key)
    }
    // print()
    console.log(i,o)
    var r = RSAEncrypt(i, o, randomNum);
    console.log('Value =  ');
    console.log(r);
    return r
}
function hexStringToMP(e){var t,n,a=Math.ceil(e.length/4),i=new JSMPnumber;for(i.size=a,t=0;a>t;t++){n=e.substr(4*t,4),i.data[a-1-t]=parseInt(n,16)}return i}
function PackageSAData(e, t) {
    var n = [],
        a = 0;
    n[a++] = 1, n[a++] = 1, n[a++] = 0;
    var i, o = t.length;
    for (n[a++] = 2 * o, i = 0; o > i; i++) {
        n[a++] = 255 & t.charCodeAt(i), n[a++] = (65280 & t.charCodeAt(i)) >> 8
    }
    var r = e.length;
    for (n[a++] = r, i = 0; r > i; i++) {
        n[a++] = 127 & e.charCodeAt(i)
    }
    return n
}

function PackagePwdOnly(e) {
    var t = [],
        n = 0;
    t[n++] = 1, t[n++] = 1, t[n++] = 0, t[n++] = 0;
    var a, i = e.length;
    for (t[n++] = i, a = 0; i > a; a++) {
        t[n++] = 127 & e.charCodeAt(a)
    }
    return t
}

function PackagePinOnly(e) {
    var t = [],
        n = 0;
    t[n++] = 1, t[n++] = 2, t[n++] = 0, t[n++] = 0, t[n++] = 0;
    var a, i = e.length;
    for (t[n++] = i, a = 0; i > a; a++) {
        t[n++] = 127 & e.charCodeAt(a)
    }
    return t
}

function PackageLoginIntData(e) {
    var t, n = [],
        a = 0;
    for (t = 0; t < e.length; t++) {
        n[a++] = 255 & e.charCodeAt(t), n[a++] = (65280 & e.charCodeAt(t)) >> 8
    }
    return n
}

function PackageSADataForProof(e) {
    var t, n = [],
        a = 0;
    for (t = 0; t < e.length; t++) {
        n[a++] = 127 & e.charCodeAt(t), n[a++] = (65280 & e.charCodeAt(t)) >> 8
    }
    return n
}

function PackageNewPwdOnly(e) {
    var t = [],
        n = 0;
    t[n++] = 1, t[n++] = 1;
    var a, i = e.length;
    for (t[n++] = i, a = 0; i > a; a++) {
        t[n++] = 127 & e.charCodeAt(a)
    }
    return t[n++] = 0, t[n++] = 0, t
}

function PackageNewAndOldPwd(e, t) {
    var n = [],
        a = 0;
    n[a++] = 1, n[a++] = 1;
    var i, o = t.length;
    for (n[a++] = o, i = 0; o > i; i++) {
        n[a++] = 127 & t.charCodeAt(i)
    }
    for (n[a++] = 0, o = e.length, n[a++] = o, i = 0; o > i; i++) {
        n[a++] = 127 & e.charCodeAt(i)
    }
    return n
}

function mapByteToBase64(e) {
    return e >= 0 && 26 > e ? String.fromCharCode(65 + e) : e >= 26 && 52 > e ? String.fromCharCode(97 + e - 26) : e >= 52 && 62 > e ? String.fromCharCode(48 + e - 52) : 62 == e ? "+" : "/"
}

function base64Encode(e, t) {
    var n, a = "";
    for (n = t; 4 > n; n++) {
        e >>= 6
    }
    for (n = 0; t > n; n++) {
        a = mapByteToBase64(63 & e) + a, e >>= 6
    }
    return a
}

function byteArrayToBase64(e) {
    var t, n, a = e.length,
        i = "";
    for (t = a - 3; t >= 0; t -= 3) {
        n = e[t] | e[t + 1] << 8 | e[t + 2] << 16, i += base64Encode(n, 4)
    }
    var o = a % 3;
    for (n = 0, t += 2; t >= 0; t--) {
        n = n << 8 | e[t]
    }
    return 1 == o ? i = i + base64Encode(n << 16, 2) + "==" : 2 == o && (i = i + base64Encode(n << 8, 3) + "="), i
}

function parseRSAKeyFromString(e) {
    var t = e.indexOf(";");
    if (0 > t) {
        return null
    }
    var n = e.substr(0, t),
        a = e.substr(t + 1),
        i = n.indexOf("=");
    if (0 > i) {
        return null
    }
    var o = n.substr(i + 1);
    if (i = a.indexOf("="), 0 > i) {
        return null
    }
    var r = a.substr(i + 1),
        s = new Object;
    return s.n = hexStringToMP(r), s.e = parseInt(o, 16), s
}

function RSAEncrypt(e, t) {
    for (var n = [], a = 42, i = 2 * t.n.size - a, o = 0; o < e.length; o += i) {
        if (o + i >= e.length) {
            var r = RSAEncryptBlock(e.slice(o), t, randomNum);
            r && (n = r.concat(n))
        } else {
            var r = RSAEncryptBlock(e.slice(o, o + i), t, randomNum);
            r && (n = r.concat(n))
        }
    }
    var s = byteArrayToBase64(n);
    return s
}
function RSAEncryptBlock(e, t, n) {
    var a = t.n,
        i = t.e,
        o = e.length,
        r = 2 * a.size,
        s = 42;
    if (o + s > r) {
        return null
    }
    applyPKCSv2Padding(e, r, n), e = e.reverse();
    var l = byteArrayToMP(e),
        d = modularExp(l, i, a);
    d.size = a.size;
    var c = mpToByteArray(d);
    return c = c.reverse()
}

function JSMPnumber() {
    this.size = 1, this.data = [], this.data[0] = 0
}

function duplicateMP(e) {
    var t = new JSMPnumber;
    return t.size = e.size, t.data = e.data.slice(0), t
}

function byteArrayToMP(e) {
    var t = new JSMPnumber,
        n = 0,
        a = e.length,
        i = a >> 1;
    for (n = 0; i > n; n++) {
        t.data[n] = e[2 * n] + (e[1 + 2 * n] << 8)
    }
    return a % 2 && (t.data[n++] = e[a - 1]), t.size = n, t
}

function mpToByteArray(e) {
    var t = [],
        n = 0,
        a = e.size;
    for (n = 0; a > n; n++) {
        t[2 * n] = 255 & e.data[n];
        var i = e.data[n] >>> 8;
        t[2 * n + 1] = i
    }
    return t
}

function modularExp(e, t, n) {
    for (var a = [], i = 0; t > 0;) {
        a[i] = 1 & t, t >>>= 1, i++
    }
    for (var o = duplicateMP(e), r = i - 2; r >= 0; r--) {
        o = modularMultiply(o, o, n), 1 == a[r] && (o = modularMultiply(o, e, n))
    }
    return o
}

function modularMultiply(e, t, n) {
    var a = multiplyMP(e, t),
        i = divideMP(a, n);
    return i.r
}

function multiplyMP(e, t) {
    var n = new JSMPnumber;
    n.size = e.size + t.size;
    var a, i;
    for (a = 0; a < n.size; a++) {
        n.data[a] = 0
    }
    var o = e.data,
        r = t.data,
        s = n.data;
    if (e == t) {
        for (a = 0; a < e.size; a++) {
            s[2 * a] += o[a] * o[a]
        }
        for (a = 1; a < e.size; a++) {
            for (i = 0; a > i; i++) {
                s[a + i] += 2 * o[a] * o[i]
            }
        }
    } else {
        for (a = 0; a < e.size; a++) {
            for (i = 0; i < t.size; i++) {
                s[a + i] += o[a] * r[i]
            }
        }
    }
    return normalizeJSMP(n), n
}

function normalizeJSMP(e) {
    var t, n, a, i, o;
    for (a = e.size, n = 0, t = 0; a > t; t++) {
        i = e.data[t], i += n, o = i, n = Math.floor(i / 65536), i -= 65536 * n, e.data[t] = i
    }
}

function removeLeadingZeroes(e) {
    for (var t = e.size - 1; t > 0 && 0 == e.data[t--];) {
        e.size--
    }
}

function divideMP(e, t) {
    var n = e.size,
        a = t.size,
        i = t.data[a - 1],
        o = t.data[a - 1] + t.data[a - 2] / 65536,
        r = new JSMPnumber;
    r.size = n - a + 1, e.data[n] = 0;
    for (var s = n - 1; s >= a - 1; s--) {
        var l = s - a + 1,
            d = Math.floor((65536 * e.data[s + 1] + e.data[s]) / o);
        if (d > 0) {
            var c = multiplyAndSubtract(e, d, t, l);
            for (0 > c && (d--, multiplyAndSubtract(e, d, t, l)); c > 0 && e.data[s] >= i;) {
                c = multiplyAndSubtract(e, 1, t, l), c > 0 && d++
            }
        }
        r.data[l] = d
    }
    removeLeadingZeroes(e);
    var u = {
        "q": r,
        "r": e
    };
    return u
}

function multiplyAndSubtract(e, t, n, a) {
    var i, o = e.data.slice(0),
        r = 0,
        s = e.data;
    for (i = 0; i < n.size; i++) {
        var l = r + n.data[i] * t;
        r = l >>> 16, l -= 65536 * r, l > s[i + a] ? (s[i + a] += 65536 - l, r++) : s[i + a] -= l
    }
    return r > 0 && (s[i + a] -= r), s[i + a] < 0 ? (e.data = o.slice(0), -1) : 1
}

function applyPKCSv2Padding(e, t, n) {
    var a, i = e.length,
        o = [218, 57, 163, 238, 94, 107, 75, 13, 50, 85, 191, 239, 149, 96, 24, 144, 175, 216, 7, 9],
        r = t - i - 40 - 2,
        s = [];
    for (a = 0; r > a; a++) {
        s[a] = 0
    }
    s[r] = 1;
    var l = o.concat(s, e),
        d = [];
    for (a = 0; 20 > a; a++) {
        d[a] = Math.floor(256 * Math.random())
    }
    d = SHA1(d.concat(n));
    var c = MGF(d, t - 21),
        u = XORarrays(l, c),
        p = MGF(u, 20),
        m = XORarrays(d, p),
        g = [];
    for (g[0] = 0, g = g.concat(m, u), a = 0; a < g.length; a++) {
        e[a] = g[a]
    }
}

function MGF(e, t) {
    if (t > 4096) {
        return null
    }
    var n = e.slice(0),
        a = n.length;
    n[a++] = 0, n[a++] = 0, n[a++] = 0, n[a] = 0;
    for (var i = 0, o = []; o.length < t;) {
        n[a] = i++, o = o.concat(SHA1(n))
    }
    return o.slice(0, t)
}

function XORarrays(e, t) {
    if (e.length != t.length) {
        return null
    }
    for (var n = [], a = e.length, i = 0; a > i; i++) {
        n[i] = e[i] ^ t[i]
    }
    return n
}

function SHA1(e) {
    var t, n = e.slice(0);
    PadSHA1Input(n);
    var a = {
        "A": 1732584193,
        "B": 4023233417,
        "C": 2562383102,
        "D": 271733878,
        "E": 3285377520
    };
    for (t = 0; t < n.length; t += 64) {
        SHA1RoundFunction(a, n, t)
    }
    var i = [];
    return wordToBytes(a.A, i, 0), wordToBytes(a.B, i, 4), wordToBytes(a.C, i, 8), wordToBytes(a.D, i, 12), wordToBytes(a.E, i, 16), i
}

function wordToBytes(e, t, n) {
    var a;
    for (a = 3; a >= 0; a--) {
        t[n + a] = 255 & e, e >>>= 8
    }
}

function PadSHA1Input(e) {
    var t, n = e.length,
        a = n,
        i = n % 64,
        o = 55 > i ? 56 : 120;
    for (e[a++] = 128, t = i + 1; o > t; t++) {
        e[a++] = 0
    }
    var r = 8 * n;
    for (t = 1; 8 > t; t++) {
        e[a + 8 - t] = 255 & r, r >>>= 8
    }
}

function SHA1RoundFunction(e, t, n) {
    var a, i, o, r = 1518500249,
        s = 1859775393,
        l = 2400959708,
        d = 3395469782,
        c = [],
        u = e.A,
        p = e.B,
        m = e.C,
        g = e.D,
        f = e.E;
    for (i = 0, o = n; 16 > i; i++, o += 4) {
        c[i] = t[o] << 24 | t[o + 1] << 16 | t[o + 2] << 8 | t[o + 3] << 0
    }
    for (i = 16; 80 > i; i++) {
        c[i] = rotateLeft(c[i - 3] ^ c[i - 8] ^ c[i - 14] ^ c[i - 16], 1)
    }
    var v;
    for (a = 0; 20 > a; a++) {
        v = rotateLeft(u, 5) + (p & m | ~p & g) + f + c[a] + r & 4294967295, f = g, g = m, m = rotateLeft(p, 30), p = u, u = v
    }
    for (a = 20; 40 > a; a++) {
        v = rotateLeft(u, 5) + (p ^ m ^ g) + f + c[a] + s & 4294967295, f = g, g = m, m = rotateLeft(p, 30), p = u, u = v
    }
    for (a = 40; 60 > a; a++) {
        v = rotateLeft(u, 5) + (p & m | p & g | m & g) + f + c[a] + l & 4294967295, f = g, g = m, m = rotateLeft(p, 30), p = u, u = v
    }
    for (a = 60; 80 > a; a++) {
        v = rotateLeft(u, 5) + (p ^ m ^ g) + f + c[a] + d & 4294967295, f = g, g = m, m = rotateLeft(p, 30), p = u, u = v
    }
    e.A = e.A + u & 4294967295, e.B = e.B + p & 4294967295, e.C = e.C + m & 4294967295, e.D = e.D + g & 4294967295, e.E = e.E + f & 4294967295
}

function rotateLeft(e, t) {
    var n = e >>> 32 - t,
        a = (1 << 32 - t) - 1,
        i = e & a;
    return i << t | n
}


""")

