#!/usr/bin/env python3
import subprocess
import sys
import os

os.chdir(r"C:\TIR_TESTE")

# Run pytest with verbose output
result = subprocess.run(
    [sys.executable, "-m", "pytest", "tests/test_PXGPEM04.py", "-v", "--tb=short"],
    capture_output=True,
    text=True,
    timeout=400
)

# Write to file
with open("run_test_result.txt", "w") as f:
    f.write("=== STDOUT ===\n")
    f.write(result.stdout)
    f.write("\n\n=== STDERR ===\n")
    f.write(result.stderr)
    f.write(f"\n\n=== RETURN CODE: {result.returncode} ===\n")

print("Teste executado. Resultado salvo em run_test_result.txt")
print(f"Return code: {result.returncode}")
