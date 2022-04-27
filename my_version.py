import sys
def my_version():
    versiom_as_regex=sys.version
    counter=0
    string=''
    while (versiom_as_regex[counter] != ' '):
        string=string + versiom_as_regex[counter]
        counter=counter+1
    return (string)  
my_version()


