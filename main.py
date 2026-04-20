import os
from deepface import DeepFace


def analyze_face(image_path):
    """
    Rasm faylini tahlil qiladi va natijani qaytaradi.
    """
    if not os.path.exists(image_path):
        print(f"Xato: {image_path} fayli topilmadi!")
        return

    print(f"Tahlil qilinmoqda: {image_path}...")

    try:
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

            neutral_score = face["emotion"]["neutral"]
            if neutral_score > 80:
                print("Status: EHTIYOT: Shubhali (Neutral juda yuqori)")
            else:
                print("Status: Haqiqiy ko'rinishda")

    except ValueError as e:
        print(e)
        print("Xato: Rasmda yuz aniqlanmadi.")
    except Exception as e:
        print(e)
        print(f"Kutilmagan xato: {e}")


def verify_faces(img1_path, img2_path):
    try:
        result = DeepFace.verify(
            img1_path=img1_path,
            img2_path=img2_path,
            model_name="VGG-Face",
            detector_backend="opencv",
            distance_metric="cosine",
        )

        is_same = result["verified"]
        distance = result["distance"]
        threshold = result["threshold"]

        print(
            f"Solishtirish natijasi: {'Bitta odam' if is_same else 'Har xil odamlar'}"
        )
        print(f"O'xshashlik masofasi: {distance:.4f}")
        print(f"Chegara (Threshold): {threshold}")

        return result

    except Exception as e:
        print(f"Xato yuz berdi: {e}")
        return None


if __name__ == "__main__":
    test_image = "image.png"
    test_image2 = "image2.png"
    analyze_face(test_image)
    verify_faces(img1_path=test_image, img2_path=test_image2)
