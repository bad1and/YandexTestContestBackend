def first_part(void):
    return len(set("".join(void.split(",")[:3])))

def sec_part(void):
    return sum(int(z) for z in "".join(void.split(",")[3:5]).strip())

def third_part(void):
    return ord(void.split(",")[0][0].upper()) - ord('A') + 1

itog = []
for x in range(int(input())):
    main_inp = input()

    k_vo_simv_in_fio = first_part(main_inp) #к-во различных сивмолов ФИО - 1 пункт
    sum_day_month = sec_part(main_inp) #сумма цифр дня и мес - 2 пункт
    num_first_b_f = third_part(main_inp) #Номер в алфавите первой буквы фамилии - 3 пункт

    itog.append(hex(k_vo_simv_in_fio+sum_day_month*64+num_first_b_f*256)[-3:].upper().zfill(3))

print(" ".join(itog))