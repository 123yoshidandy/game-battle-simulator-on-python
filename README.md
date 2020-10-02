# Battle Simulator

## 概要

- マメッコホームページの『3rd Force』をヒントにしたドラクエ系バトルシミュレーター。
- 作成したキャラクターでパーティを作り、相手パーティとターン制で戦う。
- 戦闘中はキャラクターを手動で操作することもできるが、本ゲームの醍醐味は自動モード。
  現在の状況（相手パーティの構成や残りHPなど）にあわせて行動指針を指定し、
  どんなパーティにも勝てるような最強のパーティ／戦術を組み上げよう！
- 元ネタ： http://mamecco.es.land.to/game/force3/index.html

## 設計情報

##### データ構成

- パーティ
  - 名前
  - list of キャラクター
- キャラクター
  - 名前
  - 職業
  - ボーナスポイント振り分け
- 職業
  - 名前
  - 基本ステータス
  - スキル

バトル機能（下記）で登場するキャラクターを作成する機能。
キャラクター作成にあたっての設定項目は以下の通り。
- 名前
- 職業の選択
  ※職業によって基本ステータスおよび所持スキルが異なる。
- ボーナスポイントの振り分け

## 攻略情報

#### ステータス一覧
- HP
  体力。0になると戦闘不能となる。
- ATK
  攻撃力。通常攻撃および物理攻撃スキルのダメージに影響する。
- DEF
  防御力。相手からの通常攻撃および物理攻撃スキルのダメージに影響する。
- AGI
  素早さ。行動順序に影響する。

#### 職業一覧
- 勇者

## 今後の拡張

#### 行動パターンの追加

- 防御
- スキル

#### 職業の追加

- 僧侶：味方のHPを回復するスキルを習得する。
- 騎士：DEFが高く、味方を庇うスキルを習得する。
- 魔法使い：基本ステータスは低いものの、防御無視／必中の攻撃スキルを習得する。

#### ステータスの追加

- MP
  魔力。スキル使用時に消費する。
- INT
  賢さ。魔法攻撃スキルのダメージに影響する。
- RES
  精神力。相手からの魔法攻撃スキルのダメージに影響する。

#### 手動戦闘機能追加

戦闘中のキャラクターの行動をユーザが命令できる機能。

#### 自動戦闘機能追加

設定したパーティによる戦闘を行う機能。

#### AI部分の外部ファイル読み込み機能追加

自動戦闘時のAIを外部ファイル化し、差し替えできるようにする。

#### キャラメイク機能追加

キャラクターの定義情報をプログラムベタ書きから、プログラム実行時にユーザ入力するように拡張する。

#### ファイル読み書き機能追加

パーティの定義情報を外部ファイルに読み書きできるように拡張する。

#### ランキング機能追加

設置してあるパーティ定義情報を読み込んでリーグ戦を行い、勝敗からランキングを自動計算する機能。

## メモ

#### 自動戦闘時の行動決定タイミング

各キャラクターが行動を決定するのは、ターン開始時？それとも自分の行動時？

#### 戦闘中にキャラクターが見える情報

- 味方パーティ：すべて見える
- 相手パーティの職業：見える
- 相手パーティのステータス詳細、残りHP、所持スキル：見えない
- 各キャラクターの行動履歴：見える
- 各キャラクターの状態変化：見える（？）
