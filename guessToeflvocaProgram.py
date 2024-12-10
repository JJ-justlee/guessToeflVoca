from chatgptToeflVoca import give_toefl_voca, guess_meaning_of_voca, sample_sentences, answer, meaning_of_voca
from saveVocas import saveToeflVocaInDB

#from saveVocas import saveToeflVocaInDB
#from signupAndLogin import doLoginSignup

if __name__ == "__main__":
    #doLoginSignup()
    while True:
        voca = give_toefl_voca()
        correctOrIncorrect = guess_meaning_of_voca(voca)
        is_correct = answer(voca, correctOrIncorrect)
        meaning = meaning_of_voca(voca)
        ex_sample = sample_sentences(voca)
        saveToeflVocaInDB(voca, meaning, ex_sample, is_correct)






