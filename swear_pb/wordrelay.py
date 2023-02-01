'''done 입력될때까지 계속하는 끝말잇기 게임 함수'''

def word_relay():
    word_list = []
    idx = 1
    is_playing = True

    while is_playing:
        word = input('단어를 입력해 주세요 : ')
        # 종료 조건
        if word == 'done':
            print('종료')
            is_playing = False
        # 단어 리스트에 매달기 
        word_list.append(word)
        # 두개 이상 단어 있을 때 확인, 같은 단어 입력하거나 글자 안맞췄을때
        if idx >= 2:
            if word_list[idx-1][0] != word_list[idx-2][-1] or word_list[idx-1] in word_list[:idx-1]:
                print('종료', idx)
                is_playing = False
        idx += 1
    
word_relay()