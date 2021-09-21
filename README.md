# Battle Simulator

## 概要

- マメッコホームページの『3rd Force』をヒントにしたドラクエ系バトルシミュレーター。
- 作成したキャラクターでパーティを作り、相手パーティとターン制で戦う。
- 戦闘中はキャラクターを手動で操作することもできるが、本ゲームの醍醐味は自動モード。 <br>
  現在の状況（相手パーティの構成や残りHPなど）にあわせて行動指針を指定し、 <br>
  どんなパーティにも勝てるような最強のパーティ／戦術を組み上げよう！
- 元ネタ： http://mamecco.es.land.to/game/force3/index.html

## 攻略情報

#### ステータス一覧
- HP <br>
  体力。0になると戦闘不能となる。
- MP <br>
  魔力。スキル使用時に消費する。
- ATK <br>
  攻撃力。通常攻撃および物理攻撃スキルのダメージに影響する。
- DEF <br>
  防御力。相手からの通常攻撃および物理攻撃スキルのダメージに影響する。
- INT <br>
  賢さ。魔法攻撃スキルのダメージに影響する。
- AGI <br>
  素早さ。行動順序に影響する。

#### 職業一覧
- 勇者（hero）
- 僧侶（healer）

## 今後の拡張

#### ボーナスポイント振り分けの追加

#### 職業の追加

- 騎士：DEFが高く、味方を庇うスキルを習得する。
- 魔法使い：基本ステータスは低いものの、防御無視／必中の攻撃スキルを習得する。

#### ステータスの追加

- DEX <br>
  器用さ。通常攻撃および物理攻撃スキルの命中率に影響する。
- RES <br>
  精神力。相手からの魔法攻撃スキルのダメージに影響する。

#### 手動戦闘機能追加

戦闘中のキャラクターの行動をユーザが命令できる機能。

#### キャラメイク機能追加

キャラクターの定義情報をプログラムベタ書きから、プログラム実行時にユーザ入力するように拡張する。

#### ランキング機能追加

設置してあるパーティ定義情報を読み込んでリーグ戦を行い、勝敗からランキングを自動計算する機能。

## メモ

#### 戦闘中にキャラクターが見える情報

- 味方パーティ：すべて見える
- 相手パーティの職業：見える
- 相手パーティのステータス詳細、残りHP、所持スキル：見えない
- 各キャラクターの行動履歴：見える
- 各キャラクターの状態変化：見える（？）
