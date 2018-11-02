""" Script to add part of transcript to notes to a google sheet"""
import os
import json

from arrow import utcnow
from pathlib import Path


def create_log_file(user_id: str) -> str:
    log_date = utcnow().\
                to('Europe/London').\
                format("MMM_DD_YYYY")

    log_dir = f'{log_date}/'
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    csv_file = f'{log_date}/{user_id}.csv'
    if not os.path.isfile(csv_file):
        # create headers
        # Timestamp, Sentence, Note Type, Note, Confidence
        with open(csv_file, 'w') as f:
            f.write('Timestamp,')
            f.write('Position,')
            f.write('Transcript,')
            f.write('Confidence,')
            f.write('Result,')
            f.write('Actual Transcript\n')
        f.close()

    log_path_base = Path(log_dir)
    return f'{log_path_base}/{user_id}.csv'


def log(log_content: dict, position: int):
    '''
    we are here to behave and log some tings
    {
        'transcript',
        'confidence'
    }
    '''
    if log_content is not None:
        if {
            'transcript', 'confidence'
        } <= set(log_content):
            log_date = utcnow().\
                to('Europe/London').\
                format("HH:mm:ss")
            user_id = 'Alan'
            log_file = create_log_file(user_id)
            with open(log_file, 'a') as f:
                f.write(f'{log_date},')
                f.write(f'{position},')
                f.write(f'{log_content["transcript"]},')
                f.write(f'{log_content["confidence"]}\n')
            f.close()
            pass
    else:
        return 'dont send me nuting'