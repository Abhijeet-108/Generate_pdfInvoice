import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepath = glob.glob("invoice/*.xlsx")

for filepath in filepath:
    df = pd.read_excel(filepath,sheet_name="Sheet 1")

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    filename = Path(filepath).stem
    Invoice_nr,date = filename.split("-")

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=58, h=8, txt=f"Invoice nr.{Invoice_nr}", ln=1)

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=58, h=8, txt=f"Date: {date}",ln=1)


    pdf.output(f"PDFs/{filename}.pdf")


