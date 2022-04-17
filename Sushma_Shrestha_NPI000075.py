
    # Sushma Shrestha
    # NPI000075
import os
import datetime


def loginmenu():
    print()
    print()
    print("--------------------------------------------------------------------------------\n")
    print("             WELCOME TO OUR APPLICATION\n")
    print("--------------------------------------------------------------------------------\n")
    print()
    print()
    print("       1. Login\n")
    print("       2. Exit\n")
    print()
    print("=================================================================================\n")

    print()
    print()
    print("\tSelect operation to login(1) or exit(2) and enter number according to the menu !!!\n")
    operation = input("Operation: ")
    if operation == "1":
        print()
        print()
        input("\t\tpress enter to continue.............")
        os.system("cls")
        login()
    else:
        
        print()
        print()
        print("\n\n\tThankyou for using our application !!!")
        print()
        print()
        input("\t\tpress enter to exit.............")
        os.system("cls")
        


def login():
    un = ["Sushma", "Januka"]
    pw = ["password", "pass123"]
    log = 1

    print()
    print("------------------------------------------------------------------------------------------------------")
    print("                                          Login                    ")
    print("------------------------------------------------------------------------------------------------------")

    u = input("\n\n\t\tEnter username: ")
    p = input("\n\t\tEnter password: ")

    for i in un:
        for j in pw:
            if u == i and p == j:
                print("\n\tYou have successfully logged in!!")
                print()
                print()
                input("\t\tpress enter to continue.............")
                menu()
                log = 0
                break
    if log == 1:
        print("\n\tLogin failed.......")
        print("\n\tEither username or password is wrong!")
        again = input("\tDo you want to try again? (Y/N) : ")
        if again == 'Y':
            login()
        else:
            print("Thankyou for using application service !!")


def menu():
    os.system("cls")
    print()
    print()
    print("-------------------------------------------------------------------------------------------------------")
    print("                                         OPERATIONS                    ")
    print("-------------------------------------------------------------------------------------------------------")
    print("\t1. New Patient Registration (info, Test, Status).\n")
    print("\t2. Setting and changing patient status and Test data.\n")
    print("\t3. Statistical Information on Test Carried Out.\n")
    print("\t4. Searching Functionalities.\n")
    print("\t5. Sign Out! \n")

    print()
    print("    Which operation do you like to perform?")
    opt = input("   Enter number [1-5] according to menu: ")
    if opt == '1':
        print()
        print()
        input("\t\tpress enter to continue.............")
        os.system("cls")
        registration()
        print()
        print()
        input("\t\tpress enter to continue.............")
        os.system("cls")
        menu()
    elif opt == '2':
        print()
        print()
        input("\t\tpress enter to continue.............")
        os.system("cls")
        update_pt_status()
        print()
        print()
        input("\t\tpress enter to continue.............")
        os.system("cls")
        menu()
    elif opt == '3':
        print()
        print()
        input("\t\tpress enter to continue.............")
        os.system("cls")
        statis_info()
        print()
        print()
        input("\t\tpress enter to continue.............")
        os.system("cls")
        menu()
    elif opt == '4':
        print()
        print()
        input("\t\tpress enter to continue.............")
        os.system("cls")
        search()
        print()
        print()
        input("\t\tpress enter to continue.............")
        os.system("cls")
        menu()

    elif opt == '5':
        print()
        print("\n\n\tThank You for using our application service\n")
        input("\tPress enter to exit............")
    else:
        print("\n\tInvalid input !!!")
        try_num = input("\n\tDo you want to try again? Y/N : ")
        if try_num == 'Y' or try_num == 'y':
            print()
            print()
            input("\t\tpress enter to continue.............")
            os.system("cls")
            menu()
        else:
            print()
            print()
            input("Press enter to exit......................")
            os.system("cls")
            loginmenu()


