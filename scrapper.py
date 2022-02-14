# github_data_download = "https://github.com/IBM/nlc-email-phishing/blob/master/data/Email-trainingdata-20k.csv"
# link2 = "https://www.kaggle.com/pramodgupta92/fraud-email-datasets"

from turtle import down
from bs4 import BeautifulSoup
import pandas as pd
import opendatasets as od


GITHUB_FILE_NAME = "Github_nlc_email_phishing.csv"
KAGGLE_FILE_NAME = "kaggle_email_phishing.csv"
KAGGLE_DATASET_URL = "https://www.kaggle.com/pramodgupta92/fraud-email-datasets"
    

def download_github_email_phishing_csv():
    with open('nlc-email-phishing_Email-trainingdata-20k.csv at master · IBM_nlc-email-phishing · GitHub.html', 'r') as html_file:
        content = html_file.read()
        soup = BeautifulSoup(content, 'lxml')

        div_tags = soup.find_all('div', class_ = "BtnGroup")
        stmt = ""
        for tag in div_tags:
            stmt = tag.a['href']
            if 'csv' in stmt:
                print(stmt)
                break

        if stmt == "":
            print("Download link not found")
        else:
            df = pd.read_csv(stmt)
            df.to_csv(GITHUB_FILE_NAME)


def download_kaggle_email_phishing_csv():
    od.download(KAGGLE_DATASET_URL)




try:
    print("===============GITHUB DATA DOWNLOADING========================")
    download_github_email_phishing_csv()
except Exception as e:
    print(f"Exception raised during downloading of Github Data")
    print(e)

try:
    print("===============KAGGLE DATA DOWNLOADING========================")
    download_kaggle_email_phishing_csv()
except Exception as e:
    print(f"Exception raised during downloading of Kaggle Data")
    print(e)
    

