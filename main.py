import openai
from modules.db import connect_db

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

    responseOfAnswer = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"tell me if meaning of {voca} is right or not, here is suggestion. if it's incorrect, then tell me Incorrect and it's not, then tell me correct. {answer} is korean. if the answer is similar, because of something like typo, consider is as correct."}
        ]
    )

    correctOrIncorrect = responseOfAnswer['choices'][0]['message']['content'].lower()

    if correctOrIncorrect == 'incorrect':
        print(f"This is not the meaning of {voca}")
    elif correctOrIncorrect == 'correct':
        print("Good!")

    getAsampleSentence = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"give me korean meaning of {voca} and a sample sentence using the {voca} with korean meaning."}
            ]
    )

    printAsentence = getAsampleSentence['choices'][0]['message']['content']

    print(printAsentence)

    return 0


