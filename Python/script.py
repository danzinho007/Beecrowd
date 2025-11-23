import requests
import json
import time

BASE = "https://curso.dev/api/v1/show/questions/"
questions = {}

headers = {
    "Content-Type": "application/json"
}

def next_question(diff):
    r = requests.post(BASE + f"next/{diff}", headers=headers)
    try:
        return r.json()
    except:
        return None

def send_answer(qid, answer):
    body = {
        "question_id": qid,
        "answer": answer  # pode ser errado, só serve pra avançar
    }
    r = requests.post(BASE + "answer", json=body, headers=headers)
    try:
        return r.json()
    except:
        return None


print("\n📌 Coletando perguntas do Curso.dev...\n")
fails = 0

# Vamos rodar até o quiz ficar sem perguntas novas
while True:
    found = False
    for d in [1, 2, 3]:
        q = next_question(d)
        if not q or "question_id" not in q:
            fails += 1
            continue

        qid = q["question_id"]
        if qid not in questions:
            questions[qid] = q
            found = True
            print(f"✔️ Nova questão ({d}): {q['question']}")

        # responder qualquer alternativa pra liberar a próxima
        send_answer(qid, 1)

    if not found:
        fails += 1
        if fails >= 5:
            break

    time.sleep(0.6)

# salvar em JSON
with open("curso_dev_questions.json", "w", encoding="utf-8") as f:
    json.dump(list(questions.values()), f, ensure_ascii=False, indent=2)

print(f"\n🎉 Finalizado! {len(questions)} perguntas coletadas!")

# https://curso.dev/api/v1/show/questions/next/3