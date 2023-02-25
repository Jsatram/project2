

def fileAnalysis(file):
    """Function that begins the file Analysis"""
    def indentationCheck(line, sub):
        """Function to check the amount of indentation a line has, assuming the rest of the function has been corrected"""
        indents = line.count('\t')
        if indents == sub: # Passed line has enough indents and is good for placement
            return line, sub - 1
        else: 
            while indents < sub: # As as many indents as needed to match the currnet sub-level
                line = '\t' + line
            return line, sub - 1
        
    opened = open(file, 'r') # opens the file for reading and writing
    out = open('Updated.txt', 'a') # open a new file for appending the gather data
    
    for line in opened.readlines(): # function for re-writing the original file to the new file
        out.write(line)

    sub = 0 # checks the sublevel of a function (whether def or if has been called yet and indentation is needed)
    printKeywords = 0 # holds the number of times the print function is called
    while line is not None:
        if sub == 0:
            if line.__contains__('def '): # WE WILL NEED TO ADD FUNCATIONALITY TO CHECK IF THERE IS NO SPACE THIS IS A TEMP FIX
                    if line.__contains__('(') and line.__contains__(')') and line.__contains__(':'):
                        sub +=1
                        out.write(line)
                        line = opened.readline()
                    elif line.find('(') == -1: # this denotes the the first paraenthesis for the def function is missing
                        # since strings are immutatable have to make a new string with the missing piece and then overwrite that line of the file
                        line = line[:line.find('def') + 3] + '(' + line[line.find('def') + 3:]
                        out.write(line)
                        line = opened.readline()
                    elif line.find(')') == -1:
                        line = line[:line.find(':')] + ')' + line[line.find(':'):]
                        out.write(line)
                        line = opened.readline()
                    else:
                        line = line + ':'
                        out.write(line)
                        line = opened.readline()
            elif line.__contains__('if'):
                if line.__contains__(':'):
                    sub +=1
                    out.write(line)
                    line = opened.readline()
                else:
                    line = line + ':'
                    out.write(line)
                    line = opened.readline()
            else:
                printKeywords += line.count('print(') # Checking for the first paraenthesis since only function calls are wanted, not the actual word
                line = opened.readline()
        else:
            if line.__contains__('def'):
                if line.__contains__('(') and line.__contains__(')') and line.__contains__(':'):
                    line, sub = indentationCheck(line, sub) # Example using new indentation check method and skeleton for rest
                    out.write(line)
                    line = opened.readline()
                elif line.find('(') == -1: 
                    line = line[:line.find('def') + 3] + '(' + line[line.find('def') + 3:]
                    # Input measures for the indentation check
                elif line.find(')') == -1:
                    line = line[:line.find(':')] + ')' + line[line.find(':'):]
                    # Input measures for indentation check
                else:
                    line = line + ':'
                    # Input measures for indentation check





def main():
    """Main function to be run when in standalone"""
    fileName = input('Please input the name of the file')
    fileAnalysis(fileName)