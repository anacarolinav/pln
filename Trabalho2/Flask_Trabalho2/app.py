from flask import Flask, render_template, request, redirect, url_for, send_file
import json
from werkzeug.utils import secure_filename
import os, re, subprocess
import xml.etree.ElementTree as ET

app = Flask(__name__)
app.static_folder = 'static'

# CAMINHO PARA A PASTA uploads
app.config["UPLOAD_FOLDER"] = os.path.join(os.getcwd(), "Flask_Trabalho2/uploads")

# CAMINHO PARA A PASTA xml_files
app.config["XML_FOLDER"] = "Flask_Trabalho2/xml_files"
app.config["ALLOWED_EXTENSIONS"] = {"pdf"}

file = open("ordenado_wikit1_traducoes.json")
db = json.load(file)
file1 = open("doencas-MDSaude.json")
db1 = json.load(file1)


#########################################
# FUNCOES GERAIS
# Função para verificar a extensão do arquivo permitida
def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in app.config["ALLOWED_EXTENSIONS"]

#limpeza
def clean(text):
    text = re.sub(r"\s+", " ", text)  # Remove \n, tab, multiple spaces
    return text.strip()  # Remove leading and trailing spaces


# Função para converter o arquivo PDF em XML
def convert_to_xml(pdf_path, xml_path):
    # Comando para converter o PDF em XML usando a biblioteca pdf2xml
    command = f"pdftohtml -xml  {pdf_path} {xml_path}"
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Erro ao converter o arquivo PDF em XML: {e}")


#########################################

@app.route("/")
def home():
    return render_template("homeVERSAO2.html", title="Multilingual Medical Dictionary")



#########################################
@app.route("/homePT")
def homePT():
    return render_template("homePT.html", title="Menu - PT - EN - ES", descriptions=db.keys())

@app.route("/homeING")
def homeING():
    return render_template("homeING.html", title="Home - EN - PT - ES", descriptions=db.keys())

@app.route("/homeESP")
def homeESP():
    return render_template("homeESP.html", title="Inicio - ES - PT - EN", descriptions=db.keys())

#########################################


@app.route("/table")
def tableING():
    return render_template("tableING.html", matched=db.items())

@app.route("/tabela")
def tablePT():
    return render_template("tablePT.html", matched=db.items())

@app.route("/tabele")
def tableESP():
    return render_template("tableESP.html", matched=db.items())

#########################################

@app.route('/termos/procura')
def search_termPT():
    term = request.args.get('search-box')
    result = db.get(term)
    return render_template('searchPT.html', title="Dicionário - Dictionary - Diccionario", result=result, term=term)

@app.route('/terms/search')
def search_termING():
    term = request.args.get('search-box')
    result = db.get(term)
    return render_template('searchING.html', title="Dictionary - Dicionário - Diccionario", result=result, term=term)

@app.route('/terminos/buscar')
def search_termESP():
    term = request.args.get('search-box')
    result = db.get(term)
    return render_template('searchESP.html', title="Diccionario - Dicionário - Dictionary", result=result, term=term)


#########################################

@app.route("/terms")
def terms_ing():
    return render_template("termsING.html",title="Termos médicos (PT - EN - ES)", descriptions=db.keys())

@app.route("/termos")
def terms_pt():
    return render_template("termsPT.html",title="Termos médicos (PT - EN - ES)", descriptions=db.keys())

@app.route("/terminos")
def terms_esp():
    return render_template("termsESP.html",title="Termos médicos (PT - EN - ES)", descriptions=db.keys())

#########################################




@app.route("/term/<t>")
def term(t):
    return render_template("termING.html", description=t, value=db.get(t, "None"))

@app.route("/termo/<t>")
def termo(t):
    return render_template("termPT.html", description=t, value=db.get(t, "None"))

@app.route("/terminos/<t>")
def termi(t):
    return render_template("termESP.html", description=t, value=db.get(t, "None"))

#########################################

