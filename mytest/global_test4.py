import global_manager
import global_test2
import global_test1

global_manager._init()
global_manager.setValue('a','22')
print(global_manager._global_dict)
global_test1.test1()
global_test2.test()
