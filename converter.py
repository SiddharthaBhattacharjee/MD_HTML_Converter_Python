import markdown
import os
import html2text
import glob
import time

def convert_md_to_html(filename):
    """Convert Markdown file to HTML"""
    with open(filename, 'r', encoding='utf-8') as f:
        md_string = f.read()
    html_string = markdown.markdown(md_string)

    # Change the file extension from .md to .html
    new_filename = os.path.splitext(filename)[0] + '.html'

    with open(new_filename, 'w', encoding='utf-8') as f:
        f.write(html_string)

    print(f"Converted {filename} to {new_filename}")


def convert_html_to_md(filename):
    """Convert HTML file to Markdown"""
    with open(filename, 'r', encoding='utf-8') as f:
        html_string = f.read()

    # Use html2text library to convert HTML to Markdown
    md_string = html2text.html2text(html_string)

    # Change the file extension from .html to .md
    new_filename = os.path.splitext(filename)[0] + '.md'

    with open(new_filename, 'w', encoding='utf-8') as f:
        f.write(md_string)

    print(f"Converted {filename} to {new_filename}")

if __name__ == "__main__":
   print("What Operation you want to perform ?\n1)MarkDown to HTML \n2) HTML to MarkDown \n")
   x = input("Choose option 1 or 2 :")
   if(x=='1'):
      # path to sample certificate
      mdfiles = glob.glob(os.path.join("./Files/", '*.md'))
      mdfiles_disp = [s.replace("./Files\\",'') for s in mdfiles ]
      print("List of available MD Files : ")
      for i,s in enumerate(mdfiles_disp):
         print(i,") ",s)
      fno = int(input("Enter the File number to be selected : "))
      filepath = f'./Files/{mdfiles_disp[fno]}'
      print("Selected: ",filepath)
      convert_md_to_html(filepath)
      time.sleep(5)
      print("Task Completed Successfully...")
      
   if(x=='2'):
      # path to sample certificate
      htmlfiles = glob.glob(os.path.join("./Files/", '*.html'))
      htmlfiles_disp = [s.replace("./Files\\",'') for s in htmlfiles ]
      print("List of available HTML Files : ")
      for i,s in enumerate(htmlfiles_disp):
         print(i,") ",s)
      fno = int(input("Enter the File number to be selected : "))
      filepath = f'./Files/{htmlfiles_disp[fno]}'
      print("Selected: ",filepath)
      convert_html_to_md(filepath)
      time.sleep(5)
      print("Task Completed Successfully...")
      
      
