# -*- coding: iso-8859-15 -*-

class SuperClass(object):
    def __init__(self):
        self._superValue=""
        self._settings=[]

    def inheritance_mode_func(self):
        pass

class Template(SuperClass):
    def __init__(self):
        super(Template,self).__init__()
        self._value=""

    #Single Function
    @staticmethod
    def single_mode_func():
        pass

    #Multi Function
    def _multi_mode_func(self):
        self.single_mode_func()
        self._multi_mode_func()
        pass

    #Inheritance Function
    def _inheritance_mode_func(self):
        self.single_mode_func()
        self._multi_mode_func()
        self.inheritance_mode_func()
        pass

    #Private Function
    def __private_mode_func(self):
        self.single_mode_func()
        self._multi_mode_func()
        self.inheritance_mode_func()
        self._inheritance_mode_func()
        self._superValue
        pass

    #Setting Function
    def setSetting(self,variable):
        self._settings=variable
    def addSetting(self,variable):
        self._settings.append(variable)
    def currentSetting(self):
        self._settings=self.single_mode_func()
        return self._settings
    def getSetting(self):
        return self._settings

    #Public Function
    def public(self):
        self.single_mode_func()
        self._multi_mode_func()
        self.inheritance_mode_func()
        self._inheritance_mode_func()
        self.__private_mode_func()
        self._value
        self._superValue
        pass

    #Build Special Method
    def __new__(self,cls):
        pass

    def __del__(self):
        pass

    #Type Conversion Special Method
    def __repr__(self):
        # self.str=print(self)
        pass

    def __str__(self):
        # self.str=str(self)
        pass
    
    def __int__(self):
        # self.int=int(self)
        pass

    def __float__(self):
        # self.float=float(self)
        pass
    
    def __bytes__(self):
        #bytes(self)
        pass

    def __format__(self):
        # format(self)
        pass

    def __bool__(self):
        # bool(self)
        pass

    #Rich Comparison Special Method
    def __eq__(self,other):
        # self == other
        pass
    
    def __ne__(self,other):
        # self != other
        pass
    
    def __lt__(self,other):
        # self < other
        pass
    
    def __le__(self,other):
        # self <= other
        pass

    def __gt__(self,other):
        # self > other
        pass
    
    def __ge__(self,other):
        # self >= other
        pass

    #Arithmetic Operator Special Method
    def __add__(self,other):
        # self + other
        pass

    def __radd__(self,other):
        # other + self
        pass
    
    def __iadd__(self,other):
        # self += other
        pass

    def __sub__(self,other):
        # self - other
        pass
    
    def __rsub__(self,other):
        # other - self
        pass
    
    def __isub__(self,other):
        # self -= other
        pass

    def __mul__(self,otehr):
        # self * other
        pass

    def __rmul__(self,otehr):
        # other * self
        pass
    
    def __imul__(self,otehr):
        # self *= other
        pass

    def __matmul__(self,other):
        # self @ other
        pass

    def __rmatmul__(self,other):
        # other @ self
        pass

    def __imatmul__(self,other):
        # self @= other
        pass

    def __truediv__(self,other):
        # self / other
        pass

    def __rtruediv__(self,other):
        # other / self
        pass

    def __itruediv__(self,other):
        # self /= other
        pass

    def __floordiv__(self,other):
        # self // other
        pass
    
    def __rfloordiv__(self,other):
        # other // self
        pass

    def __ifloordiv__(self,other):
        # self //= other
        pass

    def __mod__(self,other):
        # self % other
        pass

    def __rmod__(self,other):
        # other % self
        pass
    
    def __imod__(self,other):
        # self %= other
        pass

    def __divmod__(self,other):
        # divmod()
        pass

    def __rdivmod__(self,other):
        pass
    
    def __idivmod__(self,other):
        pass

    def __pow__(self,other):
        # pow(self)
        pass

    def __rpow__(self,other):
        pass

    def __ipow__(self,other):
        pass

    #Bitwise Operator Special Method
    def __lshift__(self,other):
        # self << other
        pass

    def __rlshift__(self,other):
        # other << self
        pass

    def __ilshift__(self,other):
        # self <<= other
        pass

    def __rshift__(self,other):
        # self >> other
        pass

    def __rrshift__(self,other):
        # other >> self
        pass

    def __irshift__(self,other):
        # self >>= other
        pass

    def __and__(self,other):
        # self & other
        pass

    def __rand__(self,other):
        # other & self
        pass

    def __iand__(self,other):
        # self &= other
        pass

    def __or__(self,other):
        # self | other
        pass

    def __ror__(self,other):
        # other | self
        pass

    def __ior__(self,other):
        # self = other
        pass

    def __xor__(self,other):
        # self ^ other
        pass

    def __rxor__(self,other):
        # other ^ self
        pass

    def __ixor__(self,other):
        # self ^= other
        pass

    #Container  Special Method
    def __len__(self):
        # self.int=len(self)
        pass

    def __iter__(self):
        # self.int,self.value=iter(self)
        pass

    def __next__(self):
        pass
    
    def __getitem__(self,key):
        # self[key]

        # self.list=[0,1,2,3]
        # return self.list[key]
        pass

    def __setitem__(self,key,value):
        # self[key]=value

        # self.list=[0,1,2,3]
        # self.list.insert(key,value)
        pass

    def __delitem__(self,key):
        # del self[key]

        # del self.list[key]
        pass

    def __contains__(self,item):
        # value in self

        # bool=item in self.list
        pass

    #Attribute Special Method
    def __setattr__(self,nonName,value):
        # self.nonName=value
        pass
    
    def __getattr__(self,nonName):
        # self.nonName or self.nonName()
        pass

    def __getattribute__(self,nonName):
        # self.nonName or self.nonName()
        pass

    def __delattr__(self,name):
        # del self.name or del self.name()
        pass
    
    #Other Special Method
    def __copy__(self):
        pass

    def __deepcopy__(self):
        pass

    def __hash__(self):
        pass

    def __dir__(self):
        pass

    def __get__(self,instance,owner=None):
        pass
    
    def __set__(self,instance,value):
        pass

    def __delete__(self,instance):
        pass

    def __call__(self,args):
        pass

    def __missing__(self,key):
        pass

    def __reversed__(self):
        pass

    def __neg__(self):
        pass

    def __pos__(self):
        pass

    def __abs__(self):
        pass

    def __invert__(self):
        pass

    def __complex__(self):
        pass

    def __index__(self):
        pass

    def __round__(self):
        pass

    def __trunc__(self):
        pass

    def __floor__(self):
        pass

    def __ceil__(self):
        pass

    def __enter__(self):
        pass

    def __exit__(self):
        pass

    def __buffer__(self,flags):
        pass

    def __await__(self):
        pass
    
    def __aiter__(self):
        pass

    def __anext__(self):
        pass

    def __aenter__(self):
        pass

    def __aexit__(self):
        pass

    def __set_name__(self, owner, name):
        pass

    def __mro_entries__(self,bases):
        pass

    def __class_getitem__(cls,key):
        pass

    def __length_hint__(self):
        pass

    def __release_buffer__(self,buffer):
        pass