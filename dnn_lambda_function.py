import json
import boto3
import sys

# EFS 경로의 패키지를 import 가능하게 수정
sys.path.append("/mnt/efs/packages")
import numpy as np
# import xgboost as xgb

# S3에서 모델 다운로드
s3 = boto3.client('s3')
s3.download_file('unho-spmm', 'model/sp_smdm_xgb.model', '/tmp/sp_smdm_xgb.model' )
s3.download_file('unho-spmm', 'model/bz_smsm_xgb.model', '/tmp/bz_smsm_xgb.model' )

# 모델 불러오기
# sp_smdm_xgb_model = xgb.XGBRegressor()
# bz_smsm_xgb_model = xgb.XGBRegressor()
# sp_smdm_xgb_model.load_model('/tmp/sp_smdm_xgb.model')
# bz_smsm_xgb_model.load_model('/tmp/bz_smsm_xgb.model')

def lambda_handler(event, context):
    
    # event로부터 feature 전처리
    lr = event["lr"]
    lc = event["lc"]
    rc = event["rc"]
    ld = event["ld"]
    rd = event["rd"]
    lnnz = event["lnnz"]
    rnnz = event["rnnz"]

    # 모델 입력으로 사용할 input_feature 생성
    input_feature = np.array([[lr,lc,rc,ld,rd,lnnz,rnnz]])
    
    # input_feature에 대한 모델별 예측값 추론
    # sp_smdm_xgb_result = sp_smdm_xgb_model.predict(input_feature)
    # bz_smsm_xgb_result = bz_smsm_xgb_model.predict(input_feature)
    
    # sp_smdm, bz_smsm 중 최적의 method
    optim_method = ""
    
#     # sp_smdm이 최적일 경우
#     if (sp_smdm_xgb_result[0] <= bz_smsm_xgb_result[0]):
#         optim_method = "sp_smdm"
#     # bz_smsm이 최적일 경우
#     else:
#         optim_method = "bz_smsm"
    
# 	# 결과 생성
#     result = "sp_smdm : " + str(sp_smdm_xgb_result[0]) + " , " + \
# 		"bz_smsm : " + str(bz_smsm_xgb_result[0]) + " , " + \
# 		"optim_method : " + optim_method

	# 결과 반환
    return {
        'statusCode': 200,
        'body': json.dumps(result)
    }