import math
import matplotlib.pyplot as plt

def oklid_mesafesi(x1, y1, x2, y2):
    mesafe = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return mesafe

# Örnek kullanım
x1, y1 = 1, 2
x2, y2 = 4, 6

mesafe = oklid_mesafesi(x1, y1, x2, y2)
print(f"({x1}, {y1}) ve ({x2}, {y2}) noktaları arasındaki Öklid mesafesi: {mesafe}")

# Görselleştirme
plt.figure()
plt.plot([x1, x2], [y1, y2], 'bo-', label=f"Mesafe: {mesafe:.2f}")
plt.text((x1 + x2) / 2, (y1 + y2) / 2, f'{mesafe:.2f}', fontsize=12, ha='center')
plt.scatter([x1, x2], [y1, y2], color='red')
plt.annotate(f"({x1}, {y1})", (x1, y1), textcoords="offset points", xytext=(5,-10), ha='center')
plt.annotate(f"({x2}, {y2})", (x2, y2), textcoords="offset points", xytext=(5,-10), ha='center')
plt.title("Öklid Mesafesi Görselleştirme")
plt.xlabel("X Ekseni")
plt.ylabel("Y Ekseni")
plt.grid(True)
plt.legend()

# Grafiğin ekranda kalma süresini 10 saniye
plt.pause(10)
plt.close()  # Grafiği kapatır
