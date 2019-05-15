# files.py

# general instructions: 
#   - print a blank line between sections of output
#   - Add your comments using triple quotes. Example:
''' student comment'''

def main():
    # we want to see what is going on in the file system.
    # open file explorer and navigate to your working directory. 
    # you should see just the files in the repo.

    '''
    - creation
    '''
    # files are created with the open function.
    # look at the different modes that can be used with this function
    # https://docs.python.org/3/library/functions.html#open

    # We will use the following file name in this exercise
    fileName = "myFile.txt"

    # try the following code:
    try:
        infile = open(fileName)
    except Exception as error:
        print(type(error), error)
    print()

    # try the following code:
    try:
        infile = open(fileName, 'r')
    except Exception as error:
        print(type(error), error)
    print()

    # What errors did you get? Add a comment here with the output:
    '''<class 'FileNotFoundError'> [Errno 2] No such file or directory: 'myFile.txt'''
    # The default mode for open() is 'r', so the statements above are really
    # the same code. Logically a file must exist in order for us to read it.

    # Now write the same code but change the mode to 'a'
    # your code here
    try:
        infile = open(fileName, 'a')
    except Exception as error:
        print(type(error), error)
    print()
    # close the file

    # run this program then look in the file explorer window. A new text 
    # file should be shown. Using a text editor, edit the text file to add 
    # some text - a few lines of gibberish. Don't forget to close the file
    # in the text editor.

    # Now write the same code but change the mode to 'w'
    # your code here. 
    try:
        infile = open(fileName, 'w')
    except Exception as error:
        print(type(error), error)
    print()
    # close the file

    # run the program then open the text file in a text editor and view 
    # the contents
    # add a comment here describing the contents:
    '''The file is now empty'''

    '''
    - element access
    - traversal
    '''
    fileName = "sample.txt"
    # View the file in a text editor.

    # There are several ways to read a file

    # Method 1: read()
    # open your book to p. 161 and replicate the code at the center of 
    # the page that opens, reads, and prints the file. Use "infile" again
    # as the file handle

    # compare the program output with what you see in a text editor.
    # are they the same? Add your answer in a comment here:

    # add a print statement that prints the length of data
    # this demonstrates that data is one big string.
    # you might try counting the characters to see if the length includes
    # line feeds.

    # closing the file - uncomment the line below when you get here
    #infile.close()

    # Method 2: readlines()
    # uncomment the code below and run this program
    '''
    infile = open(fileName)
    data = infile.readlines()
    print(data)
    print()
    infile.close()
    '''
    # answer the following questions:
    # what type is data?
    # how is it different from the data in Method 1?
    # Do the strings have escape characters?

    # write a for loop that uses data as the sequence and prints out
    # the text lines. What do you have to do in the print statement 
    # to make the ouput look like what you see in a text editor?

    # your code here

    # closing the file - uncomment the line below when you get here
    #infile.close()

    # Method 3: readline()
    # uncomment the following code, then add comments above each line
    # of code to describe what that line does
    '''
    infile = open(fileName)
    line = infile.readline()
    while line != "":
        print(line[:-1])
        line = infile.readline()
    infile.close()    
    '''

    # Method 4: using the file handle as a sequence
    # replicate the last section of code on p. 162 that uses infile as the
    # sequence in the for loop.
    # your code here


    '''
    - element insertion
    - element updates
    '''
    # these are really just writing to a file.
    # open "mydata.txt" for writing using the file handle "outfile"

    # Write several lines of gibberish to the file and close it.

    # view the new file in a text editor to verify that the program worked.


main()