def registration():
    print()
    print()
    print("-------------------------------------------------------------------------------------------------------")
    print("                                   Patient's Data/Registration                    ")
    print("-------------------------------------------------------------------------------------------------------")
    name = input("\tPatient's name: ")
    age = input("\tAge: ")
    gender = input("\tGender(M/F): ")
    email = input("\tEmail address: ")
    phone = input("\tPhone number: ")
    blood = input("\tBlood Group: ")

    print()
    print("--------------------------------------------------------------------------------------------------------")
    print("  Asymptomatic individuals with history of travelling overseas (ATO)\n")
    print("  Asymptomatic individuals with history of contact with known case of COVID-19 (ACC)\n")
    print("  Asymptomatic individuals who has attended event associated with known COVID-19 outbreak (AEO)\n")
    print("  Symptomatic Individuals (SID)\n")
    print("  Asymptomatic Hospital staff (AHS)\n")
    print("---------------------------------------------------------------------------------------------------------")

    print()
    print("ATO, ACC, AEO, SID, AHS are the patient's group\n")
    print()

    group = input("\tPatient's Group: ")
    ab = ["ATO", "ACC", "AEO", "SID", "AHS"]
    while group.upper() not in ab:
        print("\tYou entered invalid group !")
        print("\tEnter from ATO, ACC, AEO, SID, AHS !!")
        print("\tEnter again!!\n")
        print()
        group = input("\tPatient's Group: ")

    group = group.upper()
    print()
    print()
    zone = input("Input patient's zone A/B/C/D : ")
    z_check = ["A", "B", "C", "D"]
    while zone.upper() not in z_check:
        print("\tYou entered invalid zone !")
        print("\tEnter from A, B, C, D !!")
        print("\tEnter again!!\n")
        print()
        zone = input("\tPatient's zone: ")

    zone = zone.upper()

    x = datetime.datetime.now()

    
    f = open("sampletext.txt", "r")
    line = f.readline()
    if line == "":
        line = 1
    else:
        line = int(line) + 1

    f = open("sampletext.txt", "w")
    line = str(line)
    f.write(line)
    with open("Registration_Data.txt", "a") as ff:
        ff.write(line + "--" + name + "--" + group + "--" + zone + "--" + str(
            age) + "--" + gender + "--" + blood + "--" + str(phone) + "--" + email + "--" +
                 str(x.strftime("%Y")) + "-" + str(x.strftime("%m")) + "-" + str(x.strftime("%d")) + "\n")

    f.close()
    print()
    print("\tThe patient's ID is " + line)
    print()
    input("\t\tpress enter to continue.............")
    os.system("cls")

    test(line, group, zone, name)


def test(ids, type_grp, zone, name):
    status = ""
    data_all = ""
    print()
    print()

    print("-----------------------------------------------------------------------------------------------------------")
    print("                                   Test data collection")
    print("-----------------------------------------------------------------------------------------------------------")

    tst_1 = input("\tTest 1 done or not? Y/N : ")

    while tst_1 == "Y":
        result1 = input("\tWhat was the result of Test 1? positive(P) or negative(N) : ")

        if result1 == "P" or result1 == "positive":

            status = "Active"

            if type_grp == "AHS":
                print()
                print("\tHome Quarantine (No follow-Up test Required.\n")

                data_all = ids + " " + type_grp + " " + "T1" + " " + "P" + " " + "HQNF" + "\n"
                break
            else:
                print()
                print("\tQuarantine in Hospital Normal Ward or ICU (No follow-Up Test Required)\n")

                ad = input("\tPatient's admitted place (Normal Ward(NW) or ICU): ")
                data_all = ids + " " + type_grp + " " + "T1" + " " + "P" + " " + "QHNF" + " " + ad + "\n"
                break

        tst_2 = input("\tTest 2 done or not? Y/N : ")

        if tst_2 == "Y":
            result2 = input("\tWhat was the result of Test 2? positive(P) or negative(N) : ")
            if result2 == "P" or result2 == "positive":

                status = "Active"

                if type_grp == "AHS":
                    print()
                    print("\tHome Quarantine (No follow-Up test Required.\n")

                    data_all = ids + " " + type_grp + " " + "T1" + " " + "N" + " " + "T2" + " " + "P" + " " + "HQNF" + "\n"
                    break

                else:
                    print()
                    print("\tQuarantine in Hospital Normal Ward or ICU (No follow-Up Test Required)\n")

                    ad = input("\tPatient's admitted place (Normal Ward(NW) or ICU): ")

                    data_all = ids + " " + type_grp + " " + "T1" + " " + "N" + " " + "T2" + " " + "P" + " " + "QHNF" + " " + ad + "\n"

                    break

            tst_3 = input("\tTest 3 done or not? Y/N : ")

            if tst_3 == "Y":
                result3 = input("\tWhat was the result of Test 3? positive(P) or negative(N) : ")
                if result3 == "P" or result3 == "positive":

                    status = "Active"

                    if type_grp == "AHS":
                        print()
                        print("\tHome Quarantine (No follow-Up test Required.\n")
                        data_all = ids + " " + type_grp + " " + "T1" + " " + "N" + " " + "T2" + " " + "N" + "T3" + " " + "P" + " " + "HQNF" + "\n"
                        break

                    else:
                        print()
                        print("\tQuarantine in Hospital Normal Ward or ICU (No follow-Up Test Required)\n")

                        ad = input("Patient's admitted place (Normal Ward(NW) or ICU): ")

                        data_all = ids + " " + type_grp + " " + "T1" + " " + "N" + " " + "T2" + " " + "N" + " " + "T3" + " " + "P" + " " + "QHNF" + " " + ad + "\n"
                        break
                else:
                    if type_grp == "AHS":
                        print()
                        print("\tContinue Working\n")

                        data_all = ids + " " + type_grp + " " + "T1" + " " + "N" + " " + "T2" + " " + "N" + " " + "T3" + " " + "N" + " " + "CW" + "\n"
                        break

                    else:
                        print()
                        print("\tAllow reunion with family\n")

                        data_all = ids + " " + type_grp + " " + "T1" + " " + "N" + " " + "T2" + " " + "N" + " " + "T3" + " " + "N" + " " + "RU" + "\n"
                        break
            else:
                print("Do Test 3 after 7 days of Test 2 !!!\n")
                if type_grp == "AHS":
                    print()
                    print("\tContinue working (Follow-Up Test Required)\n")

                    data_all = ids + " " + type_grp + " " + "T1" + " " + "N" + " " + "CWFR" + " " + "T2" + " " + "N" + " " + "CWFR" + "\n"
                    break

                elif type_grp == "SID":
                    print()
                    print("\tHome Quarantine (Follow-Up Test Required)\n")

                    data_all = ids + " " + type_grp + " " + "T1" + " " + "N" + " " + "HQFR" + " " + "T2" + " " + "N" + " " + "HQFR" + "\n"
                    break

                else:
                    print()
                    print("\tQuarantine and designated Centres (follow-Up Test Required)\n")

                    data_all = ids + " " + type_grp + " " + "T1" + " " + "N" + " " + "QDFR" + " " + "T2" + " " + "N" + " " + "QDFR" + "\n"

                    break




        else:

            print("\tDo Test 2 after 7 days of Test 1 !!!\n")

            if type_grp == "AHS":
                print()
                print("\tContinue working (Follow-Up Test Required)\n")

                data_all = ids + " " + type_grp + " " + "T1" + " " + "N" + " " + "CWFR" + "\n"
                break

            elif type_grp == "SID":
                print()
                print("\tHome Quarantine (Follow-Up Test Required)\n")

                data_all = ids + " " + type_grp + " " + "T1" + " " + "N" + " " + "HQFR" + "\n"
                break

            else:
                print()
                print("\tQuarantine and designated Centres (follow-Up Test Required)\n")
                data_all = ids + " " + type_grp + " " + "T1" + " " + "N" + " " + "QDFR" + "\n"

                break

    if tst_1 == "N":
        print("Do test 1 as soon as possible !!\n")
        data_all = ids + " " + type_grp + "\n"

    with open("Test.txt", "a") as f:
        f.write(data_all)

    statuss(ids, type_grp, zone, name, status)


