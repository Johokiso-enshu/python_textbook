AnacondaによるPython開発環境の構築（補足）
============================================

ここではPythonの数値計算ライブラリ一式と、対話的実行環境であるJupyter-notebookを含むパッケージであるAnacondaのダウンロード・インストール方法について述べる。
PythonやJupyterは現在は京都大学の教育用教PC端末で用いることができるが、
各自のPCにもインストールしておくと良い。

本章ではWindowsへのインストール方法を述べるが、OS XやLinux等で用いる場合は
次のページを参考にすること。 https://www.anaconda.com/products/individual

Anacondaのダウンロード
-------------------------

Anacondaは無料（商用利用は無料ではないため注意）かつオープンソース（ソースコードが公開されていること）のソフトウェアであり、以下のページからダウンロードできる。

https://www.anaconda.com/products/individual


下図に示すように、OSごとに異なるインストーラが提供されているため、Windows用のものをダウンロードする。

.. image:: figs/fig_python_install/Anaconda_download.png
   :width: 50%
   :alt: anaconda download
   :align: center

Anacondaのダウンロードページの様子。Python3.* のもののうち各自のOSにあわせたものをダウンロードすること。


Anacondaのインストール
-------------------------

先ほどダウンロードしたファイルを実行（クリック）することでインストールが始まる。

ダウンロードしたファイルの保存場所がわからなければインターネットブラウザの設定を確認する。
多くの場合、デフォルトではダウンロードフォルダ（以下の図を参照）にダウンロードされる。

インストーラにはいくつか質問されるが、よくわからなければデフォルトのままでよい。
なお、Windowsのユーザーアカウントにホワイトスペースを含む場合はインストールがうまくいかないかもしれない。
その場合は、途中の選択肢のうち、

+ ユーザーごとのインストール（デフォルト）
+ 全ユーザーに対するインストール（管理者権限が必要）

のうち、「全ユーザーに対するインストール」を行うと回避できる。

（ユーザー名にスペースのほか特殊文字（スラッシュや￥などの記号）を含んだシステムでは、様々なソフトウェアに不具合が生じることがある。今後はできるだけ半角英数字のユーザー名にしておいたほうがよい）

.. image:: figs/fig_python_install/Anaconda_install.png
   :width: 50%
   :alt: anaconda install
   :align: center

ダウンロードした場所をエクスプローラで開き、ファイルを実行する。

.. image:: figs/fig_python_install/Anaconda_install2.png
   :width: 50%
   :alt: alternate jupyter launch
   :align: center

インストーラを実行した時の様子。

.. image:: figs/fig_python_install/Anaconda_install3.png
   :width: 50%
   :alt: alternate jupyter launch
   :align: center

インストールには少し時間がかかる。

.. image:: figs/fig_python_install/Anaconda_install5.png
   :width: 50%
   :alt: alternate jupyter launch
   :align: center

このような画面が出れば完成である。
