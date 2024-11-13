import pandas as pd
import os
import subprocess


try:
    df = pd.read_csv("result.csv", sep=";", encoding="utf-8")
except FileNotFoundError:
    print("Error: 'result.csv' file not found.")
    exit()


try:
    with open("template.tex", "r", encoding="utf-8") as file:
        template = file.read()
except FileNotFoundError:
    print("Error: 'template.tex' file not found.")
    exit()


output_dir = "Lettres"
os.makedirs(output_dir, exist_ok=True)


def escape_latex_characters(text):
    special_chars = {
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
        "\\": r"\textbackslash{}",
    }
    for char, escape in special_chars.items():
        text = text.replace(char, escape)
    return text



def replace_accents(text):
    accents = {
        "é": r"\'e",
        "è": r"\`e",
        "ê": r"\^e",
        "ë": r"\"e",
        "à": r"\`a",
        "â": r"\^a",
        "ç": r"\c{c}",
        "î": r"\^i",
        "ï": r"\"i",
        "ô": r"\^o",
        "ù": r"\`u",
        "û": r"\^u",
        "ü": r"\"u",
    }
    for char, latex_code in accents.items():
        text = text.replace(char, latex_code)
    return text



for index, row in df.iterrows():
    entreprise = replace_accents(escape_latex_characters(str(row["ENTREPRISE"])))
    adresse = replace_accents(escape_latex_characters(str(row["ADRESS"])))

    
    latex_content = template.replace("{entreprise}", entreprise).replace(
        "{adresse}", adresse
    )

    
    tex_filename = f"{entreprise.replace(' ', '_')}.tex"
    with open(tex_filename, "w", encoding="utf-8") as tex_file:
        tex_file.write(latex_content)


   
    pdf_filename = os.path.join(
        output_dir, f"{entreprise.replace(' ', '_')}.pdf"
    )
    try:
        print(f"Compiling {tex_filename} to PDF...")
        subprocess.run(
            [
                "C:/Users/ANASS/AppData/Local/Programs/MiKTeX/miktex/bin/x64/pdflatex",
                tex_filename,
                "-output-directory",
                output_dir,
            ],
            check=True,
        )
        print(f"Generated PDF: {pdf_filename}")
    except subprocess.CalledProcessError as e:
        print(f"Error compiling {tex_filename}: {e}")

    # Remove the .tex file after generating the PDF
    try:
        os.remove(tex_filename)
        print(f"Removed temporary file: {tex_filename}")
    except FileNotFoundError:
        print(f"File not found for removal: {tex_filename}")


for root, dirs, files in os.walk(output_dir):
    for file in files:
        if file.endswith((".aux", ".log")):
            try:
                os.remove(os.path.join(root, file))
                print(f"Removed auxiliary file: {file}")
            except FileNotFoundError:
                pass  # Ignore if the file doesn't exist

print("PDF letters generated successfully in the 'lettres' folder!")
