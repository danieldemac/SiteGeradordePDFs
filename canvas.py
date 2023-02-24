from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader
import streamlit as st
import base64


st.title("CERTIDÃO de nada consta (FALÊNCIA, CONCORDATA ou RECUPERAÇÃO FISCAL)")
st.image("http://www.tjpe.jus.br/documents/10180/654750/Bras%C3%A3o+TJPE/56a35c62-9a39-4167-a2b0-c9efe8f21597?t=1409253878399")
nomeEmpresa = st.text_input("Nome da Empresa: ")
cnpj = st.text_input("CNPJ? (Sem pontos e traços) :")
if st.button("Gerar Certidão"):
    # cria o canvas
    pdf = canvas.Canvas("certidao.pdf")
    # registra a fonte negrito
    pdfmetrics.registerFont(TTFont('negrito', 'C:\\Windows\\Fonts\\arialbd.ttf'))

    # Parte Superior
    pdf.setFont("Helvetica-Bold", 9)
    pdf.drawString(400, 800, "Fórum da Comarca de Palmares-PE")
    pdf.drawString(400, 790, "Distribuidor Judicial e seus anexos")
    pdf.setFont("Helvetica-Bold", 8)
    pdf.drawString(350, 780, "Progeforo | Contadoria | Partidoria | Depósito Judicial")
    imagem = ImageReader("C:/Users/arant/PycharmProjects/PDFramon/teste.png")
    pdf.drawImage(imagem, 70, 760, width=210, height=70)
    # adiciona o título
    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(250, 650, "CERTIDÃO")

    # adiciona o parágrafo
    pdf.setFont("Helvetica-Bold", 11)

    pdf.drawString(200, 580, "CERTIFICO ")
    largura_texto = pdf.stringWidth("CERTIFICO ")
    pdf.setFont("Helvetica", 11)
    pdf.drawString(200 + largura_texto, 580, "que, em consulta ao sistema de controle processual")

    pdf.drawString(70, 560, "desta Comarca (Judwin), verifiquei ")
    largura_texto = pdf.stringWidth("desta Comarca (Judwin), verifiquei ")
    pdf.setFont("Helvetica-Bold", 11)
    pdf.drawString(70 + largura_texto, 560, "NÃO CONSTAR ações de FALÊNCIA, CONCORDATA")

    pdf.drawString(70, 540, "ou RECUPERAÇÃO FISCAL")
    largura_texto = pdf.stringWidth("ou RECUPERAÇÃO FISCAL")
    pdf.setFont("Helvetica", 11)
    pdf.drawString(70 + largura_texto, 540, " tramitando fisicamente contra a empresa:")

    pdf.setFont("Helvetica-Bold", 11)

    tamanho_empresa = pdf.stringWidth(nomeEmpresa)
    pdf.setFillColorRGB(0.8, 0.8, 0.8)
    pdf.rect(249, 520, tamanho_empresa + 1, 15, fill=True, stroke=False)
    pdf.setFillColorRGB(0, 0, 0)
    pdf.drawString(250, 525, nomeEmpresa)

    pdf.setFont("Helvetica", 11)

    pdf.drawString(70, 500, "inscrita no ")
    largura_texto = pdf.stringWidth("inscrita no ")
    pdf.setFont("Helvetica-Bold", 11)
    pdf.drawString(70 + largura_texto, 500, "CNPJ sob o nº:")

    tamanho_cnpj = pdf.stringWidth(cnpj)
    pdf.setFillColorRGB(0.8, 0.8, 0.8)
    pdf.rect(249, 480, tamanho_cnpj + 1, 15, fill=True, stroke=False)
    pdf.setFillColorRGB(0, 0, 0)
    pdf.drawString(250, 480, cnpj)

    pdf.drawString(200, 460, "CERTIFICO ")
    largura_texto = pdf.stringWidth("CERTIFICO ")
    pdf.setFont("Helvetica", 11)
    pdf.drawString(200 + largura_texto, 460, ", ainda, que ")
    largura_texto = pdf.stringWidth("CERTIFICO, ainda, que ")
    pdf.setFont("Helvetica-Bold", 11)
    pdf.drawString(200 + largura_texto, 460, "  esta  certidão  é  válida  apenas  para")

    pdf.drawString(70, 440, "processos físicos em tramitação na comarca de Palmares")
    pdf.setFont("Helvetica", 11)
    largura_texto = pdf.stringWidth("processos físicos em tramitação na comarca de Palmares   ")
    pdf.drawString(70 + largura_texto, 440, "    , devendo as certidões relativas")

    pdf.drawString(70, 420,
                   "a processos eletrônicos (PJe) ser emitidas pelo interessado, a partir do formulário disponível no")

    pdf.drawString(70, 400, " portal do pje.tjpe.jus.br.")

    pdf.drawString(70, 380, "")

    pdf.drawString(70, 360, "")

    pdf.drawString(200, 320, "O referido é verdade; dou fé.")

    pdf.drawString(200, 300, "Palmares, 16 de fevereiro de 2023.")
    largura_texto = pdf.stringWidth("Palmares, 16 de")
    imagem = ImageReader("C:/Users/arant/PycharmProjects/PDFramon/teste2.png")
    pdf.drawImage(imagem, 200 + largura_texto, 220, width=70, height=70)

    pdf.drawString(220, 200, "Ramon Sobral de Andrade Silva")

    pdf.drawString(250, 180, "Distribuidor e anexos")

    pdf.drawString(250, 160, "Matrícula 178.726-8")
    # Final 1
    pdf.setFont("Helvetica-Bold", 6)
    pdf.drawString(50, 20,
                   "Loteamento Dom Acácio Rodrigues Alves, Bairro Quilombo II, Palmares, PE - CEP: 55.540-000 - Fone: (081) 3662-0150/0168 Fax: 3662-0176 -– Expediente: 9:00 às 18:00 h")
    pdf.drawString(49, 20,
                   "__________________________________________________________________________________________________________________________________________________")

    pdf.showPage()

    # Parte Superior
    pdf.setFont("Helvetica-Bold", 9)
    pdf.drawString(400, 800, "Fórum da Comarca de Palmares-PE")
    pdf.drawString(400, 790, "Distribuidor Judicial e seus anexos")
    pdf.setFont("Helvetica-Bold", 8)
    pdf.drawString(350, 780, "Progeforo | Contadoria | Partidoria | Depósito Judicial")
    imagem = ImageReader("C:/Users/arant/PycharmProjects/PDFramon/teste.png")
    pdf.drawImage(imagem, 70, 760, width=210, height=70)

    # Adiciona o título
    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(270, 700, "CERTIDÃO")

    # Parágrafo
    pdf.setFont("Helvetica-Bold", 11)
    pdf.drawString(175, 660, "       CERTIFICO, atendendo pedido de: " + nomeEmpresa)
    pdf.drawString(85, 640, "Sob CNPJ nº:" + cnpj + ", para fins de direito, que, além deste Cartório Distribuidor")
    pdf.drawString(85, 620, "Judicial, sob a responsabilidade do servidor Ramon Sobral de Andrade Silva,   matrícula")
    pdf.drawString(85, 600, "178.726-8;")
    largura_texto = pdf.stringWidth("178.726-8;")
    pdf.setFont("Helvetica-Bold", 10)
    pdf.drawString(85 + largura_texto, 600,
                   " existem neste Município e Comarca de Palmares os Ofícios a seguir relacionados:")
    # Imagem3
    imagem = ImageReader("C:/Users/arant/PycharmProjects/PDFramon/teste3.png")
    pdf.drawImage(imagem, 85, 320, width=450, height=260)

    pdf.setFont("Helvetica-Bold", 8)
    pdf.drawString(85, 280,
                   "Tudo conforme dados disponíveis no portal Justiça Aberta do CNJ (https://www.cnj.jus.br/corregedoria/justica_aberta),")
    pdf.drawString(85, 260, "em consulta realizada nesta data.")

    pdf.setFont("Helvetica-Bold", 9)
    pdf.drawString(200, 240, "O referido é verdade; dou fé.")
    pdf.drawString(200, 220, "Palmares, 16 de fevereiro de 2023.")
    largura_texto = pdf.stringWidth("Palmares, 16 de")
    imagem = ImageReader("C:/Users/arant/PycharmProjects/PDFramon/teste2.png")
    pdf.drawImage(imagem, 200 + largura_texto, 140, width=70, height=70)
    pdf.drawString(220, 120, "Ramon Sobral de Andrade Silva")
    pdf.drawString(250, 100, "Distribuidor e anexos")
    pdf.drawString(250, 80, "Matrícula 178.726-8")

    # Final 2
    pdf.setFont("Helvetica-Bold", 6)
    pdf.drawString(50, 20,
                   "Loteamento Dom Acácio Rodrigues Alves, Bairro Quilombo II, Palmares, PE - CEP: 55.540-000 - Fone: (081) 3662-0150/0168 Fax: 3662-0176 -– Expediente: 9:00 às 18:00 h")
    pdf.drawString(49, 20,
                   "__________________________________________________________________________________________________________________________________________________")

    pdf.showPage()
    pdf.save()
    with open("certidao.pdf", "rb") as pdf_file:
        b64 = base64.b64encode(pdf_file.read()).decode('utf-8')
        href = f'<a href="data:application/octet-stream;base64,{b64}" download="certidao.pdf">Download da Certidão</a>'
        st.markdown(href, unsafe_allow_html=True)


