from os import listdir


# the_path = "D:\Users\mdieng\Documents\TOOLS\SDK\OS_11.12.2"
the_path = "D:\Program Files\TeliumSDK\SDK11.12.2.PatchP\Components\HW_TETRA\Platform\package"
for f in listdir(the_path):
    cmp_num, cmp_name = f[:f.find("_")], f[f.find("_")+1:-4]
    # print "%s + %s == %s" %(cmp_num[:-4], cmp_name, f)
    print "('%s', '%s', 'SYS')," % (cmp_num[:-4], cmp_name)