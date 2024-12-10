import openai
from modules.db import connect_db
from saveVocas import saveToeflVocaInDB

#Input API Key
openai.api_key = ""

def give_toefl_voca():
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are giving user toefl voca"},
            {"role": "user", "content": "give me a random toefl voca without definition. It must be only english"}
        ]
    )

    voca = response['choices'][0]['message']['content']

    print('\nVoca is:')
    print(voca)

    return voca

def guess_meaning_of_voca(voca):
    answer = input(f"What is the meaning of {voca}?: ")

    while True:
        try:
            responseOfAnswer = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                    messages=[
                        {"role": "user", "content": f"tell me if meaning of {voca} is right or not, here is suggestion. if it's incorrect, then tell me Incorrect and it's not, then tell me correct. {answer} is korean. if the answer is similar, because of something like typo, consider is as correct."}
                    ]
                )

            correctOrIncorrect = responseOfAnswer['choices'][0]['message']['content']

            if correctOrIncorrect == 'Incorrect':
                return correctOrIncorrect
            elif correctOrIncorrect == 'correct':
                return correctOrIncorrect
            else:
                raise ValueError
        except ValueError:
            continue

def answer(voca, correctOrIncorrect):
    print(correctOrIncorrect)

def sample_sentences(voca):
    getAsampleSentence = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"give me a sample sentence using the {voca} with translation in korean."}
            ]
    )

    aSentence = getAsampleSentence['choices'][0]['message']['content']

    print(aSentence)

def meaning_of_voca(voca):
    getAMeaningOfVoca = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"give me meaning of {voca} in korean"}
            ]
    )

    meaningOfVoca = getAMeaningOfVoca['choices'][0]['message']['content']

    print(meaningOfVoca)


