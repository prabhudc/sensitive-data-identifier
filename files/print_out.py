# Initialize variables to collect and print content
s_singaporeID =  set([])
s_twitterID =  set([])
s_emails =  set([])
s_urls =  set([])
s_phoneNumber =  set([])
s_location =  set([])
s_creditCard =  set([])
v_line_count = 0
v_singaporeID_count = 0
v_twitterID_count = 0
v_emails_count = 0
v_urls_count = 0
v_phoneNumber_count = 0
v_location_count = 0
v_creditCard_count = 0


# Loop through each line and evaluate it's security risk
f_sens = open('files/output_emails.csv','r')
for line in f_sens:
    v_line_count += 1
    if len(find_singaporeID(line))>0:
        s_singaporeID.add(str(find_singaporeID(line)))
        v_singaporeID_count += 1
    if len(find_twitterID(line))>0:
        s_twitterID.add(str(find_twitterID(line)))
        v_twitterID_count += 1
    if len(find_emails(line))>0:
        s_emails.add(str(find_emails(line)))
        v_emails_count += 1
    if len(find_urls(line))>0:
        s_urls.add(str(find_urls(line)))
        v_urls_count += 1
    if len(find_phoneNumber(line))>0:
        s_phoneNumber.add(str(find_phoneNumber(line)))
        v_phoneNumber_count += 1
    if len(find_location(line))>0:
        s_location.add(str(find_location(line)))
        v_location_count += 1
    if len(find_creditCard(line))>0:
        s_creditCard.add(str(find_creditCard(line)))
        v_creditCard_count += 1
f_out_sens.close()


# Print the content in a human readable format
print "Total number of lines in the file : " + str(v_line_count)
print "\n\nTotal number occurrences of Singaporean IDs in the file : " + str(v_singaporeID_count)
print "====> The Singapore IDs are " + str(s_singaporeID)
print "\n\nTotal number of occurrences Twitter IDs in the file : " + str(v_twitterID_count)
print "====> The Twitter IDs are " + str(s_twitterID)
print "\n\nTotal number of occurrences Email IDs in the file : " + str(v_emails_count)
print "====> The Email IDs are " + str(s_emails)
print "\n\nTotal number of occurrences URLs in the file : " + str(v_urls_count)
print "====> The URLs are " + str(s_urls)
print "\n\nTotal number of occurrences Ph Numbers in the file : " + str(v_phoneNumber_count)
print "====> The Phone numbers are " + str(s_phoneNumber)
print "\n\nTotal number of occurrences Addresses in the file : " + str(v_location_count)
print "====> The Addresses are " + str(s_location)
print "\n\nTotal number of occurrences Credit Cards in the file : " + str(v_creditCard_count)
print "====> The credit-card numbers are " + str(s_creditCard)