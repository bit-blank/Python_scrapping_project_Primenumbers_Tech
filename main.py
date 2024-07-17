from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

chrome_options = Options()
chrome_options.add_argument("--headless")  
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")


chrome_service = ChromeService(executable_path='C:\\Users\\PRAKHAR\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')


driver = webdriver.Chrome(service=chrome_service, options=chrome_options)


url = 'https://hprera.nic.in/PublicDashboard/GetFilteredProjectsPV?DistrictList%5B0%5D.Selected=false&DistrictList%5B0%5D.Value=18&DistrictList%5B1%5D.Selected=false&DistrictList%5B1%5D.Value=24&DistrictList%5B2%5D.Selected=false&DistrictList%5B2%5D.Value=20&DistrictList%5B3%5D.Selected=false&DistrictList%5B3%5D.Value=23&DistrictList%5B4%5D.Selected=false&DistrictList%5B4%5D.Value=25&DistrictList%5B5%5D.Selected=false&DistrictList%5B5%5D.Value=22&DistrictList%5B6%5D.Selected=false&DistrictList%5B6%5D.Value=26&DistrictList%5B7%5D.Selected=false&DistrictList%5B7%5D.Value=21&DistrictList%5B8%5D.Selected=false&DistrictList%5B8%5D.Value=15&DistrictList%5B9%5D.Selected=false&DistrictList%5B9%5D.Value=17&DistrictList%5B10%5D.Selected=false&DistrictList%5B10%5D.Value=16&DistrictList%5B11%5D.Selected=false&DistrictList%5B11%5D.Value=19&PlottedTypeList%5B0%5D.Selected=false&PlottedTypeList%5B0%5D.Value=P&PlottedTypeList%5B1%5D.Selected=false&PlottedTypeList%5B1%5D.Value=F&PlottedTypeList%5B2%5D.Selected=false&PlottedTypeList%5B2%5D.Value=M&ResidentialTypeList%5B0%5D.Selected=false&ResidentialTypeList%5B0%5D.Value=R&ResidentialTypeList%5B1%5D.Selected=false&ResidentialTypeList%5B1%5D.Value=C&ResidentialTypeList%5B2%5D.Selected=false&ResidentialTypeList%5B2%5D.Value=M&AreaFrom=&AreaUpto=&SearchText='
driver.get(url)
for i in range (10):
    time.sleep(1)
    print(i)  

qs_list = driver.execute_script("""
    return Array.from(document.getElementsByTagName('a'))
                .filter(x => !!x.title)
                .map(x => x.getAttribute('data-qs'));
""")

project_details = []

for qs in qs_list[:6]:
    detail_url = f'https://hprera.nic.in/Project/ProjectRegistration/PromotorDetails_PreviewPV?qs={qs}'
    driver.get(detail_url)
    time.sleep(2) 

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    name_element = soup.find('td', string='Name')
    name = name_element.find_next_sibling('td').text.strip() if name_element else 'N/A'
    
    pan_element = soup.find('td', string='PAN No.')
    pan_no = pan_element.find_next_sibling('td').text.strip() if pan_element else 'N/A'
    
    gst_element = soup.find('td', string='GSTIN No.')
    gst_no = gst_element.find_next_sibling('td').text.strip() if gst_element else 'N/A'
    
    p_add_element = soup.find('td', string='Permanent Address')
    p_add = p_add_element.find_next_sibling('td').text.strip() if p_add_element else 'N/A'
    
    project_details.append({
        'Name': name,
        'PAN No.': pan_no,
        'GSTIN No.': gst_no,
        'Permanent Address': p_add
    })

driver.quit()

for idx, details in enumerate(project_details, 1):
    print(f"Project {idx}:")
    print(f"Name: {details['Name']}")
    print(f"PAN No.: {details['PAN No.']}")
    print(f"GSTIN No.: {details['GSTIN No.']}")
    print(f"Permanent Address: {details['Permanent Address']}")
    print('-' * 20)
