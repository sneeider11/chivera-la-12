"""Genera una página por modelo de campero (SEO: una página por búsqueda).
Uso: python _generar_modelos.py   (desde la carpeta web/). Re-ejecutable: sobrescribe las páginas."""
import json
from pathlib import Path

BASE = "https://sneeider11.github.io/chivera-la-12/"  # cambiar_dominio.py lo reemplaza
WA = "https://wa.me/573156417309?text="

MODELOS = [
    {
        "slug": "repuestos-toyota-land-cruiser",
        "nombre": "Toyota Land Cruiser",
        "titulo": "Repuestos usados Toyota Land Cruiser FJ40, BJ40 y serie 70 en Bucaramanga",
        "h1": "Repuestos usados para Toyota Land Cruiser",
        "versiones": "FJ40, BJ40, FJ43, FJ45, FJ55, FJ62, serie 70 (LJ70)",
        "motores": "Motor 2F, 3F y diésel serie B",
        "piezas": ["Motor 2F y 3F completo o por partes", "Carburador, arranque, alternador y distribuidor 2F",
                   "Caja de cambios de 4 velocidades y transferencia", "Cardanes, diferenciales y puntas de eje",
                   "Puertas, capó, guardabarros, techo y tablero FJ40", "Muelles, amortiguadores y frenos"],
    },
    {
        "slug": "repuestos-chevrolet-samurai",
        "nombre": "Chevrolet Samurai / Suzuki Samurai",
        "titulo": "Repuestos usados Chevrolet Samurai y Suzuki Samurai SJ410, SJ413 | Bucaramanga",
        "h1": "Repuestos usados para Chevrolet Samurai y Suzuki Samurai",
        "versiones": "Chevrolet Samurai, Suzuki Samurai, SJ410, SJ413",
        "motores": "Motores originales del Samurai",
        "piezas": ["Caja de cambios de 5 velocidades", "Caja transfer y caja reductora", "Motor completo o por partes",
                   "Cardanes y diferenciales", "Capó, puertas, guardabarros y carrocería", "Caja de dirección y suspensión"],
    },
    {
        "slug": "repuestos-nissan-patrol",
        "nombre": "Nissan Patrol",
        "titulo": "Repuestos usados Nissan Patrol modelo viejo Y60, 260, RD28 | Bucaramanga",
        "h1": "Repuestos usados para Nissan Patrol modelo viejo",
        "versiones": "Patrol Y60, Patrol 260, Patrol GR, 6 cilindros",
        "motores": "Motores RD28, SD33 y 6 cilindros gasolina",
        "piezas": ["Motor RD28, SD33 o 6 cilindros", "Caja de cambios y transferencia", "Cardanes y diferenciales",
                   "Carrocería: puertas, capó, guardabarros", "Suspensión y frenos", "Partes eléctricas"],
    },
    {
        "slug": "repuestos-jeep-willys",
        "nombre": "Jeep Willys",
        "titulo": "Repuestos usados Jeep Willys en Bucaramanga | Envíos a toda Colombia",
        "h1": "Repuestos usados para Jeep Willys",
        "versiones": "Jeep Willys y derivados",
        "motores": "Motores originales Willys",
        "piezas": ["Motor completo o por partes", "Caja de 3 velocidades y transferencia", "Cardanes y diferenciales",
                   "Carrocería y latonería", "Suspensión y frenos", "Partes eléctricas"],
    },
    {
        "slug": "repuestos-chevrolet-luv",
        "nombre": "Chevrolet LUV",
        "titulo": "Repuestos usados Chevrolet LUV 1600, 2300 y 2.2 | Bucaramanga",
        "h1": "Repuestos usados para Chevrolet LUV 1600 y 2300",
        "versiones": "LUV 1600, LUV 2300, LUV 2.2, LUV 2.3",
        "motores": "Motores 1600, 2300 y 2.2",
        "piezas": ["Motor completo o por partes", "Caja de cambios", "Tablero y partes de cabina",
                   "Carrocería y platón", "Suspensión y frenos", "Partes eléctricas"],
    },
    {
        "slug": "repuestos-montero-daihatsu-mazda",
        "nombre": "Mitsubishi Montero, Daihatsu y Mazda",
        "titulo": "Repuestos usados Mitsubishi Montero, Daihatsu Rocky, F20, Terios y Mazda | Bucaramanga",
        "h1": "Repuestos usados para Mitsubishi Montero, Daihatsu y Mazda",
        "versiones": "Mitsubishi Montero · Daihatsu Rocky, F20, Terios · camperos y camionetas Mazda antiguas",
        "motores": "Motores de Montero, Daihatsu y Mazda",
        "piezas": ["Motores completos o por partes", "Cajas de cambios y transferencias", "Cardanes y diferenciales",
                   "Carrocería y latonería", "Suspensión y frenos", "Partes eléctricas"],
    },
]

