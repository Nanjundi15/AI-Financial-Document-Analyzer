from langchain_community.document_loaders import PyPDFLoader


def read_data_tool(path):

    loader = PyPDFLoader(path)

    docs = loader.load()

    text = ""

    for page in docs:
        text += page.page_content + "\n"

    return text