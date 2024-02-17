import pdfkit
import concurrent.futures


def convert_to_pdf(i):
    try:
        pdfkit.from_url('https://tilshunos.com/paronims/?page=' + str(i),
                        "C:\\Users\\hp\\Documents\\Najot talim\\Python_Advanced\\L_6\\hw_M5_L6\\" + str(i) + '.pdf',
                        configuration=config)
        print(f"PDF generated successfully for {i}")
    except Exception as e:
        print(f"Error converting URL {i} to PDF: {e}")

path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(convert_to_pdf, range(1, 11))