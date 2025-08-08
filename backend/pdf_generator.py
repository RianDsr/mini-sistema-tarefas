from reportlab.pdfgen import canvas

def generate_tasks_pdf(tasks, filename='tasks.pdf'):
    c = canvas.Canvas(filename)
    y = 800
    for task in tasks:
        c.drawString(50, y, f"{task['title']}: {task['description']}")
        y -= 20
    c.save()
    return filename