def statuss(ids, type_grp, zone, name, pt_status):
    print()
    print()
    print(
        "-----------------------------------------------------------------------------------------"
        "---------------------")
    print("                                    PATIENT'S STATUS")
    print(
        "-------------------------------------------------------------------------------------------"
        "-------------------")
    print()
    print()
    if pt_status == "":
        pt_status = "Unknown"
    with open("status.txt", "a+") as f:
        f.write(ids + "--" + name + "--" + type_grp + "--" + zone + "--" + pt_status + "\n")

        print("status written as: " + pt_status)


def update_pt_status():
    
    print()
    print()
    print(
        "--------------------------------------------------------------------------------------------------------------")
    print("                                     Modify")
    print(
        "--------------------------------------------------------------------------------------------------------------")
    print()
    print()
    print("                 1. Test Done and Action Taken\n")
    print("                 2. Active, Recovered or Death Status\n")

    print("\tWhich operation would you like to do?\n")
    opt = input("\tEnter num(1 or 2) according to menu: ")
    if opt == "1":
        print()
        print()
        input("\t\tpress enter to continue.............")
        os.system("cls")
        up_test()
    if opt == "2":
        print()
        print()
        input("\t\tpress enter to continue.............")
        os.system("cls")
        up_status()


def up_test():
    print()
    print()
    print(
        "------------------------------------------------------------------------------------------------------------")
    print("                                   Test Data Modify")
    print(
        "------------------------------------------------------------------------------------------------------------")

    print()
    print()

    status = ""
    f_r = open("Test.txt", "r")
    f_w = open("temp.txt", "w")

    ids = input("\tEnter patient's id: ")

    s = " "
    while (s):
        s = f_r.readline()
        L = s.split(" ")
        if len(s) > 0:
            if L[0] == ids:

                print()
                print()
                print("\tUPDATE ON TEST 1\n")
                print()

                type_grp = L[1]
                tst_1 = input("\tTest 1 done or not? (Y/N): ")

                while tst_1 == "Y":
                    result1 = input("\tWhat was the result of Test 1? positive(P) or negative(N) : ")

                    if result1 == "P" or result1 == "positive":

                        status = "Active"
                        up_status(L[0], status)

                        if type_grp == "AHS":
                            print()
                            print("\tHome Quarantine (No follow-Up test Required.\n")

                            file = L[0] + " " + type_grp + " " + "T1" + " " + "P" + " " + "HQNF" + "\n"
                            f_w.write(file)
                            break

                        else:
                            print()
                            print("\tQuarantine in Hospital Normal Ward or ICU (No follow-Up Test Required)\n")

                            ad = input("\tPatient's admitted place (Normal Ward(NW) or ICU): ")

                            file = L[0] + " " + type_grp + " " + "T1" + " " + "P" + " " + "QHNF" + " " + ad + "\n"
                            f_w.write(file)
                            break

                    print()
                    print()
                    print("\tUPDATE ON TEST 2\n")

                    tst_2 = input("\tTest 2 done or not? Y/N : ")

                    if tst_2 == "Y":
                        result2 = input("\tWhat was the result of Test 2? positive(P) or negative(N) : ")
                        if result2 == "P" or result2 == "positive":

                            status = "Active"
                            up_status(L[0], status)

                            if type_grp == "AHS":
                                print()
                                print("\tHome Quarantine (No follow-Up test Required.\n")

                                file = L[0] + " " + type_grp + " " + "T1" + " " + "N" + " " + \
                                       "T2" + " " + "P" + " " + "HQNF" + "\n"
                                f_w.write(file)
                                break

                            else:
                                print()
                                print("\tQuarantine in Hospital Normal Ward or ICU (No follow-Up Test Required)\n")

                                ad = input("\tPatient's admitted place (Normal Ward(NW) or ICU): ")

                                file = L[0] + " " + type_grp + " " + "T1" + " " + "N" + " " + "T2" + \
                                       " " + "P" + " " + "QHNF" + " " + ad + "\n"
                                f_w.write(file)
                                break

                        print()
                        print()
                        print("\tUPDATE ON TEST 3\n")

                        tst_3 = input("\tTest 3 done or not? Y/N : ")

                        if tst_3 == "Y":
                            result3 = input("\tWhat was the result of Test 2? positive(P) or negative(N) : ")
                            if result3 == "P" or result3 == "positive":

                                status = "Active"
                                up_status(L[0], status)

                                if type_grp == "AHS":
                                    print()
                                    print("\tHome Quarantine (No follow-Up test Required.\n")

                                    file = L[0] + " " + type_grp + " " + "T1" + " " + "N" + " " + \
                                           "T2" + " " + "N" + "T3" + " " + "P" + " " + "HQNF" + "\n"
                                    f_w.write(file)
                                    break

                                else:
                                    print()
                                    print("\tQuarantine in Hospital Normal Ward or ICU (No follow-Up Test Required)\n")

                                    ad = input("Patient's admitted place (Normal Ward(NW) or ICU): ")

                                    file = L[0] + " " + type_grp + " " + "T1" + " " + "N" + " " + \
                                           "T2" + " " + "N" + " " + "T3" + " " + "P" + " " + "QHNF" + " " + ad + "\n"
                                    f_w.write(file)
                                    break


                            else:

                                up_status(L[0], status)
                                if type_grp == "AHS":
                                    
                                
                                    print()
                                    print("\tContinue Working\n")

                                    file = L[0] + " " + type_grp + " " + "T1" + " " + "N" + " " + \
                                           "T2" + " " + "N" + " " + "T3" + " " + "N" + " " + "CW" + "\n"
                                    f_w.write(file)
                                    break

                                else:
                                    print()
                                    print("\tAllow reunion with family\n")

                                    file = L[0] + " " + type_grp + " " + "T1" + " " + "N" + " " + \
                                           "T2" + " " + "N" + " " + "T3" + " " + "N" + " " + "RU" + "\n"
                                    f_w.write(file)
                                    break


                        else:

                            up_status(L[0], status)

                            print()
                            
                            print("\tDo Test 3 after 7 days of Test 2 !!!\n")
                            if type_grp == "AHS":
                                print()
                                print("\tContinue working (Follow-Up Test Required)\n")

                                file = L[0] + " " + type_grp + " " + "T1" + " " + "N" + " " + "CWFR" + " " + \
                                       "T2" + " " + "N" + " " + "CWFR" + "\n"
                                f_w.write(file)
                                break

                            elif type_grp == "SID":
                                print()
                                print("\tHome Quarantine (Follow-Up Test Required)\n")

                                file = L[0] + " " + type_grp + " " + "T1" + " " + "N" + " " + "HQFR" + " " + \
                                       "T2" + " " + "N" + " " + "HQFR" + "\n"
                                f_w.write(file)
                                break

                            else:
                                print()
                                print("\tQuarantine and designated Centres (follow-Up Test Required)\n")

                                file = L[0] + " " + type_grp + " " + "T1" + " " + "N" + " " + "QDFR" + \
                                       " " + "T2" + " " + "N" + " " + "QDFR" + "\n"
                                f_w.write(file)
                                break




                    else:

                        up_status(L[0], status)

                        print()
                        print("\tDo Test 2 after 7 days of Test 1 !!!\n")

                        if type_grp == "AHS":
                            print()
                            print("\tContinue working (Follow-Up Test Required)\n")

                            file = L[0] + " " + type_grp + " " + "T1" + " " + "N" + " " + "CWFR" + "\n"
                            f_w.write(file)
                            break

                        elif type_grp == "SID":
                            print()
                            print("\tHome Quarantine (Follow-Up Test Required)\n")

                            file = L[0] + " " + type_grp + " " + "T1" + " " + "N" + " " + "HQFR" + "\n"
                            f_w.write(file)
                            break

                        else:
                            print()
                            print("\tQuarantine and designated Centres (follow-Up Test Required)\n")

                            file = L[0] + " " + type_grp + " " + "T1" + " " + "N" + " " + "QDFR" + "\n"
                            f_w.write(file)
                            break

                if tst_1 == "N":
                    up_status(L[0], status)
                    print()
                    print("\tDo test 1 as soon as possible !!\n")
                    file = L[0] + " " + type_grp + "\n"

                    f_w.write(file)


            else:
                f_w.write(s)

    f_w.close()
    f_r.close()
    os.remove("Test.txt")
    os.rename("temp.txt", "Test.txt")


