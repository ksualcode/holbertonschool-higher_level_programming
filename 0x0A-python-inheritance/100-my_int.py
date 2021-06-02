#!/usr/bin/python3
''' Module with just a silly class '''


class MyInt(int):
    ''' The silly and rebeld class '''

    def __eq__(self, n):
        ''' the EQ magic function '''
        return(super().__ne__(n))

    def __ne__(self, n):
        ''' the NE magic function '''
        return(super().__eq__(n))
