from abc import ABC,abstractmethod
import numpy

class Strategy(ABC):
    @abstractmethod
    def split_queue(self,requests_queue,num_chunks):
        pass
    
class NumpySplitStrategy(Strategy):
    def split_queue(self,requests_queue, num_chunks):
        numpy_chunks = numpy.array_split(requests_queue,num_chunks)
            
        fragmented_tasks_list = [list(chunk) for chunk in numpy_chunks]
        fragmented_tasks_list = [chunk for chunk in fragmented_tasks_list if chunk]
        
        return fragmented_tasks_list