FROM continuumio/miniconda3

RUN pip install mlflow \
    && pip install numpy \
    && pip install scipy \
    && pip install pandas \
    && pip install scikit-learn \
    && pip install boto3 \
    && pip install cloudpickle 

#AWS
ENV AWS_ACCESS_KEY_ID="*AWS_ACCESS_KEY_ID*"
ENV AWS_SECRET_ACCESS_KEY="*AWS_SECRET_ACCESS_KEY*"
ENV S3_BUCKET="*S3_BUCKET*"

#DB
ENV DB_CONNECTION="*DB_CONNECTION*"

#MLFLOW
ENV MLFLOW_SERVER_TRACKING_URI="*MLFLOW_TRACKING_URI*"


