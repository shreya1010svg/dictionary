
from Tkinter import *
master=Tk()
def NewWord(filename):
 f=open('filename.txt','a+')
 s=input('enter a word'':''meaning of word'':''part of speech'':')
 f.write(s)
 f.close()
NewWord('newfile.txt')


    pass
def display(word,part_of_speech,meaning,row_number=2):
    #Display of word and meaning.
    answer=word+'('+part_of_speech+'):'
    Label(master,text=answer,font='Helvetica 10').grid(row=row_number,column=0)
    Label(master,text=meaning,font='Helvetica 10').grid(row=row_number+1,column=0)
def displaying_many_words(list_of_word_meaning_tuples):
    #if many closest matches are found
    for i in range(0,len(list_of_word_meaning_tuples)):
        if i==0:
            k=2
        else:
            k=(i+1)*2
        display(list_of_word_meaning_tuples[i][0],list_of_word_meaning_tuples[i][1],list_of_word_meaning_tuples[i][2],k)
def if_word_not_found(word):
    def take_part_of_speech(event):
        part_speech=part_of_speech.get()
        flag=0
        if part_speech.lower()=='noun':
            part_speech='n'
        elif part_speech.lower()=='pronoun':
            part_speech='pron'
        elif part_speech.lower()=='verb':
            part_speech='v'
        elif part_speech.lower()=='adjective':
            part_speech='adj'
        elif part_speech.lower()=='adverb':
            part_speech='adv'
        elif part_speech.lower()=='preposition':
            part_speech='prep'
        elif part_speech.lower()=='conjunction':
            part_speech='conj'
        elif part_speech.lower()=='interjection':
            part_speech='interj'
        elif part_speech.lower()=='article':
            part_speech='art'
        else:
            Label(master,text='Invalid part of speech!',font='Helvetica 10 italic',padx=10).grid(row=6,column=0)
            flag=1
        if flag==0:
            lis.append(part_speech)
        if len(lis)==2:
            def take_meaning(event):
                lis.append(meaning.get())
                #print lis
                if len(lis)==3:
                    Label(master,text='New word and meaning successfully added!',font='Helvetica 10',padx=10).grid(row=8,column=0)
                    t=tuple(lis)
                shloka_func(t[0],t[1],t[2])
            Label(master,text='Enter meaning:',font='Helvetica 10',padx=10).grid(row=6,column=0)                                                                                     
            meaning=Entry(master)
            meaning.grid(row=6,column=1)
            meaning.bind("<Return>",take_meaning)
    '''def take_meaning(event):
        lis.append(meaning.get())'''
    #To add word entered and meaning if the word is not found
    lis=[word]
    Label(master,text='Word not found! Let us add it to the dictionary!',font='Helvetica 10 italic',padx=10).grid(row=3,column=0) 
    Label(master,text='Enter part of speech:',font='Helvetica 10',padx=10).grid(row=5,column=0)
    #Label(master,text='Enter meaning:',font='Helvetica 10',padx=10).grid(row=6,column=0)
    part_of_speech=Entry(master)
    part_of_speech.grid(row=5,column=1)
    part_of_speech.bind("<Return>",take_part_of_speech)
    '''if len(lis)==2:
        Label(master,text='Enter meaning:',font='Helvetica 10',padx=10).grid(row=6,column=0)                                                                                     
        meaning=Entry(master)
        meaning.grid(row=6,column=1)
        meaning.bind("<Return>",take_meaning)'''
    '''if len(lis)==3:
        Label(master,text='New word and meaning successfully added!',font='Helvetica 10',padx=10).grid(row=8,column=0)
        t=tuple(lis)
        print shloka_func(t[0],t[1],t[2])'''
def main():
    '''Main program where other functions are called.'''
    def give_word(event):
        #Gives word to other function. Function that takes the word should be called here.
        '''if word.get()=='Shreya':
            display('Shreya','n','Amazing person')
        else:
            if_word_not_found(word.get())'''
        akshatha_func(word.get())
    master.geometry('500x500')
    master.title('Dictionary')
    Label(master,text='Enter word:',font='Helvetica 10 bold',padx=10,pady=10).grid(row=0,column=0)
    word=Entry(master)
    word.grid(row=0,column=1)
    word.bind('<Return>',func=give_word)
    #display('Shreya','n','Amazing person')
main()
#displaying_many_words([('Shreya','n','Amazing person'),('Mandragoran','adj','Lans last name')])
mainloop()





