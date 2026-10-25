"""Cambia la dirección base del sitio en todos los archivos y crea el archivo CNAME.
Uso (desde web/): python _cambiar_dominio.py chiverala12.com
Después: git add -A && git commit && git push; luego configurar DNS y el dominio en GitHub Pages."""
import sys
from pathlib import Path

VIEJA = "https://sneeider11.github.io/chivera-la-12/"


def main():
    dominio = sys.argv[1].strip().lower().removeprefix("https://").removeprefix("www.").strip("/")
    nueva = f"https://{dominio}/"
    aqui = Path(__file__).parent
    cambiados = 0
    for f in list(aqui.glob("*.html")) + list(aqui.glob("*.xml")) + list(aqui.glob("*.txt")) + [aqui / "_generar_modelos.py"]:
        if f.name.startswith("google"):
            continue
        t = f.read_text(encoding="utf-8")
        if VIEJA in t:
            f.write_text(t.replace(VIEJA, nueva), encoding="utf-8")
            cambiados += 1
    (aqui / "CNAME").write_text(dominio + "\n", encoding="ascii")
    print(f"{cambiados} archivos actualizados a {nueva}; CNAME = {dominio}")


if __name__ == "__main__":
    main()
