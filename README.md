# PDFPasswordBreaker

Say you have an encrypted PDF that you have forgotten the password to,
but you remember it was a single English word. Trying to guess your forgotten password is quite a boring task. Instead you can write a program that will
decrypt the PDF by trying every possible English word until it finds one
that works. This is called a brute-force password attack. Download the text file
dictionary.txt from http://nostarch.com/automatestuff/. This dictionary file contains over 44,000 English words with one word per line.
Using the file-reading skills you learned in Chapter 8, create a list of
word strings by reading this file. Then loop over each word in this list, passing
it to the decrypt() method. If this method returns the integer 0, the password was wrong and your program should continue to the next password.
If decrypt() returns 1, then your program should break out of the loop and
print the hacked password. You should try both the uppercase and lowercase form of each word.
