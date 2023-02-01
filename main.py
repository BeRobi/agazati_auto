import bevezetes
import autom
import sorozat

bevezetes.beker()
sorozat.vel_szamok()
autom.beolvas()

print(f"\nIII/B: Flotta: \n\tAutók száma: {autom.flotta()}.")

print(f"\nIII/C: Legfiatalabb:\n\tA legfiatalabb autó: {autom.legfiatalabb()}")

print(f"\nIII/D: Legöregebb:\n\tA legöregebb autó: {autom.legoregebb()}")
