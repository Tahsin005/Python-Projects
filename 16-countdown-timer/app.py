import time

print("=== 🕒 COUNTDOWN TIMER 🕒 ===")
print("💫 Count down from your chosen seconds!")

isPlaying = True

while isPlaying:
    try:
        seconds = int(input("Enter the number of seconds: "))
    except:
        print("❌ Invalid input. Please enter a valid number.")
        continue




    for i in range(seconds, 0, -1):
        print(f'⏳ {i} seconds remaining...')
        time.sleep(1)

    print("🎉 Countdown completed! 👏")
    playing = input("⏳ Do you want to start another countdown? (y/n): ").strip().lower()
    if playing.startswith("n"):
        print("Goodbye! 👋")
        break