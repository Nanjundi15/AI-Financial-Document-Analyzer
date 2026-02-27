from fastapi import FastAPI, UploadFile, File, Form
import os
import uuid

from database import init_db, create_record, get_result

from worker import analyze_document_task


app = FastAPI()

init_db()


@app.get("/")
def root():

    return {"status": "running"}


@app.post("/analyze")
async def analyze_file(

    file: UploadFile = File(...),

    query: str = Form(...)

):

    os.makedirs("data", exist_ok=True)

    file_path = f"data/{uuid.uuid4()}.pdf"

    with open(file_path, "wb") as f:

        f.write(await file.read())

    record_id = create_record(file.filename, query)

    analyze_document_task.delay(

        record_id,

        query,

        file_path

    )

    return {

        "analysis_id": record_id,

        "status": "processing"

    }


@app.get("/result/{analysis_id}")
def result(analysis_id: int):

    row = get_result(analysis_id)

    if row:

        return {

            "id": row[0],

            "filename": row[1],

            "query": row[2],

            "result": row[3],

            "status": row[4]

        }

    return {"error": "not found"}