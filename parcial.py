#!/usr/bin/env python3
"""Herramientas offline para el parcial de Sistemas Operativos. Solo libreria estandar.

USO
  python parcial.py buscar archivo.txt                 # modo interactivo: escribes la pregunta, te da fragmentos
  python parcial.py buscar archivo.txt -q "banquero necesidad" -n 10
  python parcial.py ajuste --huecos "0x1000/0x500,0x3000/0x200" --req "0x300,0x100"
  python parcial.py banquero --asig "0,1,0;2,0,0" --max "7,5,3;3,2,2" --disp "3,3,2" [--pide "1:1,0,2"]
  python parcial.py deteccion --asig "..." --sol "..." --disp "..."
  python parcial.py pagina --pag 1024 --tabla "7,2,5,0,9,1" --dir "0x0C35,0x1400" [--proc 6144]
"""
import argparse, math, re, sys, unicodedata
from collections import Counter

# ---------------------------------------------------------------- BUSCADOR
STOP = set("""de la que el en y a los se del las un por con no una su para es al lo como mas
pero sus le ya o este si porque esta entre cuando muy sin sobre tambien me hasta hay donde quien
desde todo nos durante todos uno les ni contra otros ese eso ante ellos e esto mi antes algunos
que unos yo otro otras otra el tanto esa estos mucho quienes nada muchos cual poco ella estar
estas algunas algo nosotros""".split())

def norm(s):
    s = unicodedata.normalize("NFD", s.lower())
    return "".join(c for c in s if unicodedata.category(c) != "Mn")

def tokens(s):
    out = []
    for t in re.findall(r"[a-z0-9_]+", norm(s)):
        if t in STOP or len(t) < 2:
            continue
        out.append(t[:6] if len(t) > 6 and not t.startswith("0x") else t)  # raiz tosca
    return out

def cargar(path, ventana=14, paso=7):
    with open(path, encoding="utf-8", errors="ignore") as f:
        lineas = f.read().splitlines()
    chunks = []
    for i in range(0, max(1, len(lineas)), paso):
        trozo = lineas[i:i + ventana]
        if any(l.strip() for l in trozo):
            chunks.append((i + 1, trozo))
    return chunks

def indexar(chunks):
    docs = [Counter(tokens(" ".join(t))) for _, t in chunks]
    df = Counter()
    for d in docs:
        df.update(d.keys())
    avg = sum(sum(d.values()) for d in docs) / max(1, len(docs))
    return docs, df, avg

def buscar(chunks, idx, consulta, n=8, k1=1.4, b=0.75):
    docs, df, avg = idx
    q = tokens(consulta)
    N = len(docs)
    pts = []
    for i, d in enumerate(docs):
        ln = sum(d.values())
        s = 0.0
        for t in q:
            if t in d:
                idf = math.log(1 + (N - df[t] + .5) / (df[t] + .5))
                s += idf * d[t] * (k1 + 1) / (d[t] + k1 * (1 - b + b * ln / avg))
        if s > 0:
            pts.append((s, i))
    pts.sort(reverse=True)
    usados, res = [], []
    for s, i in pts:                       # evita resultados casi duplicados (ventanas solapadas)
        if any(abs(chunks[i][0] - u) < 10 for u in usados):
            continue
        usados.append(chunks[i][0]); res.append((s, i))
        if len(res) >= n:
            break
    return res

def cmd_buscar(a):
    chunks = cargar(a.archivo)
    idx = indexar(chunks)
    print(f"{len(chunks)} fragmentos indexados de {a.archivo}")
    def una(q):
        for s, i in buscar(chunks, idx, q, a.n):
            ini, tr = chunks[i]
            print(f"\n=== linea {ini} (puntaje {s:.1f}) ===")
            print("\n".join(tr)[:a.chars])
    if a.q:
        una(a.q); return
    while True:
        try:
            q = input("\npregunta (vacio = salir) > ").strip()
        except EOFError:
            break
        if not q:
            break
        una(q)

# ---------------------------------------------------------------- AJUSTE (memoria continua)
def entero(s): return int(s.strip(), 0)
def hx(v): return "0x%08X" % v

def cmd_ajuste(a):
    huecos0 = []
    for i, h in enumerate(a.huecos.split(",")):
        b, l = h.split("/"); huecos0.append([i, entero(b), entero(l)])
    reqs = [entero(r) for r in a.req.split(",")]
    for nombre in ("primer", "mejor", "peor"):
        hs = [h[:] for h in huecos0]
        print(f"\n##### {nombre.upper()} AJUSTE #####")
        for r in reqs:
            cand = [h for h in hs if h[2] >= r]
            if not cand:
                print(f"req {hx(r)}: NO CABE (espera). Libre total {hex(sum(h[2] for h in hs))}")
                continue
            if nombre == "primer": h = cand[0]
            elif nombre == "mejor": h = min(cand, key=lambda x: x[2])      # empate: primero
            else: h = max(cand, key=lambda x: x[2])
            print(f"req {hx(r)} -> hueco #{h[0]} (base proceso {hx(h[1])}, limite hueco {hex(h[2])})")
            h[1] += r; h[2] -= r
            hs = [x for x in hs if x[2] > 0]
        print("tabla final: " + " | ".join(f"{hx(h[1])}/{hex(h[2])}" for h in hs))

