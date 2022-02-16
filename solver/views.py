from django.shortcuts import render


def solve_sudoku(matrix):
    
    def number_unassigned(row, col):
        num_unassign = 0
        for i in range(0,9):
            for j in range (0,9):
                #cell is unassigned
                if matrix[i][j] == 0:
                    row = i
                    col = j
                    num_unassign = 1
                    a = [row, col, num_unassign]
                    return a
        a = [-1, -1, num_unassign]
        return a
    
    def is_safe(n, r, c):
        for i in range(0,9):
            if matrix[r][i] == n:
                return False
        for i in range(0,9):
            if matrix[i][c] == n:
                return False
        row_start = (r//3)*3
        col_start = (c//3)*3
        for i in range(row_start,row_start+3):
            for j in range(col_start,col_start+3):
                if matrix[i][j]==n:
                    return False
        return True

    row = 0
    col = 0
    a = number_unassigned(row, col)
    if a[2] == 0:
        return matrix
    row = a[0]
    col = a[1]
    for i in range(1,10):
        if is_safe(i, row, col):
            matrix[row][col] = i
            if solve_sudoku(matrix):
                return matrix
            matrix[row][col]=0
    return False

# Create your views here.
def sudokustart(request):
    return render(request,'grid.html')

def solver(request):
    var11=request.GET.get('cell-0')
    var12=request.GET.get('cell-1')
    var13=request.GET.get('cell-2')
    var14=request.GET.get('cell-3')
    var15=request.GET.get('cell-4')
    var16=request.GET.get('cell-5')
    var17=request.GET.get('cell-6')
    var18=request.GET.get('cell-7')
    var19=request.GET.get('cell-8')
    var21=request.GET.get('cell-9')
    var22=request.GET.get('cell-10')
    var23=request.GET.get('cell-11')
    var24=request.GET.get('cell-12')
    var25=request.GET.get('cell-13')
    var26=request.GET.get('cell-14')
    var27=request.GET.get('cell-15')
    var28=request.GET.get('cell-16')
    var29=request.GET.get('cell-17')
    var31=request.GET.get('cell-18')
    var32=request.GET.get('cell-19')
    var33=request.GET.get('cell-20')
    var34=request.GET.get('cell-21')
    var35=request.GET.get('cell-22')
    var36=request.GET.get('cell-23')
    var37=request.GET.get('cell-24')
    var38=request.GET.get('cell-25')
    var39=request.GET.get('cell-26')
    var41=request.GET.get('cell-27')
    var42=request.GET.get('cell-28')
    var43=request.GET.get('cell-29')
    var44=request.GET.get('cell-30')
    var45=request.GET.get('cell-31')
    var46=request.GET.get('cell-32')
    var47=request.GET.get('cell-33')
    var48=request.GET.get('cell-34')
    var49=request.GET.get('cell-35')
    var51=request.GET.get('cell-36')
    var52=request.GET.get('cell-37')
    var53=request.GET.get('cell-38')
    var54=request.GET.get('cell-39')
    var55=request.GET.get('cell-40')
    var56=request.GET.get('cell-41')
    var57=request.GET.get('cell-42')
    var58=request.GET.get('cell-43')
    var59=request.GET.get('cell-44')
    var61=request.GET.get('cell-45')
    var62=request.GET.get('cell-46')
    var63=request.GET.get('cell-47')
    var64=request.GET.get('cell-48')
    var65=request.GET.get('cell-49')
    var66=request.GET.get('cell-50')
    var67=request.GET.get('cell-51')
    var68=request.GET.get('cell-52')
    var69=request.GET.get('cell-53')
    var71=request.GET.get('cell-54')
    var72=request.GET.get('cell-55')
    var73=request.GET.get('cell-56')
    var74=request.GET.get('cell-57')
    var75=request.GET.get('cell-58')
    var76=request.GET.get('cell-59')
    var77=request.GET.get('cell-60')
    var78=request.GET.get('cell-61')
    var79=request.GET.get('cell-62')
    var81=request.GET.get('cell-63')
    var82=request.GET.get('cell-64')
    var83=request.GET.get('cell-65')
    var84=request.GET.get('cell-66')
    var85=request.GET.get('cell-67')
    var86=request.GET.get('cell-68')
    var87=request.GET.get('cell-69')
    var88=request.GET.get('cell-70')
    var89=request.GET.get('cell-71')
    var91=request.GET.get('cell-71')
    var92=request.GET.get('cell-73')
    var93=request.GET.get('cell-74')
    var94=request.GET.get('cell-75')
    var95=request.GET.get('cell-76')
    var96=request.GET.get('cell-77')
    var97=request.GET.get('cell-78')
    var98=request.GET.get('cell-79')
    var99=request.GET.get('cell-80')
    
    

    mat=[[var11,var12,var13,var14,var15,var16,var17,var18,var19], 
        [var21,var22,var23,var24,var25,var26,var27,var28,var29], 
        [var31,var32,var33,var34,var35,var36,var37,var38,var39],
        [var41,var42,var43,var44,var45,var46,var47,var48,var49], 
        [var51,var52,var53,var54,var55,var56,var57,var58,var59],
        [var61,var62,var63,var64,var65,var66,var67,var68,var69],
        [var71,var72,var73,var74,var75,var76,var77,var78,var79],
        [var81,var82,var83,var84,var85,var86,var87,var88,var89],
        [var91,var92,var93,var94,var95,var96,var97,var98,var99]]
    
    matrix=[]
    for i in mat:
        l=[]
        for j in i:
            l.append(int(j))
        matrix.append(l)

    
    ans=solve_sudoku(matrix)
    
    
    d={
    'revar00':ans[0][0],
    'revar01':ans[0][1],
    'revar02':ans[0][2],
    'revar03':ans[0][3],
    'revar04':ans[0][4],
    'revar05':ans[0][5],
    'revar06':ans[0][6],
    'revar07':ans[0][7],
    'revar08':ans[0][8],
    'revar10':ans[1][0],
    'revar11':ans[1][1],
    'revar12':ans[1][2],
    'revar13':ans[1][3],
    'revar14':ans[1][4],
    'revar15':ans[1][5],
    'revar16':ans[1][6],
    'revar17':ans[1][7],
    'revar18':ans[1][8],
    'revar20':ans[2][0],
    'revar21':ans[2][1],
    'revar22':ans[2][2],
    'revar23':ans[2][3],
    'revar24':ans[2][4],
    'revar25':ans[2][5],
    'revar26':ans[2][6],
    'revar27':ans[2][7],
    'revar28':ans[2][8],
    'revar30':ans[3][0],
    'revar31':ans[3][1],
    'revar32':ans[3][2],
    'revar33':ans[3][3],
    'revar34':ans[3][4],
    'revar35':ans[3][5],
    'revar36':ans[3][6],
    'revar37':ans[3][7],
    'revar38':ans[3][8],
    'revar40':ans[4][0],
    'revar41':ans[4][1],
    'revar42':ans[4][2],
    'revar43':ans[4][3],
    'revar44':ans[4][4],
    'revar45':ans[4][5],
    'revar46':ans[4][6],
    'revar47':ans[4][7],
    'revar48':ans[4][8],
    'revar50':ans[5][0],
    'revar51':ans[5][1],
    'revar52':ans[5][2],
    'revar53':ans[5][3],
    'revar54':ans[5][4],
    'revar55':ans[5][5],
    'revar56':ans[5][6],
    'revar57':ans[5][7],
    'revar58':ans[5][8],
    'revar60':ans[6][0],
    'revar61':ans[6][1],
    'revar62':ans[6][2],
    'revar63':ans[6][3],
    'revar64':ans[6][4],
    'revar65':ans[6][5],
    'revar66':ans[6][6],
    'revar67':ans[6][7],
    'revar68':ans[6][8],
    'revar70':ans[7][0],
    'revar71':ans[7][1],
    'revar72':ans[7][2],
    'revar73':ans[7][3],
    'revar74':ans[7][4],
    'revar75':ans[7][5],
    'revar76':ans[7][6],
    'revar77':ans[7][7],
    'revar78':ans[7][8],
    'revar80':ans[8][0],
    'revar81':ans[8][1],
    'revar82':ans[8][2],
    'revar83':ans[8][3],
    'revar84':ans[8][4],
    'revar85':ans[8][5],
    'revar86':ans[8][6],
    'revar87':ans[8][7],
    'revar88':ans[8][8]}

    return render(request,'answer.html',d)