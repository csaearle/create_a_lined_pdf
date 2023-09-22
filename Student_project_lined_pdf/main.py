from fpdf import FPDF

import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")

df = pd.read_csv("topics.csv", sep=",")

lines_x1 = 10
lines_x2 = 200
line_y1 = 21
line_y2 = 21

for index, row in df.iterrows():
    pdf.add_page()

    # set up the header from topics.csv file
    pdf.set_font(family="Times", style="B", size=14)
    pdf.set_text_color(250, 100, 50)
    pdf.cell(txt=row["Topic"], align="L", w=0, h=14, ln=1)

    # Draw a line under the header
    pdf.line(lines_x1, line_y1, lines_x2, line_y2)

    #  Draw multiple lines under the header of first page

    for lines_vertical_p1 in range(line_y1, 270, 10):
        print(lines_vertical_p1)
        pdf.line(lines_x1, lines_vertical_p1, lines_x2, lines_vertical_p1)

    # Write in the footer on first page of each Topic
    pdf.ln(241)
    pdf.set_font(family="Times", style="I", size=10)
    pdf.set_text_color(50, 100, 255)
    pdf.cell(txt=row["Topic"], align='R', w=0, h=10, ln=1)




    for pages in range(row["Pages"] - 1):
        pdf.add_page()
        pdf.set_font(family="Times", style="B", size=14)
        pdf.set_text_color(250, 100, 50)
        pdf.cell(txt=row["Topic"], align="L", w=0, h=14, ln=1)

        # Draw a line under the header of subsequent pages
        pdf.line(lines_x1, line_y1, lines_x2, line_y2)

        # Draw the lines of 10mm apart from first line down to footer vertically
        for lines_vertical in range(line_y1, 270, 10):
            print(lines_vertical)
            pdf.line(lines_x1, lines_vertical, lines_x2, lines_vertical)

        # Write the footer under the multiple lines
        pdf.ln(241)
        pdf.set_font(family="Times", style="I", size=10)
        pdf.set_text_color(50, 100, 255)
        pdf.cell(txt=row["Topic"], align='R', w=0, h=10, ln=1)

    # print(pages)

# print out the pdf file, as formatted
pdf.output("student_output.pdf")