def up_status(ids="", a=""):
    if a == "":
        print()
        print()
        print(
            "----------------------------------------------------------------------------------------------------------")
        print("                                      Status Modify")
        print(
            "----------------------------------------------------------------------------------------------------------")
        print()
        print()

    f_r = open("status.txt", "r")
    f_w = open("temp1.txt", "w")

    if ids == "":
        ids = input("\tEnter patient's id: ")

    s = " "
    while (s):
        s = f_r.readline()
        L = s.split("--")
        if len(s) > 0:
            if L[0] == ids:
                if a == "":
                    a = input("\tUpdated status: ")
                L[4] = a
                f_w.write(L[0] + "--" + L[1] + "--" + L[2] + "--" + L[3] + "--" + L[4] + "\n")
            else:
                f_w.write(s)

    f_w.close()
    f_r.close()
    os.remove("status.txt")
    os.rename("temp1.txt", "status.txt")
    


def statis_info():
    print()
    print()
    print(
        "-------------------------------------------------------------------------------------------------------------")
    print("                  Statistical Information on Test Carried Out")
    print(
        "-------------------------------------------------------------------------------------------------------------")
    print()
    print()
    print("            1. Number of Test Done")
    print("            2. Total Active Cases")
    print("            3. Total Recovered Cases")
    print("            4. Total Death Cases")
    print("            5. Whole Data")
    print("            6. Patients Tested")
    print("            7. Active cases group wise")
    print("            8. Active cases zone wise")
    print()
    print()
    print("\tWhich operation do you like to do?")
    opt = input("\tOPERATION No. : ")

    while opt != "":
        if opt == "1":
            print()
            print()
            input("\t\tpress enter to continue.............")
            os.system("cls")
            test_total()
            
            break
            

        elif opt == "2":
            
            active()
            break
            

        elif opt == "3":
            
            recover()
            break

        elif opt == "4":
            
            Death()
            break

        elif opt == "5":
            
            test_total()
            active()
            recover()
            Death()
            break
            
        elif opt == "6":
            print()
            print()
            input("\t\tpress enter to continue.............")
            os.system("cls")
            tested_one()
            break

        elif opt == "7":
            print()
            print()
            input("\t\tpress enter to continue.............")
            os.system("cls")
            active_group()
            break
        elif opt == "8":
            print()
            print()
            input("\t\tpress enter to continue.............")
            os.system("cls")
            active_zone()
            break
            
        else:
            print("\tInvalid operation input !!!")
            opt = input("\tEnter again: ")




