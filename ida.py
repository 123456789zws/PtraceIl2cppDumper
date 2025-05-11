# -*- coding: utf-8 -*-

def set_name(addr, name):
	new_name = name + '_' + hex(addr)
	idc.set_name(addr, new_name, SN_NOWARN | SN_NOCHECK)

def make_function(start, end):
	next_func = idc.get_next_func(start)
	if next_func < end:
		end = next_func
	if idc.get_func_attr(start, FUNCATTR_START) == start:
		ida_funcs.del_func(start)
	ida_funcs.add_func(start, end)

addresses = []
fun_infos = []
path = idaapi.ask_file(False, '*.txt', 'test_method_info.txt from PtraceIl2cppDumper')


with open(path,"r",encoding="utf-8") as name_f:
    all_lines = name_f.readlines()

for line in all_lines:
	if line == "":
		break
	# 确保地址有效
	item = line.split(":")
	if item[0] == "":
		continue 
	fun_name = item[1].replace("\n","")
	fun_addr = int(item[0],16)
	addresses.append(fun_addr)
	fun_infos.append((fun_addr,fun_name))

addresses.sort()

for index in range(len(addresses) - 1):
	start = addresses[index]
	end = addresses[index + 1]
	make_function(start, end)

for item in fun_infos:
	set_name(item[0], item[1])



print('Script finished!')

