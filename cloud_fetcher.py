import requests
url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=NM_007294.4&rettype=fasta&retmode=text"
response = requests.get(url)
if response.status_code == 200: 
    with open("brca1_fetched.fasta", "w") as file:
        file.write(response.text)
    print("Download complete: brca1_fetched.fasta saved.")
else:
    print("Request failed with status code {response.status_code}")