![GitHub release (latest by date)](https://img.shields.io/github/v/release/christopher-pedraza/excel-parser)
![GitHub Release Date](https://img.shields.io/github/release-date/christopher-pedraza/excel-parser?color=c77546)

# excel-parser
Lets you create custom strings based on the data of an .xlsx file (Microsoft Excel Worksheet)

## How to use
1. Download the compressed file that contains the program and needed configuration files from [Releases](https://github.com/christopher-pedraza/excel-parser/releases/latest/download/excel-parser.zip).
2. Extract it anywhere you want (bear in mind that it contains multiple folders and files, so you may prefer extracting it in a separate folder).
3. Add the location of the input, template and output files in **_files.txt_**.
    * The text files' names should have the prefix of the type of file followed by an underscore. If it is an input file (input_filename.txt), a template file (template_filename.txt) and an output file (output_filename.txt).
    * It's important to first write the names concerning input files, then template files, and finally output files, each in their separate line.
    * Also, you need to write the template and output files in the same order as the input files (e.g. if the first input files are input_a.txt and then input_b.txt, the template files need to be template_a.txt and then template_b.txt, and the output files output_a.txt and then output_b.txt).
4. Add the data from the .xlsx files into the input files that you defined in **_files.txt_**.
    * To convert a .xlsx file into a text file, you can either copy and paste the data into the text file (it will automatically separate the columns with tabs and will place each row in a separate line), or save the .xlsx as a .txt.
5. Create the template strings for each input file in the templates files.
    * The template needs to follow an specific format: 
        ```
        "You can write whatever you want here '{col1}' and {col2}".format(col1=val["col1"], col2=val["col2"])
        ```
        * Notice that it follows python's `format()` string syntaxis, as it is going to `eval()` whatever you write there and replace the variables with the data of an atribute of the .xlsx. You can read a simple guide on python's `format()` [here](https://www.w3schools.com/python/ref_string_format.asp).
        * Another important thing to consider is that the list `val` needs to have that name, as it is the name it has in the code.
        * Also, the key that is provided to the list needs to be the same as one of the headers of the input .xlsx, only that any spaces are changed into underscores and all the letters transformed into lowercase.
        * As you can see, the left part of the template is enclosed by double quotation marks. They are essential, however, you can also use single quotation marks. Whether you use one or the other depends on whether you are going to use one of them inside the text. If you use double quotation marks to enclose, you can only use single inside, and viceversa. In the example, I'm enclosing the text with double quotation marks and the variable `col1` with single.
        * Each variable needs to be enclosed by curly braces (e.g. `{varName}`).
        * Also, you can include as many template strings as you want, just add each in a separate line.
6. Finally, when everything is configured, you may run `parser.exe` and see the resulting strings in the output files you defined earlier (step 3).