def test_total():
    print()
    print()

    f_r = open("Test.txt", "r")

    s = " "
    count = 0
    count1 = 0
    count2 = 0
    count3 = 0

    while (s):
        a = 0
        s = f_r.readline()
        L = s.split(" ")

        if len(s) > 0:

            kk = L[-1]
            check = L.index(kk)

            while a <= check:

                if L[a] == 'T1' or L[a] == 'T1\n':
                    count1 += 1

                if L[a] == 'T2' or L[a] == 'T2\n':
                    count2 += 1

                if L[a] == 'T3' or L[a] == 'T3\n':
                    count3 += 1

                a += 1

        else:
            break

    count = count1 + count2 + count3

    print()
    print()
    print("\tThe total number of Test 1 conducted: " + str(count1))
    print()
    print("\tThe total number of Test 2 conducted: " + str(count2))
    print()
    print("\tThe total number of Test 3 conducted: " + str(count3))
    print()

    print("\tThe total number of Test conducted: " + str(count))

    f_r.close()
    
def active():
    
    f_r = open("status.txt", "r")
    count = 0
    s = " "
    while (s):
        a = 0
        s = f_r.readline()
        L = s.split("--")
        if len(s) > 0:

            kk = L[-1]
            check = L.index(kk)

            while a <= check:
                word = L[a]

                if word.lower() == "active" or word.lower() == "active\n":
                    count += 1

                a += 1

    print()
    print()
    print("\tThe total number of active cases: " + str(count))

    f_r.close()

