# Scam-Guard-GH - Ghana Fraud Detector 🇬🇭
def is_scam(message):
    message = message.lower()
    keywords = ["you have won","lotto","send momo","send money","account blocked","verify pin","share pin","claim prize","urgent","momo pin","click link"]
    score = 0
    found = []
    for w in keywords:
        if w in message:
            score += 1
            found.append(w)
    if "momo" in message and ("pin" in message or "send" in message):
        score += 2
    return score >= 2, score, found

print("🇬🇭 Scam-Guard-GH running!")
while True:
    msg = input("Paste message (or exit): ")
    if msg.lower() == "exit": break
    scam, score, found = is_scam(msg)
    if scam:
        print(f"🚨 SCAM! Score {score} - Found: {found}")
        print("DO NOT SEND MONEY!\n")
    else:
        print(f"✅ SAFE Score {score}\n")