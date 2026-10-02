Флаг:kpi2026{d0tn3t_1l_fl4tt3n1ng_p3rmut4t10ns}


Це не нативний x64, а .NET-збірка (керований код, компілюється у проміжну мову IL, а не напряму в машинний код процесора). file показує це як Mono.Net assembly

На Linux ilspycmd (ставиться як dotnet tool), або monodis (IL-лістинг), або Python-бібліотеки dnfile + dncil.

Check(flag):
  якщо довжина flag != 42 → Wrong
  T = Dec(TE)              # Dec() кожен байт XOR 110
  K = Dec(KE)
  S = BuildSbox(0xC0FFEE)  # перемішана таблиця 0..255
  для i від 0 до 41:
      якщо S[(flag[i] + i) & 255] ^ K[i % 8] != T[i] → Wrong
  → Correct