def active_group():

    # 2 is group
    f_r = open("status.txt", "r")
    count = 0
    s = " "
    ATO = 0
    ACC = 0
    AEO = 0
    SID = 0
    AHS = 0
    li_ato = []
    li_acc = []
    li_aeo = []
    li_sid = []
    li_ahs = []
    while (s):
        a = 0
        s = f_r.readline()
        L = s.split("--")
        if len(s) > 0:

            kk = L[-1]
            check = L.index(kk)

            while a <= check:
                word = L[a]

                if word.lower() == "active" or word.lower() == "active\n":
                    if L[2] == "ATO":
                        ATO += 1
                        li_ato.append(L)

                    elif L[2] == "ACC":
                        ACC += 1
                        li_acc.append(L)

                    elif L[2] == "AEO":
                        AEO += 1
                        li_aeo.append(L)

                    elif L[2] == "SID":
                        SID += 1
                        li_sid.append(L)

                    elif L[2] == "AHS":
                        AHS += 1
                        li_ahs.append(L)
   
                a += 1

    count = ATO + ACC + AEO + SID + AHS

    print()
    print()
    print("\tThe total number of active cases in ATO group: " + str(ATO))
    print()
    print("\tThe total number of active cases in ACC group: " + str(ACC))
    print()
    print("\tThe total number of active cases in AEO group: " + str(AEO))
    print()
    print("\tThe total number of active cases in SID group: " + str(SID))
    print()
    print("\tThe total number of active cases in AHS group: " + str(AHS))
    print()
    print("\tThe total number of active cases: " + str(count))
    print()

    print()
    print("---------------------------------------------------------------------------------------")
    print("                              ATO ACTIVE CASES")
    if ATO > 0:
        a = 0
        while a < len(li_ato):
            print()
            print("Patient' s Id:\t" + str(li_ato[a][0]))
            print("Patient' s Name:\t" + str(li_ato[a][1]))
            a += 1

    else:
        print()
        print("\tThe active case of ATO is 0.")

    print()
    print("---------------------------------------------------------------------------------------")
    print("                         ACC ACTIVE CASES")

    if ACC > 0:
        b = 0
        while b < len(li_acc):
            print()
            print("Patient' s Id:\t" + str(li_acc[b][0]))
            print("Patient' s Name:\t" + str(li_acc[b][1]))
            b += 1

    else:
        print()
        print("\tThe active case of ACC is 0")

    print()
    print("---------------------------------------------------------------------------------------")
    print("                         AEO ACTIVE CASES")

    if AEO > 0:
        c = 0
        while c < len(li_aeo):
            print()
            print("Patient' s Id:\t" + str(li_aeo[c][0]))
            print("Patient' s Id:\t" + str(li_aeo[c][1]))
            c += 1

    else:
        print()
        print("\tThe active case of AEO is 0.")
        

    print()
    print("---------------------------------------------------------------------------------------")
    print("                         SID ACTIVE CASES")

    if SID > 0:
        d = 0
        while d < len(li_sid):
            print()
            print("Patient' s Id:\t" + str(li_sid[d][0]))
            print("Patient' s Name:\t" + str(li_sid[d][1]))
            d += 1
    else:
        print()
        print("\tThe active case of SID is 0.")

    print()
    print("---------------------------------------------------------------------------------------")
    print("                         AHS ACTIVE CASES")

    if AHS > 0:
        e = 0
        while e < len(li_ahs):
            print()
            print("Patient' s Id:\t" + str(li_ahs[e][0]))
            print("Patient' s Name:\t" + str(li_ahs[e][1]))
            e += 1
    else:
        print()
        print("\tThe active case of AHS is 0.")

        
    f_r.close()