@app.route("/termo", methods=["POST"])
def adicionar_termo():
    term = request.form["term"]
    description = request.form["description"]
    english = request.form["english"]  # Novo campo para o inglês
    spanish = request.form["spanish"]  # Novo campo para o espanhol

    db[term] = {
        "descricao": description,
        "ingles": english,  # Adiciona a tradução em inglês ao dicionário do termo
        "espanhol": spanish  # Adiciona a tradução em espanhol ao dicionário do termo
    }

    file = open('ordenado_wikit1_traducoes.json', "w")
    json.dump(db, file, ensure_ascii=False, indent=4)
    file.close()
    
    if term not in db:
        return render_template("termsPT.html", descriptions=db.keys(),
                               info="O termo " + term + " foi adicionado!")

    else:
        return render_template("termsPT.html", descriptions=db.keys(),
                               info="O termo " + term + " foi atualizado!")
    
@app.route("/term", methods=["POST"])
def add_term():
    term = request.form["term"]
    description = request.form["description"]
    english = request.form["english"]  # Novo campo para o inglês
    spanish = request.form["spanish"]  # Novo campo para o espanhol

    db[term] = {
        "descricao": description,
        "ingles": english,  # Adiciona a tradução em inglês ao dicionário do termo
        "espanhol": spanish  # Adiciona a tradução em espanhol ao dicionário do termo
    }

    file = open('ordenado_wikit1_traducoes.json', "w")
    json.dump(db, file, ensure_ascii=False, indent=4)
    file.close()
    
    if term not in db:
        return render_template("termsING.html", descriptions=db.keys(),
                               info="The term " + term + " was added!")

    else:
        return render_template("termsING.html", descriptions=db.keys(),
                               info="The term " + term + " was updated!")
    
@app.route("/terminos", methods=["POST"])
def add_terminos():
    term = request.form["term"]
    description = request.form["description"]
    english = request.form["english"]  # Novo campo para o inglês
    spanish = request.form["spanish"]  # Novo campo para o espanhol

    db[term] = {
        "descricao": description,
        "ingles": english,  # Adiciona a tradução em inglês ao dicionário do termo
        "espanhol": spanish  # Adiciona a tradução em espanhol ao dicionário do termo
    }

    file = open('ordenado_wikit1_traducoes.json', "w")
    json.dump(db, file, ensure_ascii=False, indent=4)
    file.close()
    
    if term not in db:
        return render_template("termsESP.html", descriptions=db.keys(),
                               info="El término  " + term + " fue añadido!")

    else:
        return render_template("termsESP.html", descriptions=db.keys(),
                               info="El término  " + term + " fue actualizado!")


#########################################

@app.route("/term/<description>", methods=["DELETE"])
def delete_term(description):
    descricao = db[description]
    if description in db:
        del db[description]
    
    file = open('ordenado_wikit1_traducoes.json', "w")
    json.dump(db, file, ensure_ascii=False, indent=4)
    file.close()
    
    return {description: {"description": descricao}}

@app.route("/termo/<description>", methods=["DELETE"])
def delete_termo(description):
    descricao = db[description]
    if description in db:
        del db[description]
    
    file = open('ordenado_wikit1_traducoes.json', "w")
    json.dump(db, file, ensure_ascii=False, indent=4)
    file.close()
    
    return {description: {"descricao": descricao}}

@app.route("/terminos/<description>", methods=["DELETE"])
def delete_termi(description):
    descricao = db[description]
    if description in db:
        del db[description]
    
    file = open('ordenado_wikit1_traducoes.json', "w")
    json.dump(db, file, ensure_ascii=False, indent=4)
    file.close()
    
    return {description: {"descripción": descricao}}


#########################################

@app.route("/sistemas")
def sistemas():
    with open('sistemas.json', 'r') as file:
        data = json.load(file)
    return render_template("sistemasPT.html", title="Sistemas do Corpo Humano", menuData=data)

