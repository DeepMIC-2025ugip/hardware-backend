import os
from glob import glob

from langchain_community.docstore.document import Document
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters.character import RecursiveCharacterTextSplitter
from tiktoken import encoding_for_model

from utils.json_utils import save_json_list

encoder = encoding_for_model("text-embedding-3-small")


def load_and_split_document(loader: PyPDFLoader, chunk_size: int, chunk_overlap: int):
    documents: list[Document] = loader.load_and_split(
        text_splitter=RecursiveCharacterTextSplitter(
            length_function=lambda text: len(encoder.encode(text)),
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=["\n", "\n\n", "。", "．", " ", ""],
            keep_separator=True,
        )
    )
    return documents


def create_doc_json(
    docs_dir: str,
    save_path: str,
    chunk_size: int = 1000,
    chunk_overlap: int = 200,
):
    pdf_paths = []
    for ext in ["pdf", "txt"]:
        pdf_paths += glob(os.path.join(docs_dir, f"*.{ext}"))
    print(f"file_num: {len(pdf_paths)}")  # debug

    documents = []
    chunk_zero_docs = []

    for num, path in enumerate(pdf_paths, start=1):
        name, ext = os.path.splitext(path)
        if ext == ".txt":
            loader = TextLoader(path)
        elif ext == ".pdf":
            loader = PyPDFLoader(path)
        else:
            raise ValueError(f"unsupported file type: {ext}")
        docs = load_and_split_document(loader, chunk_size, chunk_overlap)

        print(f"\nfile{num}: {name}, chunk num: {len(docs)}")  # debug

        if docs:
            for doc in docs:
                page = doc.metadata.get("page", -1) + 1
                dict = {"title": name, "content": doc.page_content, "page": page}

                documents.append(dict)
        else:
            chunk_zero_docs.append(path)
            print(f"no documents")

    save_json_list(documents, save_path)


if __name__ == "__main__":
    create_doc_json("data", "data/index_docs.json")
