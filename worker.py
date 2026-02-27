from celery import Celery

from tools import read_data_tool

from ai_analyzer import analyze_financial_text

from database import update_result


celery = Celery(

    "worker",

    broker="redis://localhost:6379/0",

    backend="redis://localhost:6379/0"

)


@celery.task
def analyze_document_task(record_id, query, file_path):

    text = read_data_tool(file_path)

    result = analyze_financial_text(text, query)

    update_result(record_id, result)

    return result