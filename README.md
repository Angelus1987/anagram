# anagram
framework of project
Project parameters and description:

Section 2: Assignment Details
This section presents the required theory for completing the assessment, the
assessment’s application details, and the assessment criteria.
Provided code
To complete the assessment which will be explained in the forthcoming subsections you
are being provided with a few files. These will be briefly explained here and referred to
in relation in later subsections, as necessary. The provided files are:
1. AnagramsPalindromes.py
This is the file in which you will complete the required code. It has all required
function definitions, and some code included within it. You must use only these
functions to complete the final solution. You can however add additional
libraries, file references, and variable related code, as necessary.
2. load_dictionary.py
This file contains a method for opening a file. The function can be used to open
any file and return its contents as a list. It should be used to open the file
which contains the dictionary (words.txt). If necessary, it could be used to
read other similar files. This method should be accessed while remaining in this
separate file. You may not copy paste the function into the main solution file,
AnagramsPalindromes.py.
3. words.txt
This is the full dictionary file to be used within the assignment. It is the same
dictionary used in the solution from which the screenshots were taken. The
dictionary does not contain the words “I” or “A”. It is important you include
these words in the dictionary or dictionary list before accessing the list of
dictionary words in the activity functions.
4. smaller.txt
This is a smaller version of the dictionary, which you have the option of using to
test functionality of the activities. It is NOT mandatory to use this file. It is
intended to make testing your code quicker, as some activities, particularly
Activity B can take a longer amount of time to run using the words.txt
file.
However, when you submit the final solution make sure your solution is using
the words.txt
5. racecar-06.02.2020_17.03.06.txt
This is an example of a file, which would be output by Activity A. This example
shows the expected file output when there are no anagrams for the user
provided word, but the provided word itself is a palindrome.
4
6. assessment-06.02.2020_17.05.00.txt
This is an example of a file, which would be output by Activity A. This example
shows the expected file output, when there are no anagrams for the user
provided word, but the provided word itself is not a palindrome.
7. repaper-06.02.2020_17.11.03.txt
This is an example of a file, which would be output by Activity A. This example
shows the expected file output, when there are anagrams for the user provided
word, and the provided word itself is a palindrome.
8. dictionaryPalingrams.txt
This is an example of a file, which would be output by Activity B. It is an
incomplete file.
Prerequisite knowledge for assessment
The assessment will require you to find anagrams, palindromes, and palingrams. To do
this you need to understand what they are. The below section presents a simple
explanation of these concepts.
1. Anagrams
An anagram is a play on words created by rearranging the letters of the original word
to make a new word or phrase. Anagram examples can be fun and witty, and they often
end in hilarious results.
Anagrams are often longer words or phrases that do not necessarily mean anything but
are fun to come up with and say. There are also anagrams of simple words that create
random, new words that are not relevant to one another.
Single word anagram examples include:
• Tar = Rat
• Arc = Car
• Elbow = Below
• State = Taste
• Cider = Cried
• Dusty = Study
• Night = Thing
There are more complex phrases which include multiple words; however, this
assessment will focus on anagrams of single words found in the dictionary.
2. Palindromes
A palindrome is a word, phrase, number, or sequence of words that reads the same
backward as forward. Punctuation and spaces between the words or lettering is
allowed. This assessment will focus on single word, and two-word palindromes.
5
Single word palindrome examples include:
• anna
• civic
• kayak
• level
• madam
• mom
• noon
• racecar
• radar
• redder
3. Palingrams
A palingram is a sentence in which the letters, syllables, or words read the same
backward as they do forward.
Multiple word palindromes (palingrams) include:
• top spot
• my gym
• ala cicala
6
Overview
This assessment requires you to create an application, which can perform three
activities. The exact details of each activity will be explained in their own sub-sections.
This section will outline the primary high-level logic of the program – the main function
logic.
This application will start by presenting a brief explanation of:
• anagrams, palingrams and palindromes
• the activities which can be performed by the application
The function with this initial text is included in the provided in
AnagramsPalindromes.py. The function is called print_explanation().
The application should call this function to show the display in figure 1.
Figure 1 Display of the explanations
After the explanation is displayed the application should prompt the user to select
which activity, they would like performed, or “#” to be entered to end the application
(Figure 2).
Figure 2 Display of the prompt for activity choice or application end
The application should accept the user’s choice and perform the activities processes.
The processes should call the appropriate functions within the appropriate logic
structures.
After the Activity A, B, or C have run the program should always display the explanation
and re-prompt the user for a new activity selection. The application should only accept
UPPERCASE inputs of “A”, “B”, or “C”. The only other acceptable input is “#”. For
any other user input the program should redisplay the explanation and re-prompt the
user for the user’s selection of the activity.
7
The application should only stop running when the user enters the “#”. Otherwise it
must always continue to run.
The main()function should contain the primary display and prompting logic.
Activity A
Figure 3 shows acceptable user input to trigger activity “A”. Activity A finds the
anagrams for any word a user enters.
Figure 3 Acceptable input for triggering Activity A
The program prompts the user for their choice of a single word.
The application must check that the user’s input is a word or alphabetical characters. It
can not accept special characters or numbers. If the input is invalid the initial
explanation and user prompting should be re-displayed. The application should not
need to be restarted manually.
If the user was correct, the application should display the message “Using word =”
with the user’s input word added at the end. See figure 4, figure 5, and figure 6.
Once the sentence is displayed the application should use a combination of logic and
the provided functions to find the anagrams of the provided words. The anagrams
should be found by taking the user a word and searching the dictionary for anagrams of
equal length for the word. The application should compile a list of the anagrams if they
exist. It should then print the list of anagrams
• The first item in the anagram list should always be the user’s word
• All other items in the list should be sorted alphabetically (see figure 6)
Once the anagrams list has been created, all the items in the list should be printed as
shown in figure 4. The displaying of the list should be accomplished using the
print_generic_list() function. This same function should include code to
display a descriptive message of there being no anagrams to display of the list contains
no items. This code should not change if the function was called elsewhere and
provided different parameters.
After displaying the anagrams, the application should search the anagrams list for any
palindromes. The application should compile a list of the palindromes if they exist in the
list of anagrams. The list should include the word itself if it is a palindrome. The final
part of this functionality should display the message:
“Number of palindromes found = ” and the number of palindromes in the
list. e.g. “Number of palindromes found = 12”
8
Once the list of palindromes is formed its contents should be displayed using the
print_generic_list() function. If there are no palindromes the appropriate
message should be displayed (see figure 5).
After all the processing and the displaying of the information the entire result set should
be written to file. The write_anagrams_palindromes_to_file() function
should be used to accomplish the task.
The function should store the list of anagrams, and the list of palindromes. The format
of how this is done is shown in the included example text examples.
1. racecar-06.02.2020_17.03.06.txt
2. assessment-06.02.2020_17.05.00.txt
3. repaper-06.02.2020_17.11.03.txt
The function should create a new file for each search and process of activity A. The name
should be formed using the following format:
“User_word-month.day.year_hour.minute.second.txt”
The date and time used are from the time the file is created.
Figure 4 Full Activity A result display 1. Discussed in given code section.
9
Figure 5 Full Activity A result display 2. Discussed in given code section.
Figure 6 Full Activity A result display 3. Discussed in given code section.
10
Activity B
Figure 7 shows acceptable user input to trigger activity “B”. Activity B finds all the word
pairs in the dictionary list which form palingrams. The palingrams ignore spaces and
hyphens.
Figure 7 Acceptable input for triggering Activity B
Activity B uses the function find_palingrams(). For every word in the dictionary
list, the function should check if any other word(s) in the dictionary can be used to
form palingrams. Examples of palingrams are shown in the displays of figure 8 and figure
9. This function should compile a dictionary collection of the word pairs.
Once the collection of palingrams have been formed, the list should be displayed using
the print_pairs_of_twos()functions. The display should be as shown in figure
8 and figure 9.
There are 5960 word pairings (palingrams), when using the words.txt file including the
words “a” and “I”. Your code should be testable using this file or any other file with a
similar format.
The full collection should be written to file using the
write_palingrams_to_file() function. The file should be written or overwrite
the file dictionaryPalingrams.txt.
11
Figure 8 Display of results from Activity B start of display
Figure 9 Display of results from Activity B end of display
12
Activity C
Figure 10 shows acceptable user input to trigger activity “C”. Activity C finds all the
palindromes in the dictionary. A sample selection of the palindromes is shown in figure
10.
Figure 10 Sample of the display from Activity C
The application searches the entire dictionary file/list for palindromes and compiles a
list of palindromes. There are 91 palindromes in the file/list of dictionary words when
using the words.txt file including the words “a” and I”.
The application should display all the palindromes (as seen in figure 10). This should be
accomplished using the write_palingrams_to_file() function.
