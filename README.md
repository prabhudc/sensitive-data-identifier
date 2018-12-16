# sensitive-data-identifier
Identifiying sensitive data
# What does this utility do ?
Given a dataset, This tool flags sensitive information such as the following.
1) Credit card number
2) Email IDs
3) Telephone number
4) Identification numnber (Works for Singaporean IDs)
5) Twitter handles
6) Web URLs


# When do we use it ?
This tool could be used in scenarios such as a

1) Precursor to IT Remediation project
2) Auditing of unstructure datasets for sensitive information
3) General testing of documents for sensitive information

# How does it work ?

Currently the tool is set insode jupyter-notebook environment. In a true production scenario, it would be meant to be available as a python library to be run in batch mode. The tool's individual APIs could also be separately invoked for testing different scenarios. The output is presented in an easy-to-process list.

Following are APIs that the fool gives and its sample output.
The file run_log.txt gives the output-log of its execution in batch mode on multiple files.

**1) Email check API**

_find_emails("my email id is ipd2@illinois.edu")_

>> [('EMAIL', 'ipd2@illinois.edu')]

**2) Telephone number check API**

_find_phoneNumber("You can contact my manager at +7237724501", regex=None)_

>>[('PHONE', '7237724501')]

**3) URL check API**

_find_urls("If you think you're a muggle - You ought to visit http://www.mugglenet.com/ ")_

>>[('URL', 'http://www.mugglenet.com/')]


**4) Social Security ID check **(works only for Singapore's IDs as of now.**

_find_singaporeID('G9443425N')_

>>[('Singapore ID', 'G9443425N')]


**5) Twitter ID check**

_find_twitterID('If you''re caught by an obscurian, tweet me @scamander')_

>>[('TWITTER', '@scamander')]

**6) Address information check**

_find_location("I need to fix my sleigh. I live at Santa Claus 325,St. Santa Claus Lane, North Pole")_

>>[('Location', 'St'), ('Location', 'North')]


**7) Credit Card check**

_find_creditCard("My card with number 5510399013453413 seems to be blocked")_

>>[('CreditCard', '5510399013453413')]


**8) One API to rule them all - find any sensitive data**


_find_sensitive_data("I am Gandalf the Wizard, I live at Pinewood, North Mirkwood forest. My social realms are @GreyWizard. \
                    I pay my credit card bills to 5520-3277-9345-9498 with my glorious staff. If you need my help, call me at \
                    +7237724000 or email me at gandalf_the_grey@wizards.com. I shall come to thy help, unless I am busy with busy with my social media profile at https://wizard-world.com \
                    My exclusive wizrd-id is G1413425N")_
                    
                    
>>[('Singapore ID', 'G1413425N'),
>>('TWITTER', '@GreyWizard'),
>>('EMAIL', 'gandalf_the_grey@wizards.com'),
>>('URL', 'https://wizard-world.com'),
>>('PHONE', '7237724000'),
>>('Location', 'North Mirkwood'),
>>('CreditCard', '5520-3277-9345-9498')]

