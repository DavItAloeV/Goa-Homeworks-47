def manual_difference(set1, set2):
    result = set1.copy()  
    result -= set2        
    return result



student_1 = {'სახელი': 'გიორგი', 'გვარი': 'ჯოხაძე', 'ასაკი': 16, 'საშუალო ქულა': 85}
student_2 = {'სახელი': 'ანა', 'გვარი': 'მამადაშვილი', 'ასაკი': 17, 'საშუალო ქულა': 90}


print(f"მოსწავლე 1: {student_1}")
print(f"მოსწავლე 2: {student_2}")
