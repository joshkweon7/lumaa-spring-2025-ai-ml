# AI/ML Challenge: Joshua Kweon

## Summary 

This program takes in a user's query regarding their preference for a novel and outputs five books from a dataset that most matches their desired novel summary 

## Steps to Set Up 

1. **Installations** 
- To install the required packages run `pip install pandas scikit-learn nltk` and after installing **nltk** download the resources for stopwords and tokenization using a script that runs `nltk.download('stopwords')` and `nltk.download('punkt')` 

2. **Load Data Set** 
- The book summary dataset that I used is titled booksummary.csv which is already read using the function **load_data** 

3. **Run Program** 
- To run the program, type in your terminal `python3 book_rec.py` or `python book_rec.py` 
- You will then be prompted to input the desired keywords that describe the books you would like recommended to you 
- Once your input is given, the program will output the recommended 5 books as well as the similarity score that was calculated in relation to your query! 

## Salary Expectation (Per Month) 
My salary expectation per month is ~$4,000

## Sample Demo 
https://github.com/user-attachments/assets/021d8866-679a-4306-830f-2fa911215d10
