﻿# -*- mode: python; coding: utf-8-with-signature-dos -*-

####################################################################################################
## 機能オプションの選択
####################################################################################################
# [section-options] --------------------------------------------------------------------------------

# IMEの設定（３つの設定のいずれか一つを True にする）
P.use_old_Microsoft_IME = False
P.use_new_Microsoft_IME = False
P.use_Google_IME = True

# 追加機能のオプションの設定
P.use_edit_mode = True
P.use_real_emacs = True
P.use_change_keyboard = True

####################################################################################################
## 基本設定
####################################################################################################
# [section-base-1] ---------------------------------------------------------------------------------

# Emacs のキーバインドに“したくない”アプリケーションソフトを指定する
P.not_emacs_target    += [
                         ]

# IME の切り替え“のみをしたい”アプリケーションソフトを指定する
P.ime_target          += [
                         ]

# キーマップ毎にキー設定をスキップするキーを指定する
P.skip_settings_key    = {"keymap_global"    : [],
                          "keymap_emacs"     : [],
                          "keymap_ime"       : [],
                          "keymap_ei"        : [],
                          "keymap_tsw"       : [],
                          "keymap_lw"        : [],
                          "keymap_edit_mode" : [],
                         }

# Emacs のキーバインドにするアプリケーションソフトで、Emacs キーバインドから除外するキーを指定する
P.emacs_exclusion_key  = {"chrome.exe"       : ["C-l", "C-t"],
                          "msedge.exe"       : ["C-l", "C-t"],
                          "firefox.exe"      : ["C-l", "C-t"],
                         }

P.side_of_ctrl_key = "R"
P.set_input_method_key += [["C-j", None]]
# P.desktop_switching_key += [["W-Left", "W-Right"]]
# P.window_movement_key_for_desktops += [["W-p", "W-n"]]
# P.window_movement_key_for_desktops += [["W-Up", "W-Down"]]

# [section-base-2] ---------------------------------------------------------------------------------

# emacsclient プログラムを起動するキーを指定する
P.emacsclient_key = "C-Period"

# emacsclient プログラムを指定する
P.emacsclient_name = r"<Windows パス>\wslclient-n.exe"

# emacsclient プログラムの起動
def emacsclient():
    clipboard_text = getClipboardText()
    if clipboard_text:
        path = re.sub("\n|\r", "", clipboard_text.strip())
        path = re.sub(r'(\\+)"', r'\1\1"', path)
        path = re.sub('"', r'\"', path)
        path = re.sub('^', '"', path)
        keymap.ShellExecuteCommand(None, P.emacsclient_name, path, "")()

define_key(keymap_emacs, P.emacsclient_key, emacsclient)

####################################################################################################
## クリップボードリストの設定
####################################################################################################
# [section-clipboardList-1] ------------------------------------------------------------------------
# [section-clipboardList-2] ------------------------------------------------------------------------

####################################################################################################
## ランチャーリストの設定
####################################################################################################
# [section-lancherList-1] --------------------------------------------------------------------------
# [section-lancherList-2] --------------------------------------------------------------------------

####################################################################################################
## C-Enter に F2（編集モード移行）を割り当てる（オプション）
####################################################################################################
# [section-edit_mode-1] ----------------------------------------------------------------------------
# [section-edit_mode-2] ----------------------------------------------------------------------------

####################################################################################################
## Emacs の場合、IME 切り替え用のキーを C-\ に置き換える（オプション）
####################################################################################################
# [section-real_emacs-1] ---------------------------------------------------------------------------
# [section-real_emacs-2] ---------------------------------------------------------------------------

####################################################################################################
## 英語キーボード設定をした OS 上で、日本語キーボードを利用する場合の切り替えを行う（オプション）
####################################################################################################
# [section-change_keyboard-1] ----------------------------------------------------------------------
# [section-change_keyboard-2] ----------------------------------------------------------------------
