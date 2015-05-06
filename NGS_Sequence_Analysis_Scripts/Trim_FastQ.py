"""
Created on Tue Apr 21 17:51:30 2014

@author: Yancheng Liu
"""


import tkinter.filedialog

def trim_fastq():
    ''' (file) -> NoneType

    Identify the reads containing the Himar1 ITR sequence, trim the reads to retain the 25bp immediately following the ITR sequence. 

    '''

    from_filename = tkinter.filedialog.askopenfilename()
    to_filename = tkinter.filedialog.asksaveasfilename()
    #stat_filename = tkinter.filedialog.asksaveasfilename()
    
    file = open (from_filename, 'r')
    fileOutput = open (to_filename, 'w')
    fileStatistics = open ('C:/Users/RussellLab/Desktop/Tn-Seq-12-3-14/TnSeq3_Stats.txt', 'a')

    line1 = 'start'
    total = 0
    match_AGCCAACCTGTTA = 0
    match_AGCCAACCTGTTTA = 0
    while (line1):
        line1 = file.readline()
        line2 = file.readline()
        line3 = file.readline()
        line4 = file.readline()
        total += 1

        if line2[16:29] == 'AGCCAACCTGTTA':
            fileOutput.write(line1)
            fileOutput.write(line2[29:59]+'\n')
            fileOutput.write(line3)
            fileOutput.write(line4[29:59]+'\n')
            match_AGCCAACCTGTTA +=1
        if line2[16:30] == 'AGCCAACCTGTTTA':
            fileOutput.write(line1)
            fileOutput.write(line2[30:60]+'\n')
            fileOutput.write(line3)
            fileOutput.write(line4[30:60]+'\n')
            match_AGCCAACCTGTTTA +=1           
            
    fileStatistics.write('total sequences: ')
    fileStatistics.write(str(total))
    fileStatistics.write(' ')
    fileStatistics.write('match_AGCCAACCTGTTA sequences: ')
    fileStatistics.write(str(match_AGCCAACCTGTTA))
    fileStatistics.write(' ')
    fileStatistics.write('match_AGCCAACCTGTTTA sequences: ')
    fileStatistics.write(str(match_AGCCAACCTGTTTA))
    fileStatistics.write('\n')
    file.close()
    fileOutput.close()
    fileStatistics.close()

def head_fastq():
    ''' (file) -> NoneType

    Write the first 200 lines in from_filename into to_filename.

    '''

    #tkinter.filedialog.askopenfilename()
    from_filename = tkinter.filedialog.askopenfilename()
    to_filename = tkinter.filedialog.asksaveasfilename()

    from_file = open(from_filename, 'r')
    head_contents = ''
    for i in range (200):
        head_contents += from_file.readline()
    from_file.close()

    to_file = open(to_filename, 'w')
    to_file.write('first 200 lines:\n\n')
    to_file.write(head_contents)
    to_file.close()

def count_reads():
    ''' (file) -> NoneType

    Count how many reads in a selected .fastq file. 

    '''

    from_filename = tkinter.filedialog.askopenfilename()
    to_filename = tkinter.filedialog.asksaveasfilename()
    
    
    file = open (from_filename, 'r')
    fileOutput = open (to_filename, 'a')
    

    line1 = 'start'
    total = 0
    match_TGTTA = 0
    match_TGTTTA = 0
    while (line1):
        line1 = file.readline()
        line2 = file.readline()
        line3 = file.readline()
        line4 = file.readline()
        total += 1

    fileOutput.write('total sequences: ')
    fileOutput.write(str(total))
    fileOutput.write('\n')
    file.close()
    fileOutput.close()
    print ("Done")
    




    
