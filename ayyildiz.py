import turtle

t = turtle.Turtle()
w = turtle.Screen()
w.title("ŞANLI SANCAK")         # Başlık
w.setup(width=720,height=420)   # Pencere Boyutu
w.bgcolor("pink")                # Arka Plan Kırmızı Yap

# İlk daire
t.up()
t.goto(-100,-100)               # Fare imleci lokasyonu
t.color('black')                # Beyaz renk
t.begin_fill()                  # Beyaz rengi doldur
t.circle(120)                   # Çapı
t.end_fill()

# Hilal yapabilmek için ikinci daire
t.goto(-70,-80)                 # Fare imleci lokasyonu
t.color('pink')                  # Kırmızı renk
t.begin_fill()                  # Kırmızı rengi doldur
t.circle(100)                   # Çapı
t.end_fill()                    # Dolguyu Bitir

# Yıldız için hazırlık
t.goto(0,35)
t.fillcolor("black")
t.begin_fill()

# Yıldız için tekrar eden üçgen çizimi
for i in range(5):
    t.forward(150)
    t.right(144)
t.end_fill()

t.goto(-130,-190)
t.color("black")
t.write("@yazilimfuryasi", font=("Verdana", 17,"bold"))

# Fare imleci ekranda durup görüntüyü bozmasın diye uzaklaştırıyoruz :)
t.goto(-999,-0)

# Ekrana tıklayınca programın kapanmasını sağlar.
w.exitonclick()
