def dubbla(tal):
    return tal * 2

def minst(minsta_varde):
    fn = lambda tal: tal if tal >= 0 else 0
    return fn

minst_noll = minst(0)

def paverka(fn,* tal):
    result - tal
    for thisfn in fn:
        result = thisfn(result)
    return result

r = paverka(dubbla, minst, tal=10)