@app.route("/systems")
def systems():
    with open('sistemas.json', 'r') as file:
        data = json.load(file)
    return render_template("sistemasING.html", title="Sistemas do Corpo Humano", menuData=data)

@app.route("/systemas")
def systemas():
    with open('sistemas.json', 'r') as file:
        data = json.load(file)
    return render_template("sistemasESP.html", title="Sistemas do Corpo Humano", menuData=data)


#########################################


@app.route('/doencas', methods=['GET'])
def doencas():
    term = request.args.get('search-box')
    result = {}

    if term:
        # Procurar o termo no JSON
        for subdict in db1:
            for doenca, detalhes in subdict.items():
                if term.lower() in doenca.lower():
                    result[doenca] = detalhes

    return render_template('doencas.html', title='Doenças', term=term, result=result)

@app.route('/diseases', methods=['GET'])
def diseases():
    term = request.args.get('search-box')
    result = {}

    if term:
        # Procurar o termo no JSON
        for subdict in db1:
            for doenca, detalhes in subdict.items():
                if term.lower() in doenca.lower():
                    result[doenca] = detalhes

    return render_template('doencasING.html', title='Diseases', term=term, result=result)

@app.route('/enfermedades', methods=['GET'])
def enfermedades():
    term = request.args.get('search-box')
    result = {}

    if term:
        # Procurar o termo no JSON
        for subdict in db1:
            for doenca, detalhes in subdict.items():
                if term.lower() in doenca.lower():
                    result[doenca] = detalhes

    return render_template('doencasESP.html', title='Enfermedades', term=term, result=result)


#########################################
#########################################

@app.route("/uploadING", methods=["GET", "POST"])
def uploadING():
    if request.method == "POST":
        file = request.files["file"]
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            xml_filename = os.path.splitext(filename)[0] + ".xml"
            xml_path = os.path.join(app.config["XML_FOLDER"], xml_filename)
            
            file.save(file_path)
            convert_to_xml(file_path, xml_path)
                        
            # Redirecionar para a rota que exibe o PDF
            return redirect(url_for("show_pdf", filename=filename))
    
    return render_template("uploadING.html")

@app.route("/uploadPT", methods=["GET", "POST"])
def uploadPT():
    if request.method == "POST":
        file = request.files["file"]
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            xml_filename = os.path.splitext(filename)[0] + ".xml"
            xml_path = os.path.join(app.config["XML_FOLDER"], xml_filename)
            
            file.save(file_path)
            convert_to_xml(file_path, xml_path)
                        
            # Redirecionar para a rota que exibe o PDF
            return redirect(url_for("show_pdf", filename=filename))
    
    return render_template("uploadPT.html")

@app.route("/uploadESP", methods=["GET", "POST"])
def uploadESP():
    if request.method == "POST":
        file = request.files["file"]
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            xml_filename = os.path.splitext(filename)[0] + ".xml"
            xml_path = os.path.join(app.config["XML_FOLDER"], xml_filename)
            
            file.save(file_path)
            convert_to_xml(file_path, xml_path)
                        
            # Redirecionar para a rota que exibe o PDF
            return redirect(url_for("show_pdf", filename=filename))
    
    return render_template("uploadESP.html")
#########################################


@app.route("/pdf/<filename>")
def show_pdf(filename):
    pdf_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    return send_file(pdf_path, mimetype="application/pdf")

#########################################

@app.route("/xml_filesING")
def xml_filesING():
    xml_folder = app.config["XML_FOLDER"]
    files = os.listdir(xml_folder)
    xml_files = [f for f in files if f.endswith(".xml")]
    return render_template("xml_filesING.html", xml_files=xml_files)

@app.route("/xml_filesPT")
def xml_filesPT():
    xml_folder = app.config["XML_FOLDER"]
    files = os.listdir(xml_folder)
    xml_files = [f for f in files if f.endswith(".xml")]
    return render_template("xml_filesPT.html", xml_files=xml_files)

