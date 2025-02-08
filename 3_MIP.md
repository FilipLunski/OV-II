# Úloha 3: Mixed integer programming

## Problém:

Firma XYZ vyrábí dva produkty, A a B, s využitím jediného stroje. Náklady na výrobu každého
produktu zahrnují jednorázové náklady na nastavní výroby a nákldy na každý kus vyrobeného
produktu. Pro produkt A jsou jednorázové náklady 1,000 CZK a kusové náklady 20 CZK. Pro
produkt B jsou jednorázové náklady 2,000 CZK a kusové náklady 25 CZK. Výroba produktu A trvá
2 hodiny, výroba produktu B 3 hodiny. Stroj může pracovat maximálně 200 hodin. Z provozních
důvodů se výroba (potenciálně) zahájí jen pokud bude poptávka po A větší než 30 kusů a poptávka
po B větší nez 40 kusů.

## Analýza problému:

Už ze zadání je zřejmé, že se jedná o problém, který lze řešit pomocí lineárního programování. I když problém obsahuje fixní náklady, pro které by bylo vhodné použít binární proměnné a smíšené celočíselné programování, postrádá problém další podmínky, které by vyžadovaly použití celočíselných proměnných. Proto budeme předpokládat, že budou vyráběny oba produkty, a s ohledem na ostatní podmínky budeme hledat optimální řešení pomocí lineárního programování.

Pokud bychom problém řešili jako MIP, zvolili bychom další rozhodovací binární proměnné, které by určovaly, zda se bude vyrábět daný produkt. Pomocí metody branch and bound bychom pak hledali optimální řešení.

## Formulace problému:

### Definice rozhodovacích proměnných:
- *x1* – počet vyrobených jednotek produktu A
- *x2* – počet vyrobených jednotek produktu B

### Cílová funkce:
- Minimalizovat Z = 1000 + 20*x1* + 2000 + 25*x2*

### Omezení:

#### Kapacita stroje
- 2*x1* + 3*x2* ≤ 200
#### Minimální poptávka
- *x1* ≥ 31
- *x2* ≥ 41

## Řešení úlohy:

- Minimální hodnoty *x1* = 31 a *x2* = 41  splňují časové omezení.
- Zvýšení produkce nad tyto hodnoty by vedlo k vyšším nákladům, proto je optimální vyrábět přesně minimální požadovaná množství.

## Výsledek:
- optimální řešení: 
    - *x1* = 31
    - *x2* = 41
- Celkové náklady:
    - 1000 + 20*31 + 2000 + 25*41 = 1000 + 620 + 2000 + 1025 = <ins>4645 CZK</ins>

