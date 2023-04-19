import sys

mountain = {
   "name": sys.argv[1],
   "high": {
      "m":  int(sys.argv[2]),
      "ft": int(sys.argv[3])
   }
}

m_template = "{m[name]} - {m[high][m]} м ({m[high][ft]} ф)"
print(m_template.format(m=mountain))
