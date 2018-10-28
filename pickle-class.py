import pickle

class Record:
    def __init__(self,name,phone_number):
        self.name=name
        self.phone_number=phone_number
#dumps/loads
R=pickle.dumps(Record)
print(R)
print(pickle.loads(R))

record=Record("焦晓慧","13651287005")
r=pickle.dumps(record)
print(r)
print(pickle.loads(r))

#dump和load
import pickle
L=[1,2,3]
with open()