@app.route("/xml_filesESP")
def xml_filesESP():
    xml_folder = app.config["XML_FOLDER"]
    files = os.listdir(xml_folder)
    xml_files = [f for f in files if f.endswith(".xml")]
    return render_template("xml_filesESP.html", xml_files=xml_files)

#########################################

@app.route("/open_xmlING/<filename>")
def open_xmlING(filename):
    xml_folder = app.config["XML_FOLDER"]
    xml_path = os.path.join(xml_folder, filename)
    with open(xml_path, "r") as file:
        xml_content = file.read()

    # Realizar a limpeza no conteúdo XML
    xml_content = clean(xml_content)
    remove_page = re.sub(r"</?page.*?>", "\n", xml_content)
    remove_text = re.sub(r"</?text.*?>", "\n", remove_page)

    # Verificar se cada termo aparece na base de dados e sublinhar os termos correspondentes no XML
    terms_present = db.keys()

    # Construir a expressão regular para encontrar os termos no XML (insensível a maiúsculas/minúsculas)
    pattern = r"\b(" + "|".join(re.escape(term) for term in terms_present) + r")\b"
    
    def replace_term(match):
        term = match.group(0)
        if term.lower() in db:
            return f"<u><a href='/term/{term.lower()}'>{term}</a></u>"
        else:
            return term

    xml_content_sublined = re.sub(pattern, replace_term, remove_text, flags=re.IGNORECASE)

    return render_template("open_xmlING.html", filename=filename, xml_content=xml_content_sublined)


@app.route("/open_xmlPT/<filename>")
def open_xmlPT(filename):
    xml_folder = app.config["XML_FOLDER"]
    xml_path = os.path.join(xml_folder, filename)
    with open(xml_path, "r") as file:
        xml_content = file.read()

    # Realizar a limpeza no conteúdo XML
    xml_content = clean(xml_content)
    remove_page = re.sub(r"</?page.*?>", "\n", xml_content)
    remove_text = re.sub(r"</?text.*?>", "\n", remove_page)

    # Verificar se cada termo aparece na base de dados e sublinhar os termos correspondentes no XML
    terms_present = db.keys()

    # Construir a expressão regular para encontrar os termos no XML (insensível a maiúsculas/minúsculas)
    pattern = r"\b(" + "|".join(re.escape(term) for term in terms_present) + r")\b"
    
    def replace_term(match):
        term = match.group(0)
        if term.lower() in db:
            return f"<u><a href='/termo/{term.lower()}'>{term}</a></u>"
        else:
            return term

    xml_content_sublined = re.sub(pattern, replace_term, remove_text, flags=re.IGNORECASE)

    return render_template("open_xmlPT.html", filename=filename, xml_content=xml_content_sublined)

@app.route("/open_xmlESP/<filename>")
def open_xmlESP(filename):
    xml_folder = app.config["XML_FOLDER"]
    xml_path = os.path.join(xml_folder, filename)
    with open(xml_path, "r") as file:
        xml_content = file.read()

    # Realizar a limpeza no conteúdo XML
    xml_content = clean(xml_content)
    remove_page = re.sub(r"</?page.*?>", "\n", xml_content)
    remove_text = re.sub(r"</?text.*?>", "\n", remove_page)

    # Verificar se cada termo aparece na base de dados e sublinhar os termos correspondentes no XML
    terms_present = db.keys()

    # Construir a expressão regular para encontrar os termos no XML (insensível a maiúsculas/minúsculas)
    pattern = r"\b(" + "|".join(re.escape(term) for term in terms_present) + r")\b"
    
    def replace_term(match):
        term = match.group(0)
        if term.lower() in db:
            return f"<u><a href='/terminos/{term.lower()}'>{term}</a></u>"
        else:
            return term

    xml_content_sublined = re.sub(pattern, replace_term, remove_text, flags=re.IGNORECASE)

    return render_template("open_xmlESP.html", filename=filename, xml_content=xml_content_sublined)

#########################################

if __name__ == "__main__":
    app.run(host="localhost", port=3000, debug=True)