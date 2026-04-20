from deepface import DeepFace
import os


def analyze_face(image_path):
    """
    Rasm faylini tahlil qiladi va natijani qaytaradi.
    """
    if not os.path.exists(image_path):
        print(f"Xato: {image_path} fayli topilmadi!")
        return

    print(f"Tahlil qilinmoqda: {image_path}...")

    try:
        # Serverda tez ishlashi uchun detector_backend='opencv' (yoki 'retinaface' aniqroq lekin sekinroq)
        results = DeepFace.analyze(
            img_path=image_path,
            actions=["emotion", "age", "gender"],
            enforce_detection=True,
            detector_backend="opencv",
        )

        for i, face in enumerate(results):
            print(f"\n--- {i + 1}-yuz natijalari ---")
            print(f"Yosh: {face['age']}")
            print(f"Jins: {face['dominant_gender']}")
            print(f"Asosiy emotsiya: {face['dominant_emotion']}")

            # Siz yozgan mantiq bo'yicha anti-spoofing tekshiruvi
            neutral_score = face["emotion"]["neutral"]
            if neutral_score > 80:
                print("Status: EHTIYOT: Shubhali (Neutral juda yuqori)")
            else:
                print("Status: Haqiqiy ko'rinishda")

    except ValueError as e:
        print("Xato: Rasmda yuz aniqlanmadi.")
    except Exception as e:
        print(f"Kutilmagan xato: {e}")


# Test qilish uchun rasm yo'lini yozing
if __name__ == "__main__":
    # Serveringizdagi biror rasm fayli yo'li
    test_image = "image.png"
    analyze_face(test_image)
