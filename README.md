
# Bank_OCR

A program that scans account numbers from ASCII files.
The ASCII files contain numbers that each are encoded on three lines. The following picture shows how the digits 1234567890 are encoded in the file.

![Example](/images/sample1.png)

Each digit is three characters wide and three characters high. Consecutive digits are delimited by spaces. An empty line delimits consecutive rows with numbers. Each digit is build from „_“ (underscore) and „I“ (uppercase letter I).


# Usage
The program is started with a file name as a parameter. It prints the recognized numbers on the console. Please note that the input file is considered well formed. There are no errors in the input files.(you can use sample file)
```sh
$ python3 bankocr.py FILENAME
```

Files my contain errors. Although the structure of the rows is correct: three rows build one number, a blank line delimits multiple numbers. The structure of the digits is correct too, so each digit consists of a 3 x 3 matrix of characters. But the characters inside the 3 x 3 matrix may not be valid. There may be illegal characters and there may be characters at an illegal position. Each number that could not be recognized because of such errors should be printed as „Error in data“.

Sample of data: [sample.txt](sample.txt)

```sh
$ python3 bankocr.py sample.txt
Error in data
490067715
```