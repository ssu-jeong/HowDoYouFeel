from flask import Blueprint, url_for
import pickle
from flask import render_template, request
import numpy as np
from scipy import misc


# from forms import MaterialsForm
from werkzeug.utils import redirect

from flask_app.views.index_view import index

bp = Blueprint('test', __name__, url_prefix='/predict')
# model = pickle.load(open('airpollution.pkl', 'rb'))

#데이터 예측 처리
@bp.route('/predict', methods=['POST'])
def home():
    # form  = MaterialsForm()
    if request.method == 'POST':
        #업로드 파일 처리 분기
        file = request.files['image']
        if not file: return render_template('index.html', CNN_label='NO Files')

        #이미지 픽셀 정보 읽기
        # 알파 채널 값 제거 후 1차원 Reshape
        img = misc.imread(file)
        img = img[:, :, :3]
        img = img.reshape(1, -1)

        # #입력받은 이미지 예측
        # prediction = model.predict(img)

        # #예측값을 1차원 배열로 부터 확인 가능한 문자열로 변환
        # label = str(np.squeese(prediction))

        # #숫자가 10일 경우 0으로 처리
        # if label == '10' : label = '0'

        #결과 리턴
        return render_template('after.html', CNN_label = label)

    else:
        return redirect(url_for('index.html'))
