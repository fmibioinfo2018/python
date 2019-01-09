from enum import Enum
import inspect

# Sequence class

def abstractmethod(method):
    """
    An @abstractmethod member fn decorator.
    (put this in some library somewhere for reuse).

    """
    def default_abstract_method(*args, **kwargs):
        raise NotImplementedError('call to abstract method ' 
                                  + repr(method))
    default_abstract_method.__name__ = method.__name__    
    return default_abstract_method

class Sequences:
    def __init__(self, sequences):
        self._seq = sequences

    @abstractmethod
    def parse(self):
        pass

INSTANCE_CACHE={}

class _Sequence:
    def __init__(self, content, timestamp):
        self._content = content
        self._timestamp = timestamp

class _FASTA_Sequence(_Sequence):
    def parse(self):
        return self._content

class _MULTI_FASTA_Sequence(_Sequence):
    def parse(self):
        return self._content

class _CLUSTEL_Sequence(_Sequence):
    def parse(self):
        return self._content


class _BaseSplitter:
    def get_splited_data(self, _x, _y, split_num=100):
        print("_BaseSplitter")


class _KFold(_BaseSplitter):
    def get_splited_data(self, _x, _y, split_num=100):
        print("_BaseSplitter")

class _LeavePOut(_BaseSplitter):
    def get_splited_data(self, _x, _y, split_num=100):
        print("_BaseSplitter")

class _ShuffleSplit(_BaseSplitter):
    def get_splited_data(self, _x, _y, split_num=100):
        print("_BaseSplitter")

class SplitMethod(Enum):
    LEAVE_P_OUT = _LeavePOut
    K_FOLD = _KFold
    SHUFFLE_SPLIT = _ShuffleSplit

class _SplitterFactory:
    __splitt_methods = {SplitMethod.K_FOLD: _KFold, SplitMethod.LEAVE_P_OUT: _LeavePOut, SplitMethod.SHUFFLE_SPLIT: _ShuffleSplit}

    @staticmethod
    def get_splitter_instance(_splitt_method):
        return _SplitterFactory.__splitt_methods[_splitt_method]()

class Splitter:
    '''
    Split data set _x, _y to train and test data sets.
    Use SplitMethod enum to define chouse method for splitting
    '''

    def __init__(self, split_method):
        self.split_method = split_method
        self._splitter = _SplitterFactory.get_splitter_instance(split_method)

    def split(self, _x, _y, split_n=100):
        """Generate indices to split data into training and test set.

        Parameters
        ----------
        _x : array-like, shape (n_samples, n_features)
            Training data, where n_samples is the number of samples
            and n_features is the number of features.

        _y : array-like, shape (n_samples,), optional
            The target variable for supervised learning problems.

        split_n : n_sample
        the samples used while splitting the dataset into train/test set."""

        return self.__get_splitted_data(_x, _y, self.split_method, split_n)

    def __get_splitted_data(self, __x, __y, __spliting_method, __split_n=100):
        _x_train = []
        _y_train = []
        _x_test = []
        _y_test = []

        for _train_index, _test_index in self._splitter.get_splited_data(__x, __y, split_num=__split_n):
            _x_train.extend(__x[_train_index])
            _x_test.extend(__x[_test_index])
            _y_train.extend(__y[_train_index])
            _y_test.extend(__y[_test_index])
            break

        return [_x_train, _y_train, _x_test, _y_test]