import color_proc
import pathlib
import cv2
import time

class trim:
  def all(self):
    #適用する拡張子
    if self.extension == '1':
        image_list = list(pathlib.Path(self.input_dir).glob('**/*.jpeg'))
    elif self.extension == '2':
        image_list = list(pathlib.Path(self.input_dir).glob('**/*.png'))
    elif self.extension == '3':
        image_list = list(pathlib.Path(self.input_dir).glob('**/*.JPEG'))
    elif self.extension == '4':
        image_list = list(pathlib.Path(self.input_dir).glob('**/*.PNG'))
    else:
        image_list = list(pathlib.Path(self.input_dir).glob('**/*.HEIC'))


    '''一括トリミング'''
    if self.trim == '1':
      #一括トリミング
      if self.theme == '1':
        #1の場合はきさげ
          top = 100
          bottom = 900
          left = 600
          right = 1500

      else:
        #2の場合は多孔質材
        #仮の値です
        top = 150
        bottom = 950
        left = 650
        right = 1550
        
      for i in range(len(image_list)):
        img1 = cv2.imread(str(image_list[i]))
        img2 = img1[top : bottom, left: right]
        print("トリミング画像の表示")
        cv2.imshow(img2) #この時点ではウィンドウは表示されない
        cv2.waitKey(0) 
        #output_path = output_dir + '/' + image_list[i] + _[i].name
        #cv2.imwrite(output_path, img1)
        '''ここに色の処理を追加''' #  def set(self, theme, img2, output_dir):
        if self.theme == '1':
          #きさげの処理
          print('1')
          proc1 = color_proc.color_proc()
          proc1.set(1, img2, self.output_dir)
        else:
          #多孔質材の処理
          print('2')
          proc2 = color_proc.color_proc()
          proc2.set(2, img2, self.output_dir)

    '''一枚だけ選択'''
    if self.trim == '2':
      for i in range(len(image_list)):
        img1 = cv2.imread(str(image_list[i]))
        if i == 0:
          y_step=100 #高さ方向のグリッド間隔(単位はピクセル)
          x_step=100 #幅方向のグリッド間隔(単位はピクセル)
          #オブジェクトimgのshapeメソッドの1つ目の戻り値(画像の高さ)をimg_yに、2つ目の戻り値(画像の幅)をimg_xに
          img_y,img_x=img1.shape[:2]  
          #横線を引く：y_stepからimg_yの手前までy_stepおきに白い(BGRすべて255)横線を引く
          img1[y_step:img_y:y_step, :, :] = 255
          #縦線を引く：x_stepからimg_xの手前までx_stepおきに白い(BGRすべて255)縦線を引く
          img1[:, x_step:img_x:x_step, :] = 255
          #cv2.imwrite('grid.png',img1) #ファイル名'grid.png'でimgを保存
          cv2.imshow(img1)
          cv2.waitKey(0)
          time.sleep(5)
          print('1マス100pxです。')
          time.sleep(3)
          top_s = input('上の座標を指定してください')
          bottom_s = input('下の座標を指定してください')
          left_s = input('左の座標を指定してください')
          right_s = input('右の座標を指定してください')

          top_i = int(top_s)
          bottom_i = int(bottom_s)
          left_i = int(left_s)
          right_i = int(right_s)

          x = right_i - left_i
          y = bottom_i - top_i
          resize_size = x * y
          print('トリミング後のサイズは', resize_size, 'です。')

          if self.theme == '1':
            #きさげの場合
            if resize_size == 720000:
              print('pass')
              img2 = img1[top_i : bottom_i, left_i: right_i]
              print("トリミング画像の表示")
              #cv2.imwrite("out_sample1.jpg", img2)
              cv2.imshow(img2)
              cv2.waitKey(0)
              #output_path = output_dir + '/' + image_list[i].name
              #cv2.imwrite(output_path, img2)
              '''ここに色の処理を追加'''
              #きさげの処理 
              proc1 = color_proc.color_proc()
              proc1.set(1, img2, self.output_dir)
            else:
              print('もう一度サイズを決めなおしてください')

          else:
            #多孔質材の場合
            if resize_size == 150000:
                print('pass')
                img2 = img1[top_i : bottom_i, left_i: right_i]
                print("トリミング画像の表示")
                #cv2.imwrite("out_sample1.jpg", img2)
                cv2.imshow(img2)
                cv2.waitKey(0)
                #output_path = output_dir + '/' + image_list[i].name
                #cv2.imwrite(output_path, img2)
                '''ここに色の処理を追加'''
                #多孔質材の処理
                proc2 = color_proc.color_proc()
                proc2.set(2, img2, self.output_dir)  
            else:
              print('もう一度サイズを決めなおしてください')
        else:
          img2 = img1[top_i : bottom_i, left_i: right_i]
          print("トリミング画像の表示")
          #cv2.imwrite("out_sample1.jpg", img2)
          cv2.imshow(img2)
          cv2.waitKey(0)
          #output_path = output_dir + '/' + image_list[i].name
          #cv2.imwrite(output_path, img2)

          '''ここに色の処理を追加'''
        if self.theme == '1':
          #きさげの処理
          print('1')
          proc1 = color_proc.color_proc()
          proc1.set(1, img2, self.output_dir)
        else:
          #多孔質材の処理
          print('2')
          proc2 = color_proc.color_proc()
          proc2.set(2, img2, self.output_dir)
      print('done all')

    '''全選択'''
    #1枚ずつ選択
    print('この方法は推奨しません。')

    for i in range(len(image_list)):
      y_step=100 #高さ方向のグリッド間隔(単位はピクセル)
      x_step=100 #幅方向のグリッド間隔(単位はピクセル)
      img1 = cv2.imread(str(image_list[i])) #画像を読み出しオブジェクトimgに代入
      #オブジェクトimgのshapeメソッドの1つ目の戻り値(画像の高さ)をimg_yに、2つ目の戻り値(画像の幅)をimg_xに
      img_y,img_x=img1.shape[:2]  
      #横線を引く：y_stepからimg_yの手前までy_stepおきに白い(BGRすべて255)横線を引く
      img1[y_step:img_y:y_step, :, :] = 255
      #縦線を引く：x_stepからimg_xの手前までx_stepおきに白い(BGRすべて255)縦線を引く
      img1[:, x_step:img_x:x_step, :] = 255
      cv2.imshow(img1)
      cv2.waitKey(0)
      time.sleep(5)
      print('1マス100pxです。')
      if self.theme == '1':
        print('総ピクセル数が720000pxになるように指定してください')
      else:
        print('総ピクセル数が720000pxになるように指定してください')

      time.sleep(3)
      top_s = input('上の座標を指定してください')
      bottom_s = input('下の座標を指定してください')
      left_s = input('左の座標を指定してください')
      right_s = input('右の座標を指定してください')

      top_i = int(top_s)
      bottom_i = int(bottom_s)
      left_i = int(left_s)
      right_i = int(right_s)

      x = right_i - left_i
      y = bottom_i - top_i
      resize_size = x * y
      print(resize_size)

      if self.theme == '1':
        if resize_size == 720000:
          print('pass')
          img2 = img1[top_i : bottom_i, left_i: right_i]
          print("トリミング画像の表示")
          #cv2.imwrite("out_sample1.jpg", img2)
          cv2.imshow(img2)
          cv2.waitKey(0)
          #output_path = output_dir + '/' + image_list[i].name
          #cv2.imwrite(output_path, img2)
          '''ここに色の処理を追加'''
          #きさげの処理    
        else:
          print(i, '枚目はトリミングできませんでした。')
          print('後ほど正しく範囲を指定してください。')
      else:
        if resize_size == 720000:
          print('pass')
          img2 = img1[top_i : bottom_i, left_i: right_i]
          print("トリミング画像の表示")
          #cv2.imwrite("out_sample1.jpg", img2)
          cv2.imshow(img1)
          cv2.waitKey(0)
          #output_path = output_dir + '/' + image_list[i].name
          #cv2.imwrite(output_path, img2)
          '''ここに色の処理を追加'''
          #きさげの処理    
        else:
          print(i, '枚目はトリミングできませんでした。')
          print('後ほど正しく範囲を指定してください。')


  def set(self, trim, theme, input_dir, output_dir, extension):
    self.trim = trim
    self.theme = theme
    self.input_dir = input_dir
    self.output_dir = output_dir
    self.extension = extension