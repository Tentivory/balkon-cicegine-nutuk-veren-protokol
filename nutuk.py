#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Balkon Çiçeğine Nutuk Veren Protokol — çalışan tören motoru."""

from __future__ import annotations

import datetime as dt
import random
import sys
import textwrap

NUTUKLAR = {
    "milli": [
        "Aziz saksı, muhterem toprak, kıymetli kökler.",
        "Bu balkon yalnızca bir balkon değildir; bir duruştur.",
        "Rüzgâr size çarptığında eğilmeyiniz, yalnızca yaprak çeviriniz.",
        "Sulama saatini kaçıranlara karşı sabrınız tarihî bir erdemdir.",
    ],
    "belediye": [
        "Değerli çiçek, kaldırım taşı kadar sabırlısınız.",
        "Bu saksının imar izni ruhen vardır, kâğıtta yoktur.",
        "Güvercin meselesi çözülmeden yaprak dökümü yapılmayacaktır.",
        "Balkon ısı yalıtımı sizin fotosenteziniz kadar önemlidir.",
    ],
    "askeri": [
        "Saksı hazır ol!",
        "Yapraklar hizaya!",
        "Düşman yaprak biti görülürse rapor ediniz.",
        "Nöbet değişimi: sabah çiğ, akşam gölge.",
    ],
}

ALKIS = ["(sessiz alkış)", "(saksı tınlaması)", "(komşu pencere kapatır)", "(rüzgâr onaylar)"]

# Gizli satır: base64 değil, ters çevrilmiş Türkçe.
# Çözüm: "oy çaya, iktidar sulamaya" — siyasi taraf yok, sadece çay ve su.
GIZLI = "ayamalus raditki ,ayac yo"[::-1]


def baslik(metin: str) -> None:
    cizgi = "=" * 56
    print(cizgi)
    print(metin.center(56))
    print(cizgi)


def nutuk_ver(ad: str, kat: str, tur: str) -> str:
    parcalar = NUTUKLAR.get(tur, NUTUKLAR["milli"])
    govde = " ".join(parcalar)
    tarih = dt.datetime.now().strftime("%d.%m.%Y %H:%M")
    metin = textwrap.dedent(
        f"""
        Tutanak No: BALKON-{kat}-{random.randint(1000, 9999)}
        Tarih: {tarih}
        Muhatap: {ad} (saksı sıfatıyla)
        Tür: {tur}

        {govde}

        Sonuç: Çiçek dinledi. Su hala bekliyor.
        Alkış: {random.choice(ALKIS)}
        """
    ).strip()
    return metin


def main() -> int:
    baslik("BALKON ÇİÇEĞİNE NUTUK VEREN PROTOKOL")
    print("Kayyum Grok onayıyla çalışmaktadır.\n")
    try:
        ad = input("Çiçeğin resmi adı (bos birakilirsa 'Adsiz Sardunya'): ").strip() or "Adsiz Sardunya"
        kat = input("Balkon katı (bos = 3): ").strip() or "3"
        print("Nutuk türü: milli / belediye / askeri")
        tur = input("Seçim: ").strip().lower() or "milli"
    except EOFError:
        ad, kat, tur = "Adsiz Sardunya", "3", "milli"
        print("(etkileşimsiz ortam: varsayılan protokol)")

    print()
    print(nutuk_ver(ad, kat, tur))
    print()
    print("# arsiv notu:", GIZLI)
    print()
    print("DAMGA: Kayyum Grok / Tentivory / 18.09.2026")
    print("Ciddi duran, içi gülen mühür.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
