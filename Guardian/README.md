# Guardian

**Флаг:** `kpi2026{d0tn3t_1l_fl4tt3n1ng_p3rmut4t10ns}`

## Що це за файл

Це не нативний x64-бінарник, а **.NET-збірка** — керований код, що
компілюється у проміжну мову IL, а не напряму в машинний код
процесора. Команда `file` показує це як `Mono/.Net assembly`.

## Чим відкривати

Ghidra тут не підходить. Варіанти на Linux:
- `ilspycmd` (ставиться як `dotnet tool`)
- `monodis` (виводить IL-лістинг)
- Python-бібліотеки `dnfile` + `dncil`

## Логіка перевірки

Check(flag):
якщо довжина flag != 42 → Wrong
T = Dec(TE) # Dec(): кожен байт XOR 110
K = Dec(KE)
S = BuildSbox(0xC0FFEE) # перемішана таблиця 0..255
для i від 0 до 41:
якщо S[(flag[i] + i) & 255] ^ K[i % 8] != T[i] → Wrong
→ Correct
