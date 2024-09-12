


#Basic_Networking_Interview_Questions

do_you_play = input('Do You Play _______Y/N___? ').lower()

if do_you_play != 'y':
    quit()

print('Lets Play')
count = 0

Question_1 = input('What is the FTP protocol ? ').upper()
if Question_1 =='FTP':
    print('Wow, Correct Answer')
    count += 1
else:
    print('Sorry,Incorrect Answer')

Question_2 = input('What is the MAC ? ').title()
if Question_2 =='Media Access Control':
    print('Wow, Correct Answer')
    count += 1
else:
    print('Sorry,Incorrect Answer')

Question_3 = input('What is the ARP ? ').title()
if Question_3 =='Address Resolution Protocol':
    print('Wow, Correct Answer')
    count += 1
else:
    print('Sorry,Incorrect Answer')

Question_3 = input('What is the TCP protocol ? ').title()
if Question_3 =='Transmission Control Protocol':
    print('Wow, Correct Answer')
    count += 1
else:
    print('Sorry,Incorrect Answer')


print("You Got" + " " +  str(count) + " " + "Out of 4")
print("which is" + " " + str((count/4 *100 ))+ "%")