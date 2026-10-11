from pathlib import Path
import hashlib,json
P=Path(__file__).resolve().parent;R=P/'candidate';B=P.parent/'release-source'
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def manifest(r):return {str(f.relative_to(r)):digest(f) for f in sorted(r.rglob('*')) if f.is_file()}
baseline=json.loads((P/'baseline-manifest.json').read_text())
if manifest(B)!=baseline:raise SystemExit('STOP: production source changed since baseline snapshot. Reconcile newer files before sealing.')
a=manifest(R);(P/'candidate-manifest.json').write_text(json.dumps(a,indent=2))
(P/'release-diff.json').write_text(json.dumps({'changed':[k for k in baseline if k in a and a[k]!=baseline[k]],'added':[k for k in a if k not in baseline],'deleted':[k for k in baseline if k not in a]},indent=2))
routes=json.loads((P/'route-manifest.json').read_text())
for m in routes:m['sha256']=digest(R/m['file'])
(P/'route-manifest.json').write_text(json.dumps(routes,indent=2))
print('Sealed local manifest. Production-source baseline unchanged. No upload authorized.')
