from xhtml2pdf import pisa
from io import BytesIO
from string import Template

def create_pdf(summary_data):
    html_template = open("templates/report_template.html").read()
    html = Template(html_template).substitute(
        total=summary_data['Total Sales'],
        average=summary_data['Average Sales'],
        max=summary_data['Max Sale'],
        min=summary_data['Min Sale']
    )

    result = BytesIO()
    pisa.CreatePDF(BytesIO(html.encode("utf-8")), dest=result)
    return result.getvalue()