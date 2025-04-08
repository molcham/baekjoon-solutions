'''
이진 검색 트리를 전위 순회한 결과
=> 이 트리를 후위 순회한 결과를 구하여라

전위 순회한 결과를 통해 딕셔너리에 다시 저장?
그 다음 다시 후위순회로 change

전위 순회:부모-왼쪽-오른쪽

메모리 초과 나는 이유: 슬라이싱을 써서 
재귀를 돌릴 때 자주 발생함. 


'''
'''
import sys
input=sys.stdin.readline
preorder=[int(line.strip()) for line in sys.stdin if line.strip()]



def build_tree(preorder):
    tree={} #딕셔너리에 저장

#전위 순회한 트리 다시 딕셔너리에 복원
    def construct_tree(preorder):
        if not preorder:
            return None,preorder
    #첫번째 원소는 무조건 루트노드임
        root=preorder[0]
        left_subtree=[]
        right_subtree=[]

    #왼쪽 서브트리:루트보다 작은 값들
    #오른쪽 서브트리:루트보다 큰 값들

        for node in preorder[1:]:
            if node<root:
                left_subtree.append(node)
            #루트보다 작으면 왼쪽에
            else:
                right_subtree.append(node)
            #루트보다 크면 오른쪽에 
    #왼쪽 서브트리,오른쪽 서브트리 '재귀'로 구성
        tree[root]={'left':None,'right':None}
    #tree = {'A': {'left': 'B', 'right': 'C'}, ...}

        if left_subtree:
            tree[root]['left'],left_subtree=construct_tree(left_subtree)
        #재귀 호출
        #이 함수는 두 가지 값을 반환 
        #왼쪽 자식의 값, 아직 남아 있는 전위 순회 리스트
        if right_subtree:
            tree[root]['right'],right_subtree=construct_tree(right_subtree)
        
        #construct_tree함수의 반환값
        return root,[]
    root,_=construct_tree(preorder)
    return tree,root

#트리를 원상복구 시켰으니까 이제 다시 후위순회

#이 방식은 이진 탐색 트리에서 순회를 하면 오름차순이 된다.
def postorder(tree,node):
    if node is None:
       return
    postorder(tree,tree[node]['left'])
    postorder(tree,tree[node]['right'])
    print(node)



tree,root = build_tree(preorder)
postorder(tree,root)

'''

'''
#최적화 버전, 인덱스 기반 + 슬라이싱 없음,딕셔너리 사용

import sys 

preorder=[int(line.strip()) for line in sys.stdin if line.strip()]

tree={} #트리를 딕셔너리로 저장하기
index=[0] #현재 위치 추적용 인덱스

def build_tree(min_val,max_val):
    #bst규칙을 이용하여(왼쪽은 더 작고, 오른쪽은 더 큼)
    #현재위치에서 만들 수 있는 서브트리 구성
    #min_val,max_val 현재 위치에 올 수 있는 값의 허용 범위
    if index[0]>=len(preorder):
        return None
    #preorder 리스트를 다봤으면 더 이상 만들노드가 없다
    #index는 위치 추적용임 !     
    value =preorder[index[0]]
    #value는 preorder 리스트에 있는 인덱스값의 위치에 있는 값



    #현재 값이 범위를 벗어나면 이 위치에서는 쓸 수 없음
    if not (min_val<value<max_val):
        return None
    root = value
    tree[root]={'left':None,'right':None} 
    #tree 딕셔너리 구조가 위와 같음음
    index[0]+=1

    #왼쪽/오른쪽 서브트리를 재귀적으로 구성
    left=build_tree(min_val,root)
    right=build_tree(root,max_val)

    tree[root]['left']=left #재귀호출 한 결과
    tree[root]['right']=right #재귀호출 한 결과

    return root

#트리 구성해주기
root=build_tree(-float('inf'), float('inf'))

def postorder(tree,node):
    if node is None:
       return
    postorder(tree,tree[node]['left'])
    postorder(tree,tree[node]['right'])
    print(node)


postorder(tree,root)

'''

#재귀로 호출하니까 결국 오류계속남 
#스택을 사용한 반복문으로 수정
#전위 순회 => bst구성 => 후위 순회 출력

import sys
input = sys.stdin.readline

# 입력 받기
preorder = [int(line.strip()) for line in sys.stdin if line.strip()]

#예외 처리
if not preorder:
    exit()

# 1. 이진 탐색 트리 구성 (비재귀 방식)
tree = {'val': preorder[0], 'left': None, 'right': None}

def insert(tree,value):
    current = tree
    while True:
        if value<current['val']:
            if current['left'] is None:
                current['left'] = {'val': value, 'left': None, 'right': None}
                return
            else:
                if current['right'] is None:
                    current['right'] = {'val': value, 'left': None, 'right': None}
                    return
                else:
                    current=current['right']
# 트리에 값들 삽입
for val in preorder[1:]: #슬라이싱?
    insert(tree, val)      

#2.후위순회(postorder,스택 사용)
def postorder_iterative(root):
    if root is None:
        return

    stack = [root]
    result = []

    while stack:
        node = stack.pop()
        result.append(node['val'])

        # 왼쪽을 먼저 넣으면 오른쪽이 먼저 처리되기 때문에,
        # 후위 순회를 만들기 위해 오른쪽 먼저 넣기
        if node['left']:
            stack.append(node['left']) #먼저 넣으면 나중에 POP
        if node['right']:
            stack.append(node['right']) # 나중에 넣으면 먼저 POP
        #아래에서 reversed해주기 때문에 
        #왼쪽 먼저 나오게 됩니당

    # 후위 순회는 루트가 마지막에 출력되므로 뒤집어서 출력
    for val in reversed(result):
        print(val) 

# 후위 순회 결과 출력
postorder_iterative(tree) 

'''
후위 순회란 왼쪽=>오른쪽=>루트 순서로 방문
지금 스택으로 순회하고 있다(LIFO) 나중에 넣은게 먼저나옴

but 스택 사용시에 
루트 → 오른쪽 → 왼쪽 ← 이 순서로 pop됨



'''





















