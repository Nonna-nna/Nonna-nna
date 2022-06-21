import cv2
import numpy as np


class color_proc:
  def color_proc(self):
    white_ratio_list = []

    if self.theme == '1':
      #self.img2にきさげ用の加工をする
      print('start color proc')
      '''以下、モノクロクレースケール化'''
      img8 = cv2.cvtColor(self.img2, cv2.COLOR_BGR2GRAY)
      #モノクログレースケール画像を表示
      print("モノクログレースケール画像を表示")
      cv2.imshow(img8)
      cv2.waitKey(0)

      '''以下、元画像とマスクを合成'''
      # 抽出する色の下限(BGR)
      bgrLower = np.array([70])
      # 抽出する色の上限(BGR)
      bgrUpper = np.array([255])
      img_mask = cv2.inRange(img8, bgrLower, bgrUpper)
      img9 = cv2.bitwise_and(img8, img8, mask=img_mask)
      #マスク後の画像を表示
      print("マスク後の画像を表示")
      cv2.imshow(img9)
      cv2.waitKey(0)

      '''以下、モノクロ二値化にする'''
      #閾値を決める
      threshold=83
      #オブジェクトmask_imageを閾値threshold(127)で二値化しimg_binaryに代入
      ret, img10= cv2.threshold(img9, threshold, 255, cv2.THRESH_BINARY)
      #結果を表示
      print("結果を表示")
      cv2.imshow(img10)
      cv2.waitKey(0)

      '''以下保存'''
      output_path = self.output_dir + '/' + self.img2.name
      cv2.imwrite(output_path, img10)

      '''以下、白ピクセルの割合を数える'''
      #rbg_image = cv2.cvtColor(image_binary, cv2.COLOR_RGB2BGR)
      #rbg_image = cv2.cvtColor(image_binary)
      white = cv2.countNonZero(img10)
      print('白のピクセル数は', white)

      all_pixel = np.size(img10)
      #all_pixel = np.size(rbg_image)
      print('全ピクセル数は', all_pixel)
      white_ratio = (white / all_pixel) * 100
      print('白のピクセルの割合は', white_ratio, '%')

      '''以下、配列に入れる'''
      white_ratio_list = []
      white_ratio_list.append(white_ratio)
      print(white_ratio_list)

    else:
      #self.img2に多孔質材用の加工をする
      print('start color proc')
      #GBR範囲指定
      lower = np.array([96,128,128], dtype=np.uint8)
      upper = np.array([192,224,224], dtype=np.uint8)

      #maskとbitwise_andで黄色い部分を抜いてその他を黒に。
      img_mask = cv2.inRange(self.img2, lower, upper)     
      img3 = cv2.bitwise_and(self.img2, self.img2,  mask= img_mask)

      #マスク後の画像を表示
      print("マスク後の画像を表示")
      cv2.imshow(img3)
      cv2.waitKey(0)

      #グレースケールに変更
      img4 = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)
      #モノクログレースケール画像を表示
      print("モノクログレースケール画像を表示")
      cv2.imshow(img4)
      cv2.waitKey(0)

      #二値化
      threshold=83
      ret, img5= cv2.threshold(img4, threshold, 255, cv2.THRESH_BINARY)
      #結果を表示
      print("結果を表示")
      cv2.imshow(img5)
      cv2.waitKey(0)
      #白ピクセルのカウント
      white = cv2.countNonZero(img5)
      print('白のピクセル数は', white)
      all_pixel = np.size(img5)
      #all_pixel = np.size(rbg_image)
      print('全ピクセル数は', all_pixel)
      white_ratio = (white / all_pixel) * 100
      print('白のピクセルの割合は', white_ratio, '%')
      '''以下、配列に入れる'''
      white_ratio_list.append(white_ratio)

      '''以下、保存'''
      output_path = self.output_dir + '/' + self.img2.name
      cv2.imwrite(output_path, img5)
    print(white_ratio_list)


  def set(self, theme, img2, output_dir):
    self.theme = theme
    self.img2 = img2
    self.output_dir = output_dir