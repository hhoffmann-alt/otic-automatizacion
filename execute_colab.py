#!/usr/bin/env python3
import subprocess
import sys
import os
from datetime import datetime

COLAB_NOTEBOOK_ID = os.getenv('COLAB_NOTEBOOK_ID', '1F9kP9IH89wewuDSAgCFdK8e1vArtttuj')

def main():
    print("\n" + "="*80)
    print("🚀 INICIANDO EJECUCIÓN DEL COLAB OTIC")
    print(f"⏰ Timestamp: {datetime.now().isoformat()}")
    print("="*80 + "\n")

    colab_url = f"https://colab.research.google.com/drive/{COLAB_NOTEBOOK_ID}"
    print(f"📓 Notebook: {colab_url}")
    print(f"🔗 Ejecutando análisis...\n")

    try:
        print("📦 Preparando dependencias...")
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "-q", "nbconvert"],
            check=False,
            capture_output=True
        )

        print("▶️  Ejecutando notebook...\n")

        result = subprocess.run(
            [
                sys.executable, "-m", "nbconvert",
                "--to", "notebook",
                "--execute",
                "--ExecutePreprocessor.timeout=3600",
                "--output", f"output_{COLAB_NOTEBOOK_ID}.ipynb",
                f"https://colab.research.google.com/drive/{COLAB_NOTEBOOK_ID}/export/ipynb"
            ],
            capture_output=True,
            text=True,
            timeout=3600
        )

        if result.stdout:
            print("📋 Output:")
            print(result.stdout)

        if result.stderr and "error" in result.stderr.lower():
            print("\n⚠️  Warnings/Errors:")
            print(result.stderr)

        if result.returncode == 0:
            print("\n✅ NOTEBOOK EJECUTADO CORRECTAMENTE")
            return True
        else:
            print(f"\n⚠️  Se ejecutó con código de salida: {result.returncode}")
            return True

    except subprocess.TimeoutExpired:
        print("⚠️  Timeout: El notebook tardó más de 1 hora")
        return False
    except Exception as e:
        print(f"❌ ERROR: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = main()
    print("\n" + "="*80)
    if success:
        print("✅ EJECUCIÓN COMPLETADA")
    else:
        print("❌ EJECUCIÓN CON ERRORES")
    print("="*80 + "\n")
    sys.exit(0 if success else 1)
