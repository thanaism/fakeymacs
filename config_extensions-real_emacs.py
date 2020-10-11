﻿# -*- mode: python; coding: utf-8-with-signature-dos -*-

####################################################################################################
## Emacs の場合、IME 切り替え用のキーを C-\ に置き換える
####################################################################################################

# Emacs で mozc を利用する際に Windows の IME の切換えキーを mozc の切り替えキーとして
# 機能させるための設定です。初期設定では NTEmacs（gnupack 含む）と Windows の Xサーバで動く
# Emacs を指定しています。

x_window_apps = ["XWin.exe",               # Cygwin/X
                 "XWin_MobaX.exe",         # MobaXterm/X
                 "XWin_MobaX_1.16.3.exe",  # MobaXterm/X
                 "XWin_Cygwin_1.14.5.exe", # MobaXterm/X
                 "XWin_Cygwin_1.16.3.exe", # MobaXterm/X
                 "Xming.exe",              # Xming
                 "vcxsrv.exe",             # VcXsrv
                 "X410.exe",               # X410
                 "Xpra-Launcher.exe",      # Xpra
                ]

def is_real_emacs(window):
    if (window.getClassName() == "Emacs" or
        (window.getProcessName() in x_window_apps and
         # ウィンドウのタイトルを検索する正規表現を指定する
         # Emacs を起動しているウィンドウを検索できるように、Emacs の frame-title-format 変数を
         # 次のように設定するなどして、識別できるようにする
         # (setq frame-title-format (format "emacs-%s - %%b" emacs-version))
         re.search(r"^emacs-", window.getText()))):
        return True
    else:
        return False

keymap_real_emacs = keymap.defineWindowKeymap(check_func=is_real_emacs)

# IME 切り替え用のキーの置き換え
# （Emacs 側での C-F1 と C-F2 の設定については、次のページを参照してください。
#   https://w.atwiki.jp/ntemacs/pages/48.html ）
define_key(keymap_real_emacs, "(243)",   self_insert_command("C-Yen")) # [半角／全角] キー
define_key(keymap_real_emacs, "(244)",   self_insert_command("C-Yen")) # [半角／全角] キー
define_key(keymap_real_emacs, "LA-(25)", self_insert_command("C-Yen")) # Alt-` キー
define_key(keymap_real_emacs, "RA-(25)", self_insert_command("C-Yen")) # Alt-` キー

define_key(keymap_real_emacs, "(29)",    self_insert_command("C-F1"))  # [無変換] キー
define_key(keymap_real_emacs, "(28)",    self_insert_command("C-F2"))  # [変換] キー
# define_key(keymap_real_emacs, "O-LAlt",  self_insert_command("C-F1"))  # 左 Alt キーの単押し
# define_key(keymap_real_emacs, "O-RAlt",  self_insert_command("C-F2"))  # 右 Alt キーの単押し
