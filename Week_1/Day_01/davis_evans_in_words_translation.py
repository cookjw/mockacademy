def in_words(number):
    
    def convert_triple(triple):
        i_digits = list(range(1,10))
        s_digits = ["one", "two", "three", "four",
        "five", "six", "seven", "eight", "nine"]
        digit_pairs = zip(i_digits, s_digits)
        digit_translate = {}
        for num, word in digit_pairs:
            digit_translate[num] = word
        words = []
        hundreds_digit, tens_and_ones = divmod(triple, 100)
        if hundreds_digit != 0:
            words.append(digit_translate[hundreds_digit] + " hundred")
        teens = {10: "ten", 11: "eleven", 12:"twelve", 13: "thirteen",
                 14: "fourteen", 15: "fifteen", 16:"sixteen",
                 17: "seventeen", 18: "eighteen", 19:"nineteen"}
        tens_place = {20:"twenty", 30:"thirty", 40:"forty", 50:"fifty",
        60:"sixty", 70:"seventy", 80:"eighty", 90:"ninety"}
        if tens_and_ones != 0:
            if tens_and_ones < 10:
                words.append(digit_translate[tens_and_ones])
            elif tens_and_ones < 20:
                words.append(teens[tens_and_ones])
            else:
                tens, ones = divmod(tens_and_ones, 10)
                words.append(tens_place[tens*10])
                if ones != 0:
                    words.append(digit_translate[ones]) 
        (' ').join(words)
        
    if number == 0:
        return "zero"
            
    triples = []
    quotient = number
    while quotient != 0:
        quotient, remainder = divmod(quotient, 1000)
        triples.append(remainder)
    print "triples:" + str(triples)
    triples_words = map(convert_triple, triples)
    print "triples_words: " + str(triples_words)
    endings = ['', " thousand", " million", " billion", " trillion", " quadrillion"]
    result = []
    for index, t in enumerate(triples_words):
        if t:
            result.append(t + endings[index])
    print "result: " + str(result)
    return " ".join(result[::-1])
        
                