def active_zone():
    # 3 is zone
    
    f_r = open("status.txt", "r")
    count = 0
    s = " "
    A =0
    B = 0
    C = 0
    D = 0
    li_a = []
    li_b = []
    li_c = []
    li_d = []
    
    while (s):
        a = 0
        s = f_r.readline()
        L = s.split("--")
        if len(s) > 0:

            kk = L[-1]
            check = L.index(kk)

            while a <= check:
                word = L[a]

                if word.lower() == "active" or word.lower() == "active\n":
                    if L[3] == "A":
                        A += 1
                        li_a.append(L)

                    elif L[3] == "B":
                        B += 1
                        li_b.append(L)

                    elif L[3] == "C":
                        C += 1
                        li_c.append(L)

                    elif L[3] == "D":
                        D += 1
                        li_d.append(L)
   
                a += 1

    count = A + B + C + D

    print()
    print()
    print("\tThe total number of active cases in zone A: " + str(A))
    print()
    print("\tThe total number of active cases in zone B: " + str(B))
    print()
    print("\tThe total number of active cases in zone C: " + str(C))
    print()
    print("\tThe total number of active cases in zone D: " + str(D))
    print()
    print("\tThe total number of active cases: " + str(count))
    print()

    print()
    print("---------------------------------------------------------------------------------------")
    print("                             ACTIVE CASES OF ZONE A")
    if A > 0:
        k = 0
        while k < len(li_a):
            print()
            print("Patient' s Id:\t" + str(li_a[k][0]))
            print("Patient' s Id:\t" + str(li_a[k][1]))
            k += 1

    else:
        print("\tThe active case of zone A is 0.")

    print()
    print("---------------------------------------------------------------------------------------")
    print("                         ACTIVE CASES OF ZONE B")

    if B > 0:
        b = 0
        while b < len(li_b):
            print()
            print("Patient' s Id:\t" + str(li_b[b][0]))
            print("Patient' s Id:\t" + str(li_b[b][1]))
            b += 1

    else:
        print("\tThe active case of zone B is 0")

    print()
    print("---------------------------------------------------------------------------------------")
    print("                         ACTIVE CASES OF ZONE C")

    if C > 0:
        c = 0
        while c < len(li_c):
            print()
            print("Patient' s Id:\t" + str(li_c[c][0]))
            print("Patient' s Id:\t" + str(li_c[c][1]))
            c += 1

    else:
        print("\tThe active case of zone C is 0.")
        

    print()
    print("---------------------------------------------------------------------------------------")
    print("                         ACTIVE CASES OF ZONE D")

    if D > 0:
        d = 0
        while d < len(li_d):
            print()
            print("Patient' s Id:\t" + str(li_d[d][0]))
            print("Patient' s Id:\t" + str(li_d[d][1]))
            d += 1
    else:
        print("\tThe active case of zone D is 0.")


        
    f_r.close()



def recover():
    f_r = open("status.txt", "r")
    count = 0
    s = " "
    while (s):
        a = 0
        s = f_r.readline()
        L = s.split("--")
        if len(s) > 0:

            kk = L[-1]
            check = L.index(kk)

            while a <= check:
                word = L[a]

                if word.lower() == "recovered" or word.lower() == "recovered\n":
                    count += 1

                a += 1

    print()
    print()
    print("\tThe total number of recovered cases: " + str(count))

    f_r.close()


def Death():
    f_r = open("status.txt", "r")
    count = 0
    s = " "
    while (s):
        a = 0
        s = f_r.readline()
        L = s.split("--")
        if len(s) > 0:

            kk = L[-1]
            check = L.index(kk)

            while a <= check:
                word = L[a]

                if word.lower() == "dead" or word.lower() == "dead\n":
                    count += 1

                a += 1

    print()
    print()
    print("\tThe total number of death cases: " + str(count))

    f_r.close()


def tested_one():
    print()
    print()

    f_r = open("Test.txt", "r")
    f1_r = open("Registration_Data.txt", "r")
    s = " "
    t = " "
    total = []

    while (s):
        a = 0
        s = f_r.readline()
        L = s.split(" ")
        data = []
        data.append(L[0])
        if len(s) > 0:

            kk = L[-1]
            check = L.index(kk)

            while a <= check:
                
                if L[a] == 'T1' or L[a] == 'T1\n':
                    data.append("T1")

                if L[a] == "T2" or L[a] == "T2\n":
                    data.append("T2")

                if L[a] == "T3" or L[a] == "T3\n":
                    data.append("T3")

                a += 1

            total.append(data)
    g = 0
    while (t):
        t = f1_r.readline()
        M = t.split("--")

        if len(t) > 0:
            if total[g][0] == M[0]:
                print()
                print()
                print("Patient' s ID:\t" + total[g][0])
                print("Patient' s name:\t" + M[1])
                print("Patient' s test done:\t" + str(total[g][2:]))

                g += 1

    f_r.close()
    f1_r.close()


def search():
    print()
    print()
    print("\n------------------------------------------------------------------------------------\n")
    print("\t                       SEARCH FUNCTIONALITIES")
    print("--------------------------------------------------------------------------------------")
    
    print()
    print("                    1. Patient' s record")
    print("                    2. Status of patient")
    print("                    3. Deceased patient' s record")
    print()
    print("---------------------------------------------------------------------------------------")
    print()
    print()
    print("\tWhat would you like to search for?")
    print()
    print("\tEnter according to the menu [1/2/3] !!!")
    search = input("\n\tSearch: ")

    while search != "":
        if search == "1":
            print()
            print()
            input("\t\tpress enter to continue.............")
            os.system("cls")
            records()
            break
        elif search == "2":
            print()
            print()
            input("\t\tpress enter to continue.............")
            os.system("cls")
            st_atus()
            break
        elif search == "3":
            print()
            print()
            input("\t\tpress enter to continue.............")
            os.system("cls")
            deceased()
            break
        else:
            print()
            print("\tInvalid Input !!!")
            print("\tEnter 1/2/3 !!")
            search = input("\n\tSearch: ")



