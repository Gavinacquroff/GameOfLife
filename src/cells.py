# cells.py

import pygame as pyg

SIZE_S = 49
SIZE_L = 500
SIZE_TEST = 3
TESTING = False

# will want user input for intial state
def populate_surface(screen, small_screen):
    pxarray = pyg.PixelArray(small_screen)

    if (TESTING):
        print ('Testing with size ' + str((SIZE_S,SIZE_S)))
        pxarray[0, 0] = (255,255,255)
        pxarray[0, 1] = (255,255,255)
        pxarray[1, 0] = (255,255,255)
        pxarray[1, 1] = (255,255,255)
        pxarray[2, 1] = (255,255,255)

    else:
        pxarray[1][0] = (255,255,255)
        pxarray[2][1] = (255,255,255)
        pxarray[0][2] = (255,255,255)
        pxarray[1][2] = (255,255,255)
        pxarray[2][2] = (255,255,255)
#        pxarray[25][24] = (255,255,255)
#        pxarray[25][23] = (255,255,255)
#        pxarray[24,23] = (255,255,255)

    pxarray.close()
    pyg.transform.scale(small_screen, (SIZE_L,SIZE_L), screen)
    
    pyg.display.flip()

class Nbors(object):
    def __init__(self, pxarray, row = 0, col = 0, row_lim=0, col_lim=0):
        self._cells = [(row + 1, col + 1), (row, col + 1), (row - 1, col + 1), (row - 1, col), (row - 1, col - 1), (row, col - 1), (row + 1, col - 1), (row + 1, col)]
        self._live_cells = 0
        self._row = row
        self._col = col
        self._row_lim = row_lim
        self._col_lim = col_lim
        self._pxarray = pxarray

    def get_live_nbors(self):
        """Count all live neighbours"""
        #prnt = False
        if (self._pxarray[self._row][self._col] is not 0):
            prnt = True
            #print('\n----CELL: %s----' % str((self._row,self._col)))

        #count all live neighbours
        for i in self._cells:
            # check bounds
            if (0 <= i[0] < self._row_lim) and (0 <= i[1] < self._col_lim):
                #if(prnt):
                    #print('****NBORCELL: %s****' % str(i))
                if (self._pxarray[i[0]][i[1]] is not 0):
                    self._live_cells += 1
                    #if(prnt):
                        #print(str(i) + ' is an alive nbor')
        return self._live_cells

def update_cells(pxarray):
    """Run rules on all cells"""
    dead_cells = []
    new_cells = []
    ar_dims = pxarray.shape
    row_lim = ar_dims[0]
    col_lim = ar_dims[1]

    for row in range(row_lim):
        #print(row)
        for col in range(col_lim):
            #print(col)
            nbors = Nbors(pxarray, row, col, row_lim, col_lim)
            live_nbors = nbors.get_live_nbors()
            if pxarray[row, col] == 0xFFFFFF:
                #print('Cell ' + str((row, col)) +  ' has ' + str(live_nbors) + (' live neighbours'))
                # death by isolation
                if live_nbors <= 1:
                    dead_cells.append((row, col))
                    #print('DEATH by isolation: row ' + str(row) + ' col ' + str(col))
                # death by overcrowding
                elif live_nbors >= 4:
                    dead_cells.append((row, col))
                    #print('DEATH by overcrowding: row ' + str(row) + ' col ' + str(col))
            else:
                # birth
                if live_nbors == 3:
                    new_cells.append((row, col))
                    #print('BIRTH: row ' + str(row) + ' col ' + str(col))
    for cell in new_cells:
        pxarray[cell[0]][cell[1]] = 0xFFFFFF
    for cell in dead_cells:
        pxarray[cell[0]][cell[1]] = 0x0
        