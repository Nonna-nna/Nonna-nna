import os

class count:
  def count(self):
    #ここに処理を記述

    '''ファイル数のカウント'''
    count_file = 0
    for file_name in os.listdir(self.input_dir):
      #ファイルもしくはディレクトリのパスを取得
      file_path = os.path.join(self.input_dir,file_name)
      #ファイルであるか判定
      if os.path.isfile(file_path):
        count_file +=1
    print(count_file)


  def set(self, input_dir):
    self.input_dir = input_dir #後で消去