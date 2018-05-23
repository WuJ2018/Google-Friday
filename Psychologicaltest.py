import time

print   "Psychological test"
print   "Note: only choose one answer for each question, you should answer first impression, the corresponding scores are added together is the answer to your score."


print   "start testing:"

#Since the calculation of the total value of
your_sum = 0

# All issues of the store through the key
question1 = { "question": " 1, Which kind of fruit you prefer to eat?", "answer": [ "A, strawberry", "B, apple", "C, watermelon", "D, pineapple", " E, orange "]}
question2 = { "question": " 2, Where do you usually go for leisure?", "answer": [ "A, outskirts", "B, movie theater", "C, park", "D, shopping market", " E, bar ", " F, karaoke"]}
question3 = { "question": " 3, What kind of people do you think will easily attracted you?", "answer": [ "A, talented person", "B, person who rely on you", "C, elegant person "," D, kind person "," E, bold person "]}
question4 = { "question": " 4, if you are going to be an animal, what do you want to be?", "answer": [ "A, cat", "B, horse", "C, elephant" , "D, monkey", "E, dog", "F, lion "]}
question5 = { "question": " 5, the weather was very hot, what way you prefer to cool down?", "answer": [ "A, swimming", "B, a cold drink", "C, air conditioning "] }
question6 = { "question": " 6, if you must live with the animal or insect that you don't like, which you can tolerate?", "answer": [ "A, snake", "B, pig", " C, mice "," D, fly "]}
question7 = { "question": " 7, what kind of movies, TV series do you like?", "answer": [ "A, suspense reasoning class", "B, fairy mythology class", "C, natural sciences" "D, ethics class", "E, war gunfight"]}
question8 = { "question": " 8, which of the following item you will always have it on you?", "answer": [ "A, lighters", "B, lipstick", "C, Notepad", "D, tissue "," E, mobile phone "]}
question9 = { "question": " 9, which transport you prefer to have when you travel?", "answer": [ "A, train", "B, bikes", "C, car", "D, aircraft", "E, walk"]}
question10 = { "question": " 10, Which of the following colors do you like?", "answer": [ "A, Purple", "B, black", "C, blue", "D, White," " E, yellow "," F, red "]}
question11 = { "question": " 11, which of the following campaign is your favorite (don't need to be necessarily good at)?", "answer": [ "A, yoga", "B, bikes", "C, Table Tennis" , "D, boxing", "E, soccer", "F, bungee jumping"]}
question12 = { "question": " 12, if you own a villa, where do you think it should be built?", "answer": [ "A, lake", "B, grassland", "C, the sea," "D, forest", "E, in city"]}
question13 = { "question": " 13, which of the following weather you like the most?", "answer": [ "A, Snow", "B, Wind", "C, Rain", "D, fog," "E, flash"]}
question14 = { "question": " 14, where floor do you want your house be in a 30-story building?", "answer": [ "A, seventh", "B, first", "C, twenty third "," D, eighteenth "," E, thirtyth "]}
question15 = { "question": " 15, which of the following cities you think you prefer to live in?", "answer": [ "A, Lijiang", "B, Lhasa", "C, Kunming", "D Xi'an "," E, Hangzhou "," F, Beijing "]}


# All the answers, through key-value pairs exist
scoring1 = { "A": 2 , "B": 3, "C": 5, "D": 10, "E": 15}
scoring2 = { "A": 2 , "B": 3, "C": 5, "D": 10, "E": 15, "F": 20}
scoring3 = { "A": 5 , "B": 10, "C": 15}
scoring4 = { "A": 2 , "B": 5, "C": 10, "D": 15}
scoring5 = { "A": 2 , "B": 2, "C": 3, "D": 5, "E": 10}
scoring6 = { "A": 2 , "B": 3, "C": 5, "D": 8, "E": 12, "F": 15}
scoring7 = { "A": 2 , "B": 3, "C": 5, "D": 8, "E": 10, "F": 15}
scoring8 = { "A": 1 , "B": 3, "C": 5, "D": 8, "E": 10, "F": 15}

#All character
personality1 = "strong-willed, cool-headed, with a strong desire for leadership, strong dedication, and unwillingness not to stop working. \ nGood looks, good self-esteem, more emphasis on personal relationships, \nsometimes Being anxious, aggressive, and unreasonable, is not conducive to self-resistance and resistance. It is not easy to admit defeat. \ nThinking rationally, the view of love and marriage is very realistic, and the desire for money is generally."
personality2 = "Smart, lively, good-natured, good at making friends, and has a deeper understanding. \ n Strong career, longing success. Reasonable thinking, advocating love, \ nbut when love and marriage conflict, they will choose to benefit their own marriage. The desire for money is strong."
personality3 = "Love fantasy, thinking is more emotional, and choose friends based on whether or not you are guilty. \n Personality is more aloof, sometimes more annoying, and sometimes indecisive.\n Stronger in business, like creative work, not Likes to follow the routine. \ nThe character is stubborn, the speech is sharp, and he is not good at compromise. \ n Advocating romantic love, but the idea is often unrealistic. \ nMoney desire is generally."
personality4 = "strong curiosity, adventure, good karma. \ nProfessional, treat the work, keep happy, and be good at compromise. \ nChoice to find interesting things, but patience is poor, risk taking, but sometimes timid. \ N Longing for romantic love, but the requirements for marriage are more realistic. \ nNot good at money."
personality5 = "Warm temperament, friendship, and personality, but sometimes it is awkward. \ nYou have a serious career. You can take your job seriously, but you don't have much interest in things other than yourself, \n like regular work. And life, do not like adventure, family concept strong, relatively good at financial management. "
personality6 = "Slosh, playful, full of fantasy. \ nSmart, smart, warm, love friends, but there are no strict selection criteria for friends. \ nProfessionals are poor, they are better at enjoying life, willpower and patience. Poor, go it alone. \ nThere is good heterosexuality, but love is not enough to insist on serious, easy compromise. \ nNo property concept. "

def show_question_answer (question, scoring):
    """This method of all issues in order to display and use all the answers."""
    print question.get ( "question")
    l=question["answer"]
    for allans in l:
        print allans
    yourans=raw_input("> ")
    score=scoring.get(yourans.upper())
    if score==None:
        print "The answer you entered does not exist. Please check the question again:"
        show_question_answer(question,scoring)
        return
    global your_sum
    your_sum+=score

show_question_answer(question1,scoring1)
show_question_answer(question2,scoring2)
show_question_answer(question3,scoring1)
show_question_answer(question4,scoring2)
show_question_answer(question5,scoring3)
show_question_answer(question6,scoring4)
show_question_answer(question7,scoring1)
show_question_answer(question8,scoring5)
show_question_answer(question9,scoring1)
show_question_answer(question10,scoring6)
show_question_answer(question11,scoring7)
show_question_answer(question12,scoring1)
show_question_answer(question13,scoring1)
show_question_answer(question14,scoring1)
show_question_answer(question15,scoring8)

print "Your total score is:%d" %your_sum
print "Disclosed answer:\n"

if your_sum>=180:
    print personality1
elif your_sum>=140 and your_sum<180:
    print personality2
elif your_sum>=100 and your_sum<140:
    print personality3
elif your_sum>=70 and your_sum<100:
    print personality4
elif your_sum>=40 and your_sum<70:
    print personality5
elif your_sum<40:
    print personality6
else:
    print "An exception occurred in the program that caused the calculation result to be displayed incorrectly"

time.sleep(30)