# ---------------------------------------------------------------- MATRICES
def mat(s): return [[int(x) for x in f.split(",")] for f in s.split(";")]
def vec(s): return [int(x) for x in s.split(",")]
def le(a, b): return all(x <= y for x, y in zip(a, b))
def add(a, b): return [x + y for x, y in zip(a, b)]
def sub(a, b): return [x - y for x, y in zip(a, b)]

def seguridad(disp, asig, nec):
    n = len(asig); fin = [False] * n; w = disp[:]; sec = []
    print(f"  Trabajo = {w}")
    while True:
        for i in range(n):
            if not fin[i] and le(nec[i], w):
                w = add(w, asig[i]); fin[i] = True; sec.append(i)
                print(f"  P{i} (necesita {nec[i]}) -> Trabajo = {w}")
                break
        else:
            break
    return all(fin), sec

def cmd_banquero(a):
    asig, mx = mat(a.asig), mat(a.max)
    if a.disp: disp = vec(a.disp)
    else:
        tot = vec(a.total); disp = tot[:]
        for f in asig: disp = sub(disp, f)
    if a.total and a.disp:
        calc = vec(a.total)
        for f in asig: calc = sub(calc, f)
        print("Disponible calculado desde total:", calc, "(el dado es", disp, ")", "OK" if calc == disp else "<-- NO COINCIDE")
    nec = [sub(m, x) for m, x in zip(mx, asig)]
    print("Necesidad:"); [print(f"  P{i}: {r}") for i, r in enumerate(nec)]
    ok, sec = seguridad(disp, asig, nec)
    print("SEGURO, secuencia:" if ok else "INSEGURO. Procesos que lograron terminar:", ["P%d" % i for i in sec])
    if a.pide:
        i, v = a.pide.split(":"); i = int(i); v = vec(v)
        print(f"\nP{i} solicita {v}")
        if not le(v, nec[i]): print("ERROR: excede su maximo"); return
        if not le(v, disp): print("No hay disponible: P%d espera" % i); return
        d2 = sub(disp, v); a2 = [r[:] for r in asig]; n2 = [r[:] for r in nec]
        a2[i] = add(a2[i], v); n2[i] = sub(n2[i], v)
        print(f"  Simulado: Disponible = {d2}")
        ok, sec = seguridad(d2, a2, n2)
        print("SEGURO -> SE CONCEDE" if ok else "INSEGURO -> NO SE CONCEDE")

def cmd_deteccion(a):
    asig, sol, w = mat(a.asig), mat(a.sol), vec(a.disp)
    n = len(asig); fin = [not any(r) for r in asig]
    print(f"Trabajo = {w}; Fin inicial = {fin}")
    prog = True
    while prog:
        prog = False
        for i in range(n):
            if not fin[i] and le(sol[i], w):
                w = add(w, asig[i]); fin[i] = True; prog = True
                print(f"  P{i} (pide {sol[i]}) termina -> Trabajo = {w}"); break
    bl = [f"P{i}" for i in range(n) if not fin[i]]
    print("BLOQUEADOS: " + ", ".join(bl) if bl else "NO hay bloqueo")

# ---------------------------------------------------------------- PAGINACION
def cmd_pagina(a):
    P = a.pag; tabla = vec(a.tabla)
    n = int(math.log2(P)); assert 2 ** n == P, "la pagina debe ser potencia de 2"
    print(f"Pagina {P} B -> {n} bits de desplazamiento" + (f", {a.bits - n} bits de pagina ({2**(a.bits-n)} entradas)" if a.bits else ""))
    lim = a.proc if a.proc else len(tabla) * P
    for d in a.dir.split(","):
        D = entero(d)
        p, off = D // P, D % P
        if D >= lim or p >= len(tabla):
            print(f"{hex(D)} ({D}): pagina {p}, desp {off} -> PAGINA INVALIDA / fuera del limite"); continue
        F = tabla[p] * P + off
        print(f"{hex(D)} ({D}): pagina {p}, desp {off:#x}, marco {tabla[p]} -> fisica {hex(F)} ({F})")

# ---------------------------------------------------------------- MAIN
if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="c", required=True)
    s = sp.add_parser("buscar"); s.add_argument("archivo"); s.add_argument("-q"); s.add_argument("-n", type=int, default=8); s.add_argument("--chars", type=int, default=1200); s.set_defaults(f=cmd_buscar)
    s = sp.add_parser("ajuste"); s.add_argument("--huecos", required=True); s.add_argument("--req", required=True); s.set_defaults(f=cmd_ajuste)
    s = sp.add_parser("banquero"); s.add_argument("--asig", required=True); s.add_argument("--max", required=True); s.add_argument("--disp"); s.add_argument("--total"); s.add_argument("--pide"); s.set_defaults(f=cmd_banquero)
    s = sp.add_parser("deteccion"); s.add_argument("--asig", required=True); s.add_argument("--sol", required=True); s.add_argument("--disp", required=True); s.set_defaults(f=cmd_deteccion)
    s = sp.add_parser("pagina"); s.add_argument("--pag", type=int, required=True); s.add_argument("--tabla", required=True); s.add_argument("--dir", required=True); s.add_argument("--bits", type=int); s.add_argument("--proc", type=int); s.set_defaults(f=cmd_pagina)
    a = ap.parse_args(); a.f(a)