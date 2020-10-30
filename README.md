# Inspiration
I am a third year student, studying computer engineering.
One day when I was pretty bored becauce I didn't have internet, I decided to 
create a module in python (because i think i have better understanding of it as a PL as of others)
named MatrixShell designed to store matrices and do basic operations on them
like find the determinant and multiply etc etc.

This project is designed to meerely be a glimpse that I want to take in the programming world,
and help me understand how GitHub works, while I continue to perfect my skills in Python.

# How to use
1. Clone the repository (download the code in your computer)
2. Open a Python IDE (preferably PyCharm) and navigate to repositery folder
3. There are 3 modes of creating a new MatrixShell object using a python console:
    1. x = MatrixShell()
        - Prompts the user to: *enter matrix as you would with python lists; i.e. [[1,2],[1, 2]]:*
    2. x = MatrixShell(2,3) (where 2 and 3 are the dimensions of the matrix)
        - Prompts the user to: *Enter the elements separated by a single comma:*
        - this is done because we have a defined size which in this example is 2 rows and 3 columns
        - if you enter more or less than 6 elements it returns an error
        - elements entered are ordered cronoligacally
    3. x = MatrixShell(2, 4, 1)
        - this is used in case of multiplication and is useful if you have a predefined python list in form of a matrix like: m = [[1,2],[1, 2]]
        - then you can say x.matrix = m and use all MatrixShell functions on this list (like finding the determinant)
 4. Have fun!!!
    

## 01-Oct-20 Update
Added cramers and random_i to MatrixShell: the first function solves linear systems of equations 
given the MatrixShell A and the vector [x1, x2, x3,...], the second function creates randomized 
squared MatrixShells with integer elements from a given range.
Added 2 new files that analyse certain aspects like determinant frequency and solving time using 
cramers and the inverse of a MatrixShell

## 22-Oct-20 Update
I will call this matrix project officially closed, if anyone would be interested to continue it 
here are some ideas as of what to do next:
1. define a new function that does a gauss-jordan elemination and returns a MatrixShell object
2. convert all of the code or parts of it (determinant) into julia language code so it is faster
