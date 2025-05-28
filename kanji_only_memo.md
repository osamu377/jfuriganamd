# 漢字だけにルビを振る方法について考える

1. 空のリストt_kanji[]作成
1. 空のリストt_hira[]作成
1. 空のリストret_string[]作成
1. surfaceを文字のリスト化 ch_list_sur = list(surface)
1. surfaceを文字のリスト化 ch_list_hir = list(hiragana)
1. ch_list_sur[i]は漢字？
    1. 漢字だったら、t_kanji.append(ch_list_sur[i])
    1. ch_list_sur[i]とch_list_hir[0]を比較
    1. 同じだったら、ret_string.append(ch_list_sur[0])
    1. 違っていたら、t_kanji.append