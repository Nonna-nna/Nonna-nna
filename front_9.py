#テーマの選択
print("研究テーマは何ですか?次の中からお選びください")
print("1.きさげ　2.多孔質材")
theme = input("Enter number?")

#トリミングの自動機能選択
print("トリミングは自動で行いますか？")
print("一括処理の場合は1を、1枚だけ位置を決めてから一括処理する場合は2を、全て手作業で処理する場合は3を入力してください")
trim = input("Enter number?")

#入力ファイルの確認
print("どのフォルダを処理しますか？パスを入力してください")
print('ダブルクオーテーションで囲んでください')
input_dir = input("Enter path?")

#拡張子の確認
print("拡張子をお選びください")
print('1.jpeg 2.png 3.JPEG 4.PNG 5.HEIC')
extension = input('Enter number?')

#出力ファイルの確認
print("保存先を指定してください")
output_dir = input("Enter path?")

print("設定を完了しました。処理完了までしばらくお待ちください。")
print("Now loading...")

import trim
trim.trim.set(trim, theme, input_dir, output_dir, extension)