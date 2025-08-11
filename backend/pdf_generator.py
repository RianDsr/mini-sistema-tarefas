import io
from fpdf import FPDF

def gerar_pdf(tarefas):
    pdf = FPDF()
    pdf.add_page()
    
    # Título do PDF
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 10, 'Relatório de Tarefas', ln=True, align='C')
    pdf.ln(10)
    
    # Cabeçalhos da tabela
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(60, 10, 'Título', 1)
    pdf.cell(130, 10, 'Descrição', 1, ln=True)

    # Dados das tarefas
    pdf.set_font('Arial', '', 12)
    for tarefa in tarefas:
        # Primeira célula
        pdf.multi_cell(60, 10, tarefa.title.encode('latin-1', 'replace').decode('latin-1'), border=1)
        # Segunda célula (mesma linha)
        y_pos = pdf.get_y()
        pdf.set_xy(70, y_pos - 10)
        pdf.multi_cell(130, 10, tarefa.description.encode('latin-1', 'replace').decode('latin-1'), border=1)

    # Criar buffer de memória
    pdf_buffer = io.BytesIO(pdf.output(dest='S').encode('latin-1'))
    pdf_buffer.seek(0)  # Garante que o ponteiro está no início
    
    return pdf_buffer  # Somente o PDF em memória

            
            