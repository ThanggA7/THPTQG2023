import csv
import json
import requests

def crawl_data():
    start_sbd = 1000001
    end_sbd = 64006937

    with open('data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for sbd in range(start_sbd, end_sbd + 1):
            try:
                url = f"https://dantri.com.vn/thpt/1/0/99/{sbd}/2023/0.2/search-gradle.htm"
                response = requests.get(url)

                if response.status_code == 200:
                    json_data = response.json()

                    if json_data:
                        student_data = json_data["student"]

                        # Export data to CSV
                        row_data = [
                            student_data.get('sbd'),
                            student_data.get('toan'),
                            student_data.get('van'),
                            student_data.get('ngoaiNgu'),
                            student_data.get('vatLy'),
                            student_data.get('hoaHoc'),
                            student_data.get('sinhHoc'),
                            student_data.get('diemTBTuNhien'),
                            student_data.get('lichSu'),
                            student_data.get('diaLy'),
                            student_data.get('gdcd'),
                            student_data.get('diemTBXaHoi')
                        ]
                        writer.writerow(row_data)

                        print(f"[CRAWL] {sbd} thành công")

                if sbd == end_sbd:
                    print("Data crawling and export complete.")

            except Exception as e:
                print(f"[CRAWL] {sbd} không thành công")
                print(f"[CRAWL] {sbd} không thành công")

crawl_data()
