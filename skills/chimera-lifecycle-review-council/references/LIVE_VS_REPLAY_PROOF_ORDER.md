# Live Vs Replay Proof Order

Use this order:

1. reasoning review
2. live artifact inspection
3. deterministic contract checks
4. replay for first divergence
5. learning capture

Do not let replay overwrite live truth.
Use replay to isolate the fault faster, not to pretend the live path is already healthy.
