import boto3

s3_resource = boto3.resource('s3')
s3_resource.Object('layerfiles-mlops-course', 'layer_file.zip').download_file('./layer.zip')
s3_resource.Object('layerfiles-mlops-course', 'model.onnx').download_file('./model.onnx')
s3_resource.Object('layerfiles-mlops-course', 'mlflow_model.zip').download_file('./mlflow_model.zip')
s3_resource.Object('layerfiles-mlops-course', 'input_batch.csv').download_file('./input_batch.csv')