def records():
    print()
    print()

    id_s = input("\tID of patient to be searched: ")
    fr = open("Test.txt", "r")
    f1r = open("Registration_Data.txt", "r")
    s = " "
    t = " "
    data = []

    while (s):
        a = 0
        s = fr.readline()
        L = s.split(" ")
        

        if len(s) > 0:
            if L[0] == id_s:
                data.append(L[0])
                kk = L[-1]
                check = L.index(kk)

                while a <= check:
                    
                    if L[a] == 'T1' or L[a] == 'T1\n':
                        
                        data.append("T1")

                    if L[a] == "T2" or L[a] == "T2\n":
                        data.append("T2")

                    if L[a] == "T3" or L[a] == "T3\n":
                        data.append("T3")

                    a += 1
    
    while (t):
        t = f1r.readline()
        M = t.split("--")

        if len(t) > 0:
            if data[0] == M[0]:
                print()
                print()
                print("-------------------------------------------------------------------------------------")
                print("\tPATIENT'S INFO")
                print("-------------------------------------------------------------------------------------")
                print()
                print("\n\n   Patient' s ID:\t" + data[0] + "\t" + "Registration Date:\t" + M[9])
                print("\n\ttName:\t" + M[1])
                print("\n\ttest done:\t" + str(data[1:]))
                print("\n\tGroup:\t" + M[2])
                print("\n\tZone:\t" + M[3])
                print("\n\tAge:\t" + M[4])
                print("\n\tGender:\t" + M[5])
                print("\n\tBlood Group:\t" + M[6])
                print("\n\tPhone number:\t" + M[7])
                print("\n\temail address:\t" + M[8])
                print()
                print("--------------------------------------------------------------------------------------")
                

            

    fr.close()
    f1r.close()
    

def st_atus():
    print()
    print()
    print()
    f_r = open("status.txt", "r")
    print("\tEnter the id of the patient whose status is to be searched!!!")
    id_s = input("\n\tID: ")
    
    s = " "
    while (s):
        a = 0
        s = f_r.readline()
        L = s.split("--")
        if len(s) > 0:
            if L[0] == id_s:
                print()
                print()
                print("\n\n-----------------------------------------------------------------------------")
                print("\tPATIENT' S STATUS INFO")
                print("------------------------------------------------------------------------------")
                print()
                print("\n\tPatient' s ID: " + str(L[0]))
                print("\n\tName: " + str(L[1]))
                print("\n\tGroup: " + str(L[2]))
                print("\n\tZone: " + str(L[3]))
                print("\n\tStatus: " + str(L[4]))
                print()
                print("-------------------------------------------------------------------------------")


    f_r.close()

def deceased():
    print()
    print()
    print("----------------------------------------------------------------------------------------------")
    print("                  DECEASED PATIENT'S DATA")
    print("----------------------------------------------------------------------------------------------")
    print()
    print()
    fr = open("Test.txt", "r")
    f1r = open("Registration_Data.txt", "r")
    f2r = open("status.txt", "r") 
    u = " "
    s = " "
    t = " "
    data_id = []
    total = []
    
    while (u):
        u = f2r.readline()
        N = u.split("--")

        if len(u) > 0:
            if N[-1].lower() == "dead" or N[-1].lower() == "dead\n":
                data_id.append(N[0])


    p = len(data_id)
    if p > 0:
        g = 0
        while (t):
            t = f1r.readline()
            M = t.split("--")

            if len(t) > 0:
                if M[0] in data_id:
                    if data_id[g] == M[0]:
                        print()
                        print()
                        print("\tPatient' s ID:\t" + data_id[g] + "\t" + "Registration Date:\t" + M[9])
                        print("\tPatient' s name:\t" + M[1])
                        print()
                       
                        print("\tGroup:\t\t" + M[2])
                        print("\tZone:\t\t" + M[3])
                        print("\tAge:\t\t" + M[4])
                        print("\tGender:\t\t" + M[5])
                        print("\tBlood Group:\t" + M[6])
                        print("\tPhone number:\t" + M[7])
                        print("\temail address:\t" + M[8])
                        print()
                        print("----------------------------------------------------------------------------------------------")

                        g += 1
    else:
        
        print()
        print()
        print("\tThe number of deceased is 0.")

    fr.close()
    f1r.close()

loginmenu()