PLANTILLA = """<!doctype html>
<html lang="es-CO">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titulo}</title>
<meta name="description" content="Chivera la 12: repuestos usados originales para {nombre} ({versiones}). {motores}. Precios de $100.000 a $2.000.000. Envíos a toda Colombia desde Bucaramanga.">
<link rel="canonical" href="{base}{slug}.html">
<link rel="stylesheet" href="estilos.css">
<script type="application/ld+json">{jsonld}</script>
</head>
<body>
<header class="top">
  <div class="wrap">
    <p class="marca"><a href="./">CHIVERA LA 12</a></p>
    <h1>{h1}</h1>
    <p class="sub">Piezas originales usadas · {versiones}. Enviamos a toda Colombia.</p>
    <div class="ctas">
      <a class="btn wa" href="{wa}{wa_txt}" rel="nofollow">Cotizar por WhatsApp</a>
      <a class="btn sec" href="tel:+573156453597">Llamar 315 645 3597</a>
    </div>
  </div>
</header>
<main class="wrap">
  <section>
    <h2>Qué tenemos para {nombre}</h2>
    <ul class="modelos">
{piezas}
    </ul>
    <p><strong>{motores}.</strong> Precios de piezas usadas de <strong>$100.000 a $2.000.000</strong> según la pieza y su estado. Motores completos: cotiza por WhatsApp.</p>
  </section>
  <section class="pasos">
    <h2>Cómo comprar</h2>
    <ol>
      <li>Escríbenos por WhatsApp con la foto de la pieza o de la tarjeta de propiedad.</li>
      <li>Te cotizamos y te mandamos foto o video de la pieza real antes de pagar.</li>
      <li>Despachamos por transportadora a cualquier ciudad de Colombia.</li>
    </ol>
  </section>
  <section>
    <h2>¿Tienes un {nombre} viejo, chocado o varado?</h2>
    <p>Te lo compramos en el estado que esté. <a href="vende-tu-campero.html">Mira cómo vender tu campero</a>.</p>
    <p><a class="btn sec" href="./">Ver todos los camperos que manejamos</a></p>
  </section>
</main>
<footer class="pie">
  <div class="wrap">Chivera la 12 · Cl. 26 #11-74, Bucaramanga · Cel 315 645 3597 · WhatsApp 315 641 7309</div>
</footer>
<a class="flotante" href="{wa}{wa_txt}" aria-label="Escribir por WhatsApp" rel="nofollow">WhatsApp</a>
</body>
</html>
"""


def main():
    aqui = Path(__file__).parent
    for m in MODELOS:
        jsonld = json.dumps({
            "@context": "https://schema.org", "@type": "WebPage", "name": m["h1"],
            "url": f"{BASE}{m['slug']}.html",
            "about": {"@type": "AutoPartsStore", "name": "Chivera la 12", "telephone": "+573156453597",
                      "address": {"@type": "PostalAddress", "streetAddress": "Cl. 26 #11-74",
                                  "addressLocality": "Bucaramanga", "addressRegion": "Santander", "addressCountry": "CO"}},
        }, ensure_ascii=False)
        wa_txt = f"Hola%2C%20vengo%20de%20la%20p%C3%A1gina%20web.%20Busco%20un%20repuesto%20para%20{m['nombre'].split(' /')[0].replace(' ', '%20')}%3A%20"
        piezas = "\n".join(f"      <li>{p}</li>" for p in m["piezas"])
        datos = {**m, "piezas": piezas}
        html = PLANTILLA.format(base=BASE, wa=WA, wa_txt=wa_txt, jsonld=jsonld, **datos)
        (aqui / f"{m['slug']}.html").write_text(html, encoding="utf-8")
    print(len(MODELOS), "paginas de modelo")


if __name__ == "__main__":
    main()
