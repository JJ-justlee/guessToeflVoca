import openai

#Input API Key
openai.api_key = "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"

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

def give_meaning_of_voca(voca):
    answer = input(f"What is the meaning of this {voca}?: ")

    responseOfAnswer = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"tell me if meaning of {voca} is {answer}. if correct, tell me correct. but if incorrect, tell me incorrect"}
        ]
    )

    correctOrIncorrect = responseOfAnswer['choices'][0]['message']['content']
    correctOrIncorrect = correctOrIncorrect.strip()

    if correctOrIncorrect == 'incorrect':
        print(f"This is not the meaning of {voca}")
    elif correctOrIncorrect == 'correct':
        print("congratulation!")
    else:
        print("ss")

    return 0

if __name__ == "__main__":
    voca = give_toefl_voca()
    give_meaning_of_voca(voca)


