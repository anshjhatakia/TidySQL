SQL Formatting Algorithm

1. Start with unformatted SQL code
2. Place newline reserved words in a set
3. Place all reserved words in a set
4. Divide up the unformatted SQL code into a list of words
5. If the word is select, increment the select counter and print out select
6. If the word is not select, then print the word like normal in the same line
7. Check the word for a comma.
    - If there is a comma, check if the comma is in the beginning or the end. Split the line by the comma so that the first line ends with the comma
      and the new line starts at the first character after the